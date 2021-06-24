<template>
  <div
    :class="{ 'TheModal-Invisible': !visible }"
    class="TheModal"
    @keyup="keyMonitor"
  >
    <article 
      :class="{ 'TheModal-Inner--small': small }" 
      class="TheModal-Inner"
    >
      <header class="TheModal-Header">
        <div 
          v-if="showTitle" 
          class="TheModal-TitleWrapper"
        >
          <h1 class="TheModal-Title">{{ title }}</h1>
        </div>

        <div 
          v-if="allowClose" 
          class="TheModal-CloseButtonWrapper"
        >
          <a
            class="TheModal-CloseButtonLink"
            href="#"
            title="Fechar"
            @click="clickToClose"
          >
            &times;
          </a>
        </div>
      </header>

      <section
        :class="{ 'TheModal-Content--small': small }"
        class="TheModal-Content"
      >
        <slot />
      </section>
    </article>
  </div>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .TheModal {
    position: fixed;
    z-index: 9999;
    top: 0;
    left: 0;
    height: 100vh;
    width: 100vw;
    background-color: $color-background-transparent;

    @media screen and (min-width: $desktop-breakpoint - 1) {
    }

    &-Inner {
      position: fixed;
      z-index: 9999;
      background-color: $color-background-white;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;

      @media screen and (min-width: $tablet-breakpoint - 1) {
        top: 50%;
        left: 50%;
        width: 80vw;
        border-radius: 10px;
        transform: translate(-50%, -50%);
        max-height: 90vh;
        height: auto;
      }

      @media screen and (min-width: $desktop-breakpoint - 1) {
        max-width: $desktop-breakpoint;
      }

      &--small {
        @media screen and (min-width: $tablet-breakpoint - 1) {
          max-width: 500px;
        }
      }
    }

    &-Content {
      position: relative;
      max-height: 85vh;
      overflow-y: auto;
      overflow-x: hidden;
      box-sizing: border-box;
      margin-bottom: 20px;
      scrollbar-color: $color-background-border rgba(0, 0, 0, 0);

      @media screen and (min-width: $tablet-breakpoint - 1) {
        max-height: 66vh;
      }

      @media screen and (min-width: $desktop-breakpoint - 1) {
        max-width: $desktop-breakpoint;
      }

      &--small {
        @media screen and (min-width: $desktop-breakpoint - 1) {
          max-width: 500px;
        }
      }
    }

    &-Invisible {
      display: none;
    }

    &-Header {
      display: flex;
      align-items: center;
      border-bottom: 1px solid $color-background-border;
    }

    &-TitleWrapper {
      flex: 1 1 auto;
    }

    &-Title {
      margin: 10px 20px;
      cursor: default;
      font-size: 16pt;
    }

    &-CloseButtonWrapper {
      flex: 0 0 auto;
      justify-self: flex-end;
      margin-right: 10px;
    }

    &-CloseButtonLink {
      font-size: 36px;
      padding: 5px;
    }

    &-CloseButtonLink:hover {
      text-decoration: none;
    }
  }
</style>

<script>
  import { OPEN_MODAL } from "@/store/actions.type";

  export default {

    props: {
      allowClose: {
        type: Boolean,
        default: true,
      },

      title: {
        type: String,
        default: "",
      },

      visible: {
        type: Boolean,
        default: false,
      },

      small: {
        type: Boolean,
        default: false,
      },
    },

    data: () => {
      return {
        keyListener: null,
      };
    },
    computed: {
      showTitle() {
        return this.title !== "";
      },
    },

    watch: {
      visible(value) {
        this.$store.dispatch(OPEN_MODAL, value);

        if (value) {
          document.body.classList.add("modal-opened");
          this.addKeyListener();
        } else {
          document.body.classList.remove("modal-opened");
          this.removeKeyListener();
        }
      },
    },

    beforeDestroy() {
      this.removeKeyListener();
    },

    methods: {
      clickToClose(event) {
        this.$emit("close");
        event.preventDefault();
      },

      keyMonitor(event) {
        if (event.key === "Escape" && this.allowClose) {
          this.$emit("close");
        }
      },

      addKeyListener() {
        if (this.keyListener !== null) {
          return;
        }

        this.keyListener = document.addEventListener("keyup", this.keyMonitor);
      },

      removeKeyListener() {
        if (this.keyListener !== null) {
          document.removeEventListener("keyup", this.keyMonitor);
          this.keyListener = null;
        }
      },
    },
  };
</script>
