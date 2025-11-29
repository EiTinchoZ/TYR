"""
Script para preprocesar el dataset expandido de 4358 ejemplos
Genera archivos .pt para entrenamiento de BERT
"""

import json
import torch
from transformers import AutoTokenizer
from sklearn.model_selection import train_test_split
from collections import Counter

# Configuración
MODEL_NAME = "dccuchile/bert-base-spanish-wwm-cased"
MAX_LENGTH = 128
DATA_DIR = "./data"
DATASET_FILE = "Dataset_TYR_3000_FINAL.json"

print("=" * 60)
print("PREPROCESANDO DATASET TYR - 4358 EJEMPLOS")
print("=" * 60)

# 1. Cargar dataset
print(f"\nPASO 1: Cargando dataset {DATASET_FILE}...")
with open(DATASET_FILE, 'r', encoding='utf-8') as f:
    dataset = json.load(f)

print(f"OK Ejemplos cargados: {len(dataset)}")

# 2. Mostrar distribución
intenciones = Counter([x[1] for x in dataset])
print("\nDistribucion por intencion:")
for intencion, count in sorted(intenciones.items()):
    print(f"  {intencion}: {count}")

# 3. Crear mapeo de etiquetas
print("\nPASO 2: Creando mapeo de etiquetas...")
unique_labels = sorted(set([x[1] for x in dataset]))
label2id = {label: idx for idx, label in enumerate(unique_labels)}
id2label = {idx: label for label, idx in label2id.items()}

print(f"OK {len(unique_labels)} intenciones encontradas:")
for idx, label in id2label.items():
    print(f"  {idx}: {label}")

# 4. Convertir a formato (texto, label_id)
print("\nPASO 3: Convirtiendo a formato (texto, label_id)...")
textos = [x[0] for x in dataset]
labels = [label2id[x[1]] for x in dataset]

print(f"OK {len(textos)} textos preparados")

# 5. Split train/val/test (70/15/15)
print("\nPASO 4: Dividiendo dataset (70% train, 15% val, 15% test)...")
train_texts, temp_texts, train_labels, temp_labels = train_test_split(
    textos, labels, test_size=0.30, random_state=42, stratify=labels
)

val_texts, test_texts, val_labels, test_labels = train_test_split(
    temp_texts, temp_labels, test_size=0.50, random_state=42, stratify=temp_labels
)

print(f"OK Train: {len(train_texts)} ejemplos")
print(f"OK Val:   {len(val_texts)} ejemplos")
print(f"OK Test:  {len(test_texts)} ejemplos")

# 6. Cargar tokenizer
print(f"\nPASO 5: Cargando tokenizer {MODEL_NAME}...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
print("OK Tokenizer cargado")

# 7. Tokenizar datasets
print("\nPASO 6: Tokenizando datasets...")

def tokenize_data(texts, labels):
    """Tokeniza textos y crea dataset de PyTorch"""
    encodings = tokenizer(
        texts,
        truncation=True,
        padding='max_length',
        max_length=MAX_LENGTH,
        return_tensors='pt'
    )

    dataset = torch.utils.data.TensorDataset(
        encodings['input_ids'],
        encodings['attention_mask'],
        torch.tensor(labels)
    )

    return dataset

print("  Tokenizando train...")
train_dataset = tokenize_data(train_texts, train_labels)

print("  Tokenizando val...")
val_dataset = tokenize_data(val_texts, val_labels)

print("  Tokenizando test...")
test_dataset = tokenize_data(test_texts, test_labels)

print("OK Tokenizacion completada")

# 8. Guardar datasets
print(f"\nPASO 7: Guardando datasets en {DATA_DIR}/...")
import os
os.makedirs(DATA_DIR, exist_ok=True)

torch.save(train_dataset, f"{DATA_DIR}/train_dataset.pt")
torch.save(val_dataset, f"{DATA_DIR}/val_dataset.pt")
torch.save(test_dataset, f"{DATA_DIR}/test_dataset.pt")

# Guardar label_map
with open(f"{DATA_DIR}/label_map.json", 'w', encoding='utf-8') as f:
    json.dump(id2label, f, ensure_ascii=False, indent=2)

print("OK Archivos guardados:")
print(f"  {DATA_DIR}/train_dataset.pt")
print(f"  {DATA_DIR}/val_dataset.pt")
print(f"  {DATA_DIR}/test_dataset.pt")
print(f"  {DATA_DIR}/label_map.json")

# Resumen final
print("\n" + "=" * 60)
print("PREPROCESAMIENTO COMPLETADO")
print("=" * 60)
print(f"\nDataset expandido:")
print(f"  Total ejemplos: {len(dataset)}")
print(f"  Train: {len(train_dataset)} (70%)")
print(f"  Val:   {len(val_dataset)} (15%)")
print(f"  Test:  {len(test_dataset)} (15%)")
print(f"  Intenciones: {len(unique_labels)}")
print("\nProximo paso: Ejecutar bert_training.py para entrenar BERT")
print("=" * 60)
