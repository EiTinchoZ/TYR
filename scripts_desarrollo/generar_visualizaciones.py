"""
Script para generar visualizaciones del proyecto TYR

Genera:
1. Matriz de confusión del modelo 4358
2. Gráfica de distribución de intenciones
3. Comparativa de modelos (evolución)
4. Métricas del modelo

Autor: Martín Bundy
Proyecto: TYR - Asistente Virtual ITSE
Fecha: 23 Noviembre 2025
"""

import json
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report
from pathlib import Path
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from tqdm import tqdm

# Configuración de estilo
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# Configuración
MODELO_PATH = "modelo_bert_tyr_4358"
DATASET_PATH = "Dataset_TYR_3000_FINAL.json"
OUTPUT_DIR = "documentacion/visualizaciones"
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# Crear directorio de salida
Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

print("=" * 70)
print("  GENERADOR DE VISUALIZACIONES - TYR")
print("=" * 70)
print(f"\nDispositivo: {DEVICE}")
print(f"Modelo: {MODELO_PATH}")
print(f"Dataset: {DATASET_PATH}")
print(f"Salida: {OUTPUT_DIR}/\n")


def cargar_modelo():
    """Cargar modelo BERT y tokenizer"""
    print("[*] Cargando modelo...")
    tokenizer = AutoTokenizer.from_pretrained(MODELO_PATH)
    model = AutoModelForSequenceClassification.from_pretrained(MODELO_PATH)
    model.to(DEVICE)
    model.eval()
    print("[OK] Modelo cargado\n")
    return tokenizer, model


def cargar_dataset():
    """Cargar dataset de entrenamiento"""
    print("[*] Cargando dataset...")
    with open(DATASET_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f"[OK] Dataset cargado: {len(data)} ejemplos\n")
    return data


def cargar_label_map():
    """Cargar mapeo de labels"""
    with open(f"{MODELO_PATH}/label_map.json", 'r', encoding='utf-8') as f:
        label_map_str = json.load(f)
    # Convertir claves a int
    idx_to_label = {int(k): v for k, v in label_map_str.items()}
    label_to_idx = {v: int(k) for k, v in label_map_str.items()}
    return label_to_idx, idx_to_label


def generar_predicciones(tokenizer, model, data, label_to_idx, max_samples=500):
    """Generar predicciones en una muestra del dataset"""
    print(f"[*] Generando predicciones (muestra de {max_samples})...")

    # Tomar muestra aleatoria
    np.random.seed(42)
    indices = np.random.choice(len(data), min(max_samples, len(data)), replace=False)
    muestra = [data[i] for i in indices]

    y_true = []
    y_pred = []

    for item in tqdm(muestra, desc="Prediciendo"):
        texto = item[0]  # Dataset es [texto, label_nombre]
        label_nombre = item[1]
        label_idx = label_to_idx[label_nombre]

        # Tokenizar
        inputs = tokenizer(
            texto,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=128
        ).to(DEVICE)

        # Predecir
        with torch.no_grad():
            outputs = model(**inputs)
            logits = outputs.logits
            pred = torch.argmax(logits, dim=1).item()

        y_true.append(label_idx)
        y_pred.append(pred)

    print(f"[OK] {len(y_pred)} predicciones generadas\n")
    return y_true, y_pred


def plot_confusion_matrix(y_true, y_pred, label_names, output_path):
    """Generar y guardar matriz de confusión"""
    print("[*] Generando matriz de confusión...")

    # Calcular matriz
    cm = confusion_matrix(y_true, y_pred)

    # Calcular accuracy
    accuracy = np.sum(np.diag(cm)) / np.sum(cm) * 100

    # Crear figura
    fig, ax = plt.subplots(figsize=(14, 12))

    # Plot matriz
    sns.heatmap(
        cm,
        annot=True,
        fmt='d',
        cmap='Blues',
        xticklabels=label_names,
        yticklabels=label_names,
        cbar_kws={'label': 'Cantidad de ejemplos'},
        ax=ax,
        linewidths=0.5,
        linecolor='gray'
    )

    # Configurar
    ax.set_xlabel('Predicción', fontsize=12, fontweight='bold')
    ax.set_ylabel('Etiqueta Real', fontsize=12, fontweight='bold')
    ax.set_title(
        f'Matriz de Confusión - Modelo TYR 4358\n'
        f'Accuracy: {accuracy:.2f}% (Dataset: 4,358 ejemplos)',
        fontsize=14,
        fontweight='bold',
        pad=20
    )

    # Rotar labels
    plt.setp(ax.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')
    plt.setp(ax.get_yticklabels(), rotation=0)

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    print(f"[OK] Guardado: {output_path}\n")
    plt.close()

    return accuracy


def plot_distribucion_intenciones(data, label_map, idx_to_label, output_path):
    """Generar gráfica de distribución de intenciones"""
    print("[*] Generando distribucion de intenciones...")

    # Contar por intención
    labels = [item[1] for item in data]  # Dataset es [texto, label_nombre]
    conteo = {}
    for nombre in labels:
        conteo[nombre] = conteo.get(nombre, 0) + 1

    # Ordenar por cantidad
    conteo_sorted = dict(sorted(conteo.items(), key=lambda x: x[1], reverse=True))

    # Crear figura
    fig, ax = plt.subplots(figsize=(12, 8))

    nombres = list(conteo_sorted.keys())
    valores = list(conteo_sorted.values())
    colores = sns.color_palette("husl", len(nombres))

    bars = ax.barh(nombres, valores, color=colores, edgecolor='black', linewidth=0.7)

    # Agregar valores en las barras
    for i, (bar, val) in enumerate(zip(bars, valores)):
        porcentaje = (val / len(data)) * 100
        ax.text(
            val + 20,
            bar.get_y() + bar.get_height() / 2,
            f'{val} ({porcentaje:.1f}%)',
            va='center',
            fontsize=10,
            fontweight='bold'
        )

    ax.set_xlabel('Cantidad de Ejemplos', fontsize=12, fontweight='bold')
    ax.set_ylabel('Intención', fontsize=12, fontweight='bold')
    ax.set_title(
        f'Distribución de Intenciones en Dataset TYR\n'
        f'Total: {len(data):,} ejemplos',
        fontsize=14,
        fontweight='bold',
        pad=20
    )
    ax.grid(axis='x', alpha=0.3, linestyle='--')

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    print(f"[OK] Guardado: {output_path}\n")
    plt.close()


def plot_evolucion_modelos(output_path):
    """Generar comparativa de evolución de modelos"""
    print("[*] Generando comparativa de modelos...")

    # Datos de evolución (según documentación del proyecto)
    modelos = ['Modelo v1\n(1,542 ejemplos)', 'Modelo v2\n(3,000 ejemplos)', 'Modelo v3\n(4,358 ejemplos)']
    accuracy = [96.2, 98.1, 98.93]
    f1_score = [95.8, 97.9, 98.92]
    precision = [95.9, 98.0, 98.92]
    recall = [96.0, 98.1, 98.93]

    # Crear figura con subplots
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Evolución de Métricas - Modelos TYR', fontsize=16, fontweight='bold', y=0.995)

    # Colores
    colores = ['#FF6B6B', '#4ECDC4', '#45B7D1']

    # 1. Accuracy
    ax = axes[0, 0]
    bars = ax.bar(modelos, accuracy, color=colores, edgecolor='black', linewidth=1.5, width=0.6)
    for bar, val in zip(bars, accuracy):
        ax.text(bar.get_x() + bar.get_width() / 2, val + 0.3, f'{val}%',
                ha='center', va='bottom', fontsize=11, fontweight='bold')
    ax.set_ylabel('Accuracy (%)', fontsize=11, fontweight='bold')
    ax.set_title('Accuracy por Modelo', fontsize=12, fontweight='bold')
    ax.set_ylim(94, 100)
    ax.grid(axis='y', alpha=0.3, linestyle='--')

    # 2. F1-Score
    ax = axes[0, 1]
    bars = ax.bar(modelos, f1_score, color=colores, edgecolor='black', linewidth=1.5, width=0.6)
    for bar, val in zip(bars, f1_score):
        ax.text(bar.get_x() + bar.get_width() / 2, val + 0.3, f'{val}%',
                ha='center', va='bottom', fontsize=11, fontweight='bold')
    ax.set_ylabel('F1-Score (%)', fontsize=11, fontweight='bold')
    ax.set_title('F1-Score por Modelo', fontsize=12, fontweight='bold')
    ax.set_ylim(94, 100)
    ax.grid(axis='y', alpha=0.3, linestyle='--')

    # 3. Precision
    ax = axes[1, 0]
    bars = ax.bar(modelos, precision, color=colores, edgecolor='black', linewidth=1.5, width=0.6)
    for bar, val in zip(bars, precision):
        ax.text(bar.get_x() + bar.get_width() / 2, val + 0.3, f'{val}%',
                ha='center', va='bottom', fontsize=11, fontweight='bold')
    ax.set_ylabel('Precision (%)', fontsize=11, fontweight='bold')
    ax.set_title('Precision por Modelo', fontsize=12, fontweight='bold')
    ax.set_ylim(94, 100)
    ax.grid(axis='y', alpha=0.3, linestyle='--')

    # 4. Recall
    ax = axes[1, 1]
    bars = ax.bar(modelos, recall, color=colores, edgecolor='black', linewidth=1.5, width=0.6)
    for bar, val in zip(bars, recall):
        ax.text(bar.get_x() + bar.get_width() / 2, val + 0.3, f'{val}%',
                ha='center', va='bottom', fontsize=11, fontweight='bold')
    ax.set_ylabel('Recall (%)', fontsize=11, fontweight='bold')
    ax.set_title('Recall por Modelo', fontsize=12, fontweight='bold')
    ax.set_ylim(94, 100)
    ax.grid(axis='y', alpha=0.3, linestyle='--')

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    print(f"[OK] Guardado: {output_path}\n")
    plt.close()


def generar_reporte_metricas(y_true, y_pred, label_names, output_path):
    """Generar reporte de clasificación y guardarlo"""
    print("[*] Generando reporte de metricas...")

    report = classification_report(
        y_true,
        y_pred,
        target_names=label_names,
        digits=4
    )

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("=" * 70 + "\n")
        f.write("  REPORTE DE CLASIFICACIÓN - MODELO TYR 4358\n")
        f.write("=" * 70 + "\n\n")
        f.write(f"Total de ejemplos evaluados: {len(y_true)}\n")
        f.write(f"Dataset completo: 4,358 ejemplos\n\n")
        f.write(report)
        f.write("\n" + "=" * 70 + "\n")

    print(f"[OK] Guardado: {output_path}\n")
    print(report)


def main():
    """Función principal"""
    # Cargar componentes
    tokenizer, model = cargar_modelo()
    data = cargar_dataset()
    label_to_idx, idx_to_label = cargar_label_map()

    # Obtener nombres de labels ordenados
    label_names = [idx_to_label[i] for i in range(len(idx_to_label))]

    # Generar predicciones
    y_true, y_pred = generar_predicciones(tokenizer, model, data, label_to_idx, max_samples=500)

    # Generar visualizaciones
    print("=" * 70)
    print("  GENERANDO VISUALIZACIONES")
    print("=" * 70 + "\n")

    # 1. Matriz de confusión
    accuracy = plot_confusion_matrix(
        y_true,
        y_pred,
        label_names,
        f"{OUTPUT_DIR}/matriz_confusion_4358.png"
    )

    # 2. Distribución de intenciones
    plot_distribucion_intenciones(
        data,
        label_to_idx,
        idx_to_label,
        f"{OUTPUT_DIR}/distribucion_intenciones.png"
    )

    # 3. Evolución de modelos
    plot_evolucion_modelos(f"{OUTPUT_DIR}/evolucion_modelos.png")

    # 4. Reporte de métricas
    generar_reporte_metricas(
        y_true,
        y_pred,
        label_names,
        f"{OUTPUT_DIR}/metricas_clasificacion.txt"
    )

    print("=" * 70)
    print("  [OK] VISUALIZACIONES COMPLETADAS")
    print("=" * 70)
    print(f"\nArchivos generados en: {OUTPUT_DIR}/")
    print(f"  1. matriz_confusion_4358.png")
    print(f"  2. distribucion_intenciones.png")
    print(f"  3. evolucion_modelos.png")
    print(f"  4. metricas_clasificacion.txt")
    print(f"\nAccuracy en muestra: {accuracy:.2f}%")
    print("\nListo para documentacion!\n")


if __name__ == "__main__":
    main()
