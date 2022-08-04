const colors = require('tailwindcss/colors')

module.exports = {
  // mode: 'jit',
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
    require('@tailwindcss/aspect-ratio'),
    require('@tailwindcss/line-clamp'),
  ],
  purge: [
    './templates/*.html',
  ],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        'pink': colors.pink,
        'cyan': colors.cyan,
      }
    },
  },
  variants: {
    extend: {
      opacity: ['disabled'],
      animation: ['responsive', 'motion-safe', 'motion-reduce', 'hover']
    }
  },
}
