import { useEffect, useRef, useState } from 'react';
import { motion } from 'motion/react';
import { useScrollAnimation } from '../hooks/useScrollAnimation';

interface StatsCardProps {
  number: string;
  label: string;
}

export function StatsCard({ number, label }: StatsCardProps) {
  const { ref, isVisible } = useScrollAnimation(0.3);
  const [displayNumber, setDisplayNumber] = useState('0');
  const hasAnimated = useRef(false);

  useEffect(() => {
    if (isVisible && !hasAnimated.current) {
      hasAnimated.current = true;
      
      // Check if number contains a numeric value
      const numMatch = number.match(/\d+\.?\d*/);
      if (numMatch) {
        const targetNum = parseFloat(numMatch[0]);
        const suffix = number.replace(numMatch[0], '');
        const isDecimal = number.includes('.');
        const duration = 1500; // 1.5s
        const steps = 60;
        const increment = targetNum / steps;
        let current = 0;
        
        const timer = setInterval(() => {
          current += increment;
          if (current >= targetNum) {
            setDisplayNumber(number);
            clearInterval(timer);
          } else {
            if (isDecimal) {
              setDisplayNumber(current.toFixed(2) + suffix);
            } else {
              setDisplayNumber(Math.floor(current).toString() + suffix);
            }
          }
        }, duration / steps);

        return () => clearInterval(timer);
      } else {
        // If not numeric (like "24/7"), just show it
        setDisplayNumber(number);
      }
    }
  }, [isVisible, number]);

  return (
    <motion.div
      ref={ref}
      initial={{ opacity: 0, scale: 0.8 }}
      animate={isVisible ? { opacity: 1, scale: 1 } : { opacity: 0, scale: 0.8 }}
      transition={{ duration: 0.5 }}
      className="bg-[#262730] border border-[#31333F] rounded-[12px] p-[32px] text-center transition-all duration-300 hover:border-[#0066CC] hover:shadow-[0_8px_24px_rgba(0,102,204,0.3)] hover:-translate-y-1"
    >
      <div 
        className="text-[42px] text-[#3399FF] mb-2"
        style={{ 
          fontFamily: 'Inter', 
          fontWeight: 700,
          lineHeight: 1.2
        }}
      >
        {displayNumber}
      </div>
      <div 
        className="text-[14px] text-[#B3B3B3]"
        style={{ 
          fontFamily: 'IBM Plex Sans',
          fontWeight: 400
        }}
      >
        {label}
      </div>
    </motion.div>
  );
}
