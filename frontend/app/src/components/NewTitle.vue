<template>
  <div class="title-box">
    <slot></slot>
  </div>
</template>

<style lang="scss" scoped>
  @import "@/styles/_variables.scss";

  .title-box {
    display: block;
    position: fixed;
    top: 0;

    margin: 75px 0;
    padding: 15px 0;

    background-color: rgba(0, 0, 0, 0.33);
    width: 100vw;

    font-size: 24pt;
    font-weight: 800;
    color: $primary-text-color;
    text-align: center;

    @media screen and (min-width: $desktop-breakpoint) {
      padding-left: 10vw;
      text-align: left;
    }
  }

  .title-box strong {
    color: $secondary-text-color;
  }
</style>

<script>
  export default {
  };
</script>
