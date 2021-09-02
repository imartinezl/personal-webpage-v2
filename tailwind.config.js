module.exports = {
    purge: [
        './_includes/**/*.html',
        './_layouts/**/*.html',
        './_posts/*.md',
        './*.html',
        './assets/css/*.scss'
    ],
    darkMode: false, // or 'media' or 'class'
    theme: {
        extend: {
        },
    },
    variants: {
        extend: {
            borderWidth: ['hover', 'group-hover'],
            borderOpacity: ['hover', 'group-hover'],
            fontWeight: ['hover', 'group-hover']
        },
    },
    plugins: [

    ],
}