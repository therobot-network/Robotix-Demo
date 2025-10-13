/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        // Dark mode color palette using OKLCH for perceptual uniformity - Enhanced Contrast
        background: {
          DEFAULT: 'oklch(0.12 0.015 195)', // Deep black with teal hint
          elevated: 'oklch(0.16 0.02 195)', // Slightly lighter for cards
          hover: 'oklch(0.20 0.025 195)', // Hover state
        },
        surface: {
          DEFAULT: 'oklch(0.18 0.02 195)', // Card backgrounds
          elevated: 'oklch(0.24 0.03 195)', // Elevated surfaces
          muted: 'oklch(0.14 0.015 195)', // Muted backgrounds
        },
        primary: {
          DEFAULT: 'oklch(0.62 0.12 195)', // Vibrant cyan-teal
          50: 'oklch(0.96 0.03 195)',
          100: 'oklch(0.92 0.05 195)',
          200: 'oklch(0.85 0.08 195)',
          300: 'oklch(0.75 0.10 195)',
          400: 'oklch(0.68 0.11 195)',
          500: 'oklch(0.62 0.12 195)',
          600: 'oklch(0.52 0.11 195)',
          700: 'oklch(0.45 0.10 195)',
          800: 'oklch(0.38 0.08 195)',
          900: 'oklch(0.30 0.06 195)',
          950: 'oklch(0.22 0.05 195)',
        },
        secondary: {
          DEFAULT: 'oklch(0.68 0.22 320)', // Vibrant magenta-pink
          50: 'oklch(0.96 0.05 320)',
          100: 'oklch(0.92 0.10 320)',
          200: 'oklch(0.85 0.14 320)',
          300: 'oklch(0.75 0.18 320)',
          400: 'oklch(0.70 0.20 320)',
          500: 'oklch(0.68 0.22 320)',
          600: 'oklch(0.58 0.20 320)',
          700: 'oklch(0.48 0.17 320)',
          800: 'oklch(0.40 0.14 320)',
          900: 'oklch(0.32 0.12 320)',
        },
        accent: {
          DEFAULT: 'oklch(0.72 0.20 45)', // Vibrant amber-gold
          50: 'oklch(0.96 0.05 45)',
          100: 'oklch(0.92 0.10 45)',
          200: 'oklch(0.85 0.14 45)',
          300: 'oklch(0.78 0.17 45)',
          400: 'oklch(0.73 0.19 45)',
          500: 'oklch(0.72 0.20 45)',
          600: 'oklch(0.62 0.18 45)',
          700: 'oklch(0.52 0.16 45)',
          800: 'oklch(0.44 0.14 45)',
          900: 'oklch(0.36 0.12 45)',
        },
        text: {
          DEFAULT: 'oklch(0.98 0.005 195)', // Primary text - very light
          muted: 'oklch(0.78 0.015 195)', // Secondary text
          subtle: 'oklch(0.65 0.02 195)', // Tertiary text
          inverse: 'oklch(0.25 0.02 195)', // For light backgrounds
        },
        border: {
          DEFAULT: 'oklch(0.35 0.03 195)', // Default borders
          subtle: 'oklch(0.28 0.025 195)', // Subtle borders
          focus: 'oklch(0.68 0.11 195)', // Focus rings
        },
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        display: ['Poppins', 'system-ui', 'sans-serif'],
      },
      animation: {
        'fade-in': 'fadeIn 0.8s ease-out',
        'slide-up': 'slideUp 0.6s ease-out',
        'slide-down': 'slideDown 0.6s ease-out',
        'float': 'float 6s ease-in-out infinite',
        'pulse-slow': 'pulse-slow 4s ease-in-out infinite',
        'gradient-shift': 'gradient-shift 8s ease infinite',
        'blob': 'blob 7s ease-in-out infinite',
        'orbit': 'orbit 20s linear infinite',
        'shimmer': 'shimmer 3s linear infinite',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0', transform: 'translateY(10px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
        slideUp: {
          '0%': { transform: 'translateY(30px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
        slideDown: {
          '0%': { transform: 'translateY(-30px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
        float: {
          '0%, 100%': { transform: 'translateY(0px) rotate(0deg)' },
          '50%': { transform: 'translateY(-20px) rotate(5deg)' },
        },
        'pulse-slow': {
          '0%, 100%': { opacity: '1', transform: 'scale(1)' },
          '50%': { opacity: '0.8', transform: 'scale(1.05)' },
        },
        'gradient-shift': {
          '0%, 100%': { backgroundPosition: '0% 50%' },
          '50%': { backgroundPosition: '100% 50%' },
        },
        blob: {
          '0%, 100%': { transform: 'translate(0, 0) scale(1)' },
          '33%': { transform: 'translate(30px, -50px) scale(1.1)' },
          '66%': { transform: 'translate(-20px, 20px) scale(0.9)' },
        },
        orbit: {
          '0%': { transform: 'rotate(0deg) translateX(100px) rotate(0deg)' },
          '100%': { transform: 'rotate(360deg) translateX(100px) rotate(-360deg)' },
        },
        shimmer: {
          '0%': { backgroundPosition: '-1000px 0' },
          '100%': { backgroundPosition: '1000px 0' },
        },
      },
    },
  },
  plugins: [],
};

