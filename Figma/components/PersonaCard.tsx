import { motion } from 'motion/react';
import { useScrollAnimation } from '../hooks/useScrollAnimation';

interface PersonaCardProps {
  emoji?: string;
  illustrationSrc?: string;
  title: string;
  metadata: string;
  quote: string;
  name: string;
  location: string;
}

export function PersonaCard({ emoji, illustrationSrc, title, metadata, quote, name, location }: PersonaCardProps) {
  const { ref, isVisible } = useScrollAnimation(0.3);

  return (
    <motion.div
      ref={ref}
      initial={{ opacity: 0, scale: 0.9 }}
      animate={isVisible ? { opacity: 1, scale: 1 } : { opacity: 0, scale: 0.9 }}
      transition={{ duration: 0.5 }}
      className="bg-[#262730] border-2 border-[#31333F] rounded-[12px] p-[32px] text-center transition-all duration-500 hover:border-[#0066CC] hover:shadow-[0_12px_40px_rgba(0,102,204,0.4)] hover:-translate-y-2 hover:scale-[1.02] cursor-pointer"
    >
      <div className="mb-[20px] flex justify-center">
        {illustrationSrc ? (
          <img src={illustrationSrc} alt={name} className="w-32 h-32 object-contain rounded-2xl" loading="lazy" />
        ) : (
          <div className="text-[64px]">{emoji}</div>
        )}
      </div>
      
      <h3 
        className="text-[18px] text-[#3399FF] mb-[4px]"
        style={{ 
          fontFamily: 'Inter', 
          fontWeight: 600
        }}
      >
        {title}
      </h3>
      
      <p 
        className="text-[14px] text-[#B3B3B3] mb-[20px]"
        style={{ 
          fontFamily: 'IBM Plex Sans',
          fontWeight: 400
        }}
      >
        {metadata}
      </p>
      
      <p 
        className="text-[16px] text-[#FAFAFA] my-[20px] italic"
        style={{ 
          fontFamily: 'IBM Plex Sans',
          fontWeight: 400,
          lineHeight: 1.6
        }}
      >
        "{quote}"
      </p>
      
      <div className="pt-[20px] border-t border-[#31333F]">
        <p 
          className="text-[14px] text-[#FAFAFA] mb-1"
          style={{ 
            fontFamily: 'IBM Plex Sans',
            fontWeight: 600
          }}
        >
          {name}
        </p>
        <p 
          className="text-[14px] text-[#B3B3B3]"
          style={{ 
            fontFamily: 'IBM Plex Sans',
            fontWeight: 400
          }}
        >
          📍 {location}
        </p>
      </div>
    </motion.div>
  );
}
