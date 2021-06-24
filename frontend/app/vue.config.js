module.exports = {
  devServer: {
    disableHostCheck: true,
  },
  css: {
    loaderOptions: {
      sass: {
        // prependData: `@import "@/styles/_variables.scss";`
      },
    },
  },
};
