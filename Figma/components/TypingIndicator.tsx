import { motion } from 'motion/react';

export function TypingIndicator() {
  const dotVariants = {
    initial: { y: 0 },
    animate: { y: -8 },
  };

  const dotTransition = {
    duration: 0.5,
    repeat: Infinity,
    repeatType: "reverse" as const,
    ease: "easeInOut",
  };

  return (
    <div className="flex items-center gap-1">
      <motion.div
        className="size-2 bg-[#B3B3B3] rounded-full"
        variants={dotVariants}
        initial="initial"
        animate="animate"
        transition={{ ...dotTransition, delay: 0 }}
      />
      <motion.div
        className="size-2 bg-[#B3B3B3] rounded-full"
        variants={dotVariants}
        initial="initial"
        animate="animate"
        transition={{ ...dotTransition, delay: 0.2 }}
      />
      <motion.div
        className="size-2 bg-[#B3B3B3] rounded-full"
        variants={dotVariants}
        initial="initial"
        animate="animate"
        transition={{ ...dotTransition, delay: 0.4 }}
      />
    </div>
  );
}
