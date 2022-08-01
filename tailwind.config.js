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
        letterSpacing: {
            '1': '-0.014em'
        },
        extend: {
            transitionTimingFunction: {
                'in-expo': 'cubic-bezier(0.95, 0.05, 0.795, 0.035)',
                'out-expo': 'cubic-bezier(0.19, 1, 0.22, 1)',
                'custom': 'cubic-bezier(0.645, 0.045, 0.355, 1)',
            },
            saturate: {
                25: '.25',
                75: '.75',
            }
        },
    },
    variants: {
        extend: {
            borderWidth: ['hover', 'group-hover'],
            letterSpacing: ['hover', 'group-hover'],
            borderOpacity: ['hover', 'group-hover'],
            fontWeight: ['hover', 'group-hover'],
            display: ['last'],
            translate: ['hover', 'group-hover'],
            saturate: ['hover', 'group-hover'],
            scale: ['hover', 'group-hover', 'active', 'focus'],
            cursor: ['hover', 'group-hover'],
        },
    },
    plugins: [

    ],
}