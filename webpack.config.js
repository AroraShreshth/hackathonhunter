const path = require('path');
const VueLoaderPlugin = require('vue-loader/lib/plugin')

module.exports = {
    // path to our input file
    entry: './assets/index.js',
  output: {
    filename: 'index-bundle.js',  // output bundle file name
    path: path.resolve(__dirname, './staticfiles'),  // path to our Django static directory
  },

  module: {
    rules: [
      {
        test: /\.vue$/,
        loader: 'vue-loader'
      },
      // this will apply to both plain `.js` files
      // AND `<script>` blocks in `.vue` files
      {
        test: /\.js$/,
        loader: 'babel-loader'
      },
      // this will apply to both plain `.css` files
      // AND `<style>` blocks in `.vue` files
      {
        test: /\.css$/,
        use: [
          'vue-style-loader',
          'css-loader'
        ]
      }
    ]
  },

  plugins: [
    // make sure to include the plugin!
    new VueLoaderPlugin()
  ]
};

