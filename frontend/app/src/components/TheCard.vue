<template>
  <article class="TheCard">
    <slot/>
  </article>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  $background-transition-time: 400ms;

  .TheCard {
    background-color: $background-secondary-color;
    border: 1px solid $background-secondary-border;
    border-radius: 5px;
    margin: 20px;
  }
</style>

<script>
  export default {};
</script>
