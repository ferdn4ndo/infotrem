<template>
  <div class="HorizontalRuler">{{ text }}</div>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .HorizontalRuler {
    display: flex;
    align-items: center;
    text-align: center;
    margin: 10px 0;

    &::before,
    &::after {
      content: "";
      flex: 1;
      border-bottom: 1px solid $color-secondary-border;
    }

    &::before {
      margin-right: 0.25em;
    }

    &::after {
      margin-left: 0.25em;
    }
  }
</style>

<script>
  export default {
    props: {
      text: {
        type: String,
        default: "",
      },
    },
  };
</script>
