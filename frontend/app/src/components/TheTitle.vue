<template>
  <h1 
    :class="{ 'TheTitle--bordered': bordered }" 
    class="TheTitle"
  >
    <slot/>
  </h1>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .TheTitle {
    color: $foreground-dark-color;
    padding-left: 20px;
    font-size: 24px;
    font-weight: 800;

    &--bordered {
      border-bottom: 2px solid $foreground-primary-color;
    }
  }
</style>

<script>
  export default {
    props: {
      bordered: {
        type: Boolean,
        default: true,
      },
    },
  };
</script>
