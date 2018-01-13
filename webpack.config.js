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
        new webpack.ProvidePlugin({
            $: 'jquery',
            jQuery: 'jquery',
            'window.jQuery': 'jquery'
        })
    ],
}
