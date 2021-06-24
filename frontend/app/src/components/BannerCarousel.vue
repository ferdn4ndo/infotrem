<template>
  <article
    :style="{
      'background-image': `url(${imageSrc})`,
    }"
    class="BannerCarousel"
  >
    <transition
      name="slide-fade"
      mode="out-in"
    >
      <header
        :key="text"
        class="BannerCarousel-text"
      >
        {{ text }}
      </header>
    </transition>
  </article>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  $background-transition-time: 400ms;

  .BannerCarousel {
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;

    -webkit-transition: background $background-transition-time linear;
    -moz-transition: background $background-transition-time linear;
    -o-transition: background $background-transition-time linear;
    -ms-transition: background $background-transition-time linear;
    transition: background $background-transition-time linear;

    height: 100%;
    width: 100%;

    display: flex;
    justify-content: center;
    align-items: center;

    &-text {
      margin: 20px;
      padding: 20px;
      max-width: 90vw;
      box-sizing: border-box;
      background-color: rgba(0, 0, 0, 0.8);
      color: $color-primary-foreground;

      -webkit-transition: content $background-transition-time linear;
      -moz-transition: content $background-transition-time linear;
      -o-transition: content $background-transition-time linear;
      -ms-transition: content $background-transition-time linear;
      transition: content $background-transition-time linear;

      @media screen and (min-width: $desktop-breakpoint - 1) {
        max-width: 800px;
      }
    }
  }

  .BannerCarousel::before {
    content: "";
    background: rgba(0, 0, 0, 0.1) no-repeat center;
    background-size: inherit;
    opacity: 0;
    transition: opacity 0.3s ease-in-out;
  }

  .slide-fade-enter-active {
    transition: all 0.3s ease;
  }

  .slide-fade-leave-active {
    transition: all #{$background-transition-time * 1.5} cubic-bezier(1, 0.5, 0.8, 1);
  }

  .slide-fade-enter,
  .slide-fade-leave-to {
    transform: translateX(10px);
    opacity: 0;
  }
</style>

<script>
  export default {

    props: {
      slides: {
        type: Array,
        required: true,
      },

      interval: {
        type: Number,
        default: 5000,
      },
    },

    data() {
      return {
        loaded: false,
        imageSrc: "",
        slideIndex: 0,
        text: "",
        timer: null,
      };
    },

    watch: {
      slides: function() {
        this.updateData();
      },
    },
    created() {
      this.updateData();
      this.timer = setInterval(this.nextSlide, this.interval);
    },

    mounted: function() {
      this.loaded = false;
      let imagesSrc = this.slides.map((slide) => slide.imageSrc);
      this.$nextTick(function() {
        this.$images.preload(imagesSrc, (completed, progress) => {
          console.log(`Loading image... (${Math.round(progress * 100)}%)`);
          if (completed) {
            this.loaded = true;
          }
        });
      });
    },

    methods: {
      nextSlide() {
        this.slideIndex++;

        if (this.slideIndex >= this.slides.length) {
          this.slideIndex = 0;
        }

        this.updateData();
      },

      updateData() {
        if (this.slides.length > 0) {
          this.text = this.slides[this.slideIndex].text;
          this.imageSrc = this.slides[this.slideIndex].imageSrc;
        } else {
          this.text = "Carregando...";
          this.imageSrc = "";
        }
      },
    },
  };
</script>
