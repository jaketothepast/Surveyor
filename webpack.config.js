var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
    // Base directory for resolving entry options
    context: __dirname,

    // The entry point for webpack
    entry: './assets/js/index',

    output: {
        // Where the compiled bundle is stored
        // uses the path library
        path: path.resolve('./assets/bundles/'),
        // naming conventions webpack uses
        filename: '[name]-[hash].js'
    },

    plugins: [
        // Where to store bundle metadata
        new BundleTracker({filename: './webpack-stats.json'}),
        // Make JQuery available in modules
        // Point the node module at variables it exposes
        new webpack.ProvidePlugin({
            $: 'jquery',
            jQuery: 'jquery',
            'window.jQuery': 'jquery'
        })
    ],

    module: {
        loaders: [
            //Regex that tells webpack to use loaders

            // Load JS and JSX files
            {test: /\.jsx?$/,

             // Dont transpile all files in node_modules
             exclude: /node_modules/,

             // Use the Babel loader
             loader: 'babel-loader',

             query: {
                 // We will be dealing with React
                 presets: ['react']
             }}
        ]
    },

    resolve: {
        //Where to look for modules
        modules: ['node_modules'],
        // Extensions used to resolve modules
        extensions: ['.js', '.jsx']
    }
}
