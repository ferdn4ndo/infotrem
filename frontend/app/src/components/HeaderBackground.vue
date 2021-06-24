<template>
  <header
    :style="{ 'background-image': `url(${imageSrc})`, 'height': height + 'px' }"
    class="HeaderBackground"
  >
    <div class="HeaderBackground-TitleWrapper">
      <h1 class="HeaderBackground-Title">{{ title }}</h1>
    </div>
  </header>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .HeaderBackground {
    width: 100%;
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
    overflow: hidden;

    &-TitleWrapper {
      background-color: rgba(0, 0, 0, 0.25);
      width: 100%;
      height: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
    }

    &-Title {
      width: 100%;
      margin: 10px 0;
      padding: 10px 10%;
      box-sizing: border-box;
      background-color: $background-dark-transparent;
      text-align: center;
      font-size: 24pt;
      color: $color-primary-foreground;
    }
  }
</style>

<script>
  export default {
    props: {
      imageSrc: {
        type: String,
        default: "img/backgrounds/9.jpg",
      },

      height: {
        type: Number,
        default: 200,
      },

      title: {
        type: String,
        default: "",
      },
    },
  };
</script>
