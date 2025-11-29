import { motion } from 'motion/react';
import { useScrollAnimation } from '../hooks/useScrollAnimation';

interface FeatureCardProps {
  emoji?: string;
  iconSrc?: string;
  icon?: React.ReactNode;
  title: string;
  description: string;
}

export function FeatureCard({ emoji, iconSrc, icon, title, description }: FeatureCardProps) {
  const { ref, isVisible } = useScrollAnimation(0.3);

  return (
    <motion.div
      ref={ref}
      initial={{ opacity: 0, scale: 0.9 }}
      animate={isVisible ? { opacity: 1, scale: 1 } : { opacity: 0, scale: 0.9 }}
      transition={{ duration: 0.5 }}
      className="bg-[#262730] border border-[#31333F] rounded-[12px] p-[24px] transition-all duration-500 hover:border-[#0066CC] hover:shadow-[0_12px_40px_rgba(0,102,204,0.4)] hover:-translate-y-2 hover:scale-[1.02] cursor-pointer"
    >
      <div className="mb-[16px]">
        {iconSrc ? (
          <img src={iconSrc} alt={title} className="w-12 h-12 rounded-xl" loading="lazy" />
        ) : icon ? (
          <div className="text-[48px]">{icon}</div>
        ) : (
          <div className="text-[48px]">{emoji}</div>
        )}
      </div>
      <h3 
        className="text-[20px] text-[#FAFAFA] mb-[12px]"
        style={{ 
          fontFamily: 'Inter', 
          fontWeight: 600,
          lineHeight: 1.3
        }}
      >
        {title}
      </h3>
      <p 
        className="text-[14px] text-[#B3B3B3] mb-[16px]"
        style={{ 
          fontFamily: 'IBM Plex Sans',
          fontWeight: 400,
          lineHeight: 1.6
        }}
      >
        {description}
      </p>
      <a 
        href="#" 
        className="text-[#3399FF] hover:text-[#FAFAFA] inline-flex items-center gap-1 transition-colors duration-300 group"
        style={{ 
          fontFamily: 'IBM Plex Sans',
          fontWeight: 500,
          fontSize: '14px'
        }}
      >
        <span className="relative">
          Explorar
          <span className="absolute bottom-0 left-0 w-0 h-[1px] bg-[#3399FF] transition-all duration-300 group-hover:w-full"></span>
        </span>
        →
      </a>
    </motion.div>
  );
}
