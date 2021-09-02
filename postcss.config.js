module.exports = {
    parser: 'postcss-scss',
    plugins: [
        require("postcss-import"),
        require('tailwindcss'),
        require('autoprefixer'),
        ...(process.env.JEKYLL_ENV == "production" // example of only using a plugin in production
            ?
            [require("cssnano")({ preset: "default" })] : [])
    ]
}