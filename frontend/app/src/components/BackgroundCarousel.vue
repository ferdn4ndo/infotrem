<template>
  <div
    class="background-carousel"
    :style="{
      'background-image': `url(${imageSrc})`,
    }"
  >
    <slot>

    </slot>
  </div>
</template>

<style lang="scss" scoped>
  @import "@/styles/_variables.scss";

  .background-carousel {
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;

    -webkit-transition: background $background-transition-time linear;
    -moz-transition: background $background-transition-time linear;
    -o-transition: background $background-transition-time linear;
    -ms-transition: background $background-transition-time linear;
    transition: background $background-transition-time linear;

    position: fixed;
    height: 100vh;
    width: 100vw;
    top: 0;
    left: 0;
  }

  .background-carousel::before {
    content: '';
    position: absolute;
    left: 0;
    top: 0;
    right:0;
    bottom: 0;
    background: rgba(0,0,0,0.1) no-repeat center;
    background-size: inherit;
    opacity: 0;
    transition: opacity 0.3s ease-in-out;
  }
</style>

<script>
  import PHOTOS_LIST from "../common/photos";

  export default {
    computed: {
      background_image_src() {
        return 'img/backgrounds/1.jpg';
      }
    },
    created() {
      this.timer = setInterval(this.nextImage, 3000);
    },
    data() {
      return {
        timer: null,
        imageIndex: 0,
        imageOpacity: 1,
        imageSrc: 'img/backgrounds/1.jpg',
      };
    },
    methods: {
      getRandomIndex() {
        let max = PHOTOS_LIST.length;
        let min = 0;
        return parseInt(Math.random() * (max - min) + min);
      },

      nextImage() {
        let newIndex = this.getRandomIndex();

        let newImageSrc = PHOTOS_LIST[newIndex];
        const img = new Image();
        img.src = newImageSrc;

        img.onload = () => {
          this.imageSrc = newImageSrc;
        }
      },
    }
  };
</script>
