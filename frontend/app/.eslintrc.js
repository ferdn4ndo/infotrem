module.exports = {
  root: true,
  env: {
    node: true,
  },
  extends: ["plugin:vue/recommended"],
  rules: {
    "comma-dangle": [2, "always-multiline"],
    "no-console": process.env.NODE_ENV === "production" ? "error" : "off",
    "no-debugger": process.env.NODE_ENV === "production" ? "error" : "off",
    "vue/html-closing-bracket-newline": ["error", {
      "singleline": "never",
      "multiline": "always",
    }],
  },
  parserOptions: {
    parser: "babel-eslint",
  },
};
