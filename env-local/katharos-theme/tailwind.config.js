/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './views/**/*.xml',
    './static/src/js/**/*.js',
    './static/src/scss/**/*.scss',
  ],
  darkMode: 'class', // atau 'media' atau 'class'
  theme: {
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [],
}

