import { MessageCircle, Menu, X } from "lucide-react";
import { useState } from "react";
import { motion, AnimatePresence } from "motion/react";

export function Header() {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  return (
    <header className="fixed top-0 left-0 right-0 bg-[#0e1117]/95 backdrop-blur-md border-b border-[#31333F] z-50">
      <div className="container mx-auto px-4 md:px-6 lg:px-8 h-[64px] flex items-center justify-between">
        {/* Logo */}
        <div className="flex items-center gap-3">
          <div className="size-8 rounded-full bg-gradient-to-br from-[#0066CC] to-[#004C99] flex items-center justify-center">
            <MessageCircle className="size-4 text-[#FAFAFA]" />
          </div>
          <span 
            className="text-[#FAFAFA]"
            style={{ 
              fontFamily: 'Inter', 
              fontWeight: 600,
              fontSize: '18px'
            }}
          >
            TYR
          </span>
        </div>

        {/* Desktop Navigation */}
        <nav className="hidden md:flex items-center gap-6 lg:gap-8">
          <a 
            href="#hero" 
            className="text-[#B3B3B3] hover:text-[#3399FF] transition-colors duration-300"
            style={{ 
              fontFamily: 'IBM Plex Sans', 
              fontSize: '14px',
              fontWeight: 500
            }}
          >
            Inicio
          </a>
          <a 
            href="#features" 
            className="text-[#B3B3B3] hover:text-[#3399FF] transition-colors duration-300"
            style={{ 
              fontFamily: 'IBM Plex Sans', 
              fontSize: '14px',
              fontWeight: 500
            }}
          >
            Características
          </a>
          <a 
            href="#demo" 
            className="text-[#B3B3B3] hover:text-[#3399FF] transition-colors duration-300"
            style={{ 
              fontFamily: 'IBM Plex Sans', 
              fontSize: '14px',
              fontWeight: 500
            }}
          >
            Demo
          </a>
          <a 
            href="#contact" 
            className="text-[#B3B3B3] hover:text-[#3399FF] transition-colors duration-300"
            style={{ 
              fontFamily: 'IBM Plex Sans', 
              fontSize: '14px',
              fontWeight: 500
            }}
          >
            Contacto
          </a>
        </nav>

        {/* CTA Button - Desktop */}
        <button 
          className="hidden md:block bg-[#0066CC] text-[#FAFAFA] px-[20px] lg:px-[24px] py-[10px] rounded-[20px] transition-all duration-300 hover:bg-[#004C99] hover:scale-105 cursor-pointer"
          style={{ 
            fontFamily: 'IBM Plex Sans', 
            fontSize: '14px',
            fontWeight: 600
          }}
        >
          Probar TYR
        </button>

        {/* Mobile Menu Button */}
        <button
          className="md:hidden text-[#FAFAFA] p-2"
          onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
          aria-label="Toggle menu"
        >
          {mobileMenuOpen ? <X className="size-6" /> : <Menu className="size-6" />}
        </button>
      </div>

      {/* Mobile Menu */}
      <AnimatePresence>
        {mobileMenuOpen && (
          <motion.div
            initial={{ opacity: 0, height: 0 }}
            animate={{ opacity: 1, height: "auto" }}
            exit={{ opacity: 0, height: 0 }}
            className="md:hidden bg-[#0e1117] border-b border-[#31333F] overflow-hidden"
          >
            <nav className="container mx-auto px-4 py-4 flex flex-col gap-4">
              <a 
                href="#hero" 
                className="text-[#B3B3B3] hover:text-[#3399FF] transition-colors duration-300 py-2"
                style={{ 
                  fontFamily: 'IBM Plex Sans', 
                  fontSize: '16px',
                  fontWeight: 500
                }}
                onClick={() => setMobileMenuOpen(false)}
              >
                Inicio
              </a>
              <a 
                href="#features" 
                className="text-[#B3B3B3] hover:text-[#3399FF] transition-colors duration-300 py-2"
                style={{ 
                  fontFamily: 'IBM Plex Sans', 
                  fontSize: '16px',
                  fontWeight: 500
                }}
                onClick={() => setMobileMenuOpen(false)}
              >
                Características
              </a>
              <a 
                href="#demo" 
                className="text-[#B3B3B3] hover:text-[#3399FF] transition-colors duration-300 py-2"
                style={{ 
                  fontFamily: 'IBM Plex Sans', 
                  fontSize: '16px',
                  fontWeight: 500
                }}
                onClick={() => setMobileMenuOpen(false)}
              >
                Demo
              </a>
              <a 
                href="#contact" 
                className="text-[#B3B3B3] hover:text-[#3399FF] transition-colors duration-300 py-2"
                style={{ 
                  fontFamily: 'IBM Plex Sans', 
                  fontSize: '16px',
                  fontWeight: 500
                }}
                onClick={() => setMobileMenuOpen(false)}
              >
                Contacto
              </a>
              <button 
                className="w-full bg-[#0066CC] text-[#FAFAFA] px-[24px] py-[12px] rounded-[20px] transition-all duration-300 hover:bg-[#004C99] cursor-pointer mt-2"
                style={{ 
                  fontFamily: 'IBM Plex Sans', 
                  fontSize: '16px',
                  fontWeight: 600
                }}
                onClick={() => setMobileMenuOpen(false)}
              >
                Probar TYR
              </button>
            </nav>
          </motion.div>
        )}
      </AnimatePresence>
    </header>
  );
}