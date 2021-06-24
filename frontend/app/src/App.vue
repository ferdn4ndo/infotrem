<template>
  <div
    id="app"
    class="CscSite"
  >
    <div
      v-if="isLoading"
      class="CscSite-LoaderOverlay"
    >
      <loader-ellipsis/>
    </div>

    <the-header
      class="CscSite-Header"
      @show-login="openAuthModalLogin"
      @show-register="openAuthModalRegister"
      @show-menu="openMenuModal"
    />

    <toast-messages
      ref="CscToastMessages"
      class="CscSite-ToastMessages"
    />

    <section class="CscSite-Content">
      <router-view
        @alert="addToastMessage"
        @show-login="openAuthModalLogin"
      />
    </section>

    <the-footer class="CscSite-Footer" />

    <auth-modal
      :initial-state="initialAuthState"
      :visible="displayAuthModal"
      @close="closeAuthModal"
      @alert="addToastMessage"
    />

    <menu-modal
      :visible="displayMenuModal"
      @close="closeMenuModal"
      @show-login="openAuthModalLogin"
      @show-register="openAuthModalRegister"
    />
  </div>
</template>

<script>
  import { mapGetters } from "vuex";
  import TheHeader from "@/components/TheHeader";
  import TheFooter from "@/components/TheFooter";
  import LoaderEllipsis from "@/components/LoaderEllipsis";
  import AuthModal from "@/components/modals/AuthModal";
  import MenuModal from "@/components/modals/MenuModal";
  import ToastMessages from "@/components/ToastMessages";
  import { FETCH_USER } from "@/store/actions.type";

  export default {
    name: "App",

    components: {
      AuthModal,
      MenuModal,
      LoaderEllipsis,
      TheHeader,
      TheFooter,
      ToastMessages,
    },

    data: () => ({
      displayAuthModal: false,
      displayMenuModal: false,
      initialAuthState: "login",
    }),

    computed: {
      ...mapGetters(["isLoading", "isAuthenticated", "hasOpenModal"]),
    },

    watch: {
      isAuthenticated(value) {
        if (value) {
          this.$store.dispatch(FETCH_USER);
        }
      },
    },

    methods: {
      addToastMessage(message) {
        let text = message.text !== undefined ? message.text : "";
        let style = message.style !== undefined ? message.style : "info";
        let icon = message.icon !== undefined ? message.icon : "auto";
        let expSecs = message.expSecs !== undefined ? message.expSecs : 5;
        let closeable =
          message.closeable !== undefined ? message.closeable : true;

        let toasts = this.$refs.CscToastMessages;
        toasts.addMessage(text, style, icon, expSecs, closeable);
      },

      closeAuthModal() {
        this.displayAuthModal = false;
      },

      closeMenuModal() {
        this.displayMenuModal = false;
      },

      openAuthModalLogin() {
        this.initialAuthState = "login";
        this.displayAuthModal = true;
      },

      openAuthModalRegister() {
        this.initialAuthState = "register";
        this.displayAuthModal = true;
      },

      openMenuModal() {
        this.displayMenuModal = true;
      },
    },
  };
</script>

<style lang="scss">
  //@import url("https://fonts.googleapis.com/css?family=Caveat+Brush|Play");
  //@import url("https://fonts.googleapis.com/css?family=Alata&display=swap");
  //@import url("https://fonts.googleapis.com/css2?family=Noto+Sans&display=swap");
  @import url("https://fonts.googleapis.com/css2?family=Poppins&display=swap");
  @import "~@/styles/_variables.scss";

  body {
    //font-family: "Play", sans-serif;
    //font-family: "Alata", sans-serif;
    //font-family: "Noto Sans", sans-serif;
    font-family: "Poppins", sans-serif;
    margin: 0;
  }

  .modal-opened {
    overflow: hidden;
  }

  a {
    text-decoration: none;
    color: $primary-text-color;
    cursor: pointer;
  }

  a:hover {
    text-decoration: underline;
  }

  a:active {
    color: $color-text-black-highlight;
  }

  a:visited {
    text-decoration: none;
    color: $primary-text-color;
  }
</style>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .CscSite {
    min-height: 100vh;
    background-color: $color-background-gray;
    display: flex;
    flex-direction: column;

    &-LoaderOverlay {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      z-index: 999999;
      background-color: rgba(0, 0, 0, 0.85);
      display: flex;
      justify-content: center;
      align-items: center;
    }

    &-Content {
      flex: 1 0 100%;
      height: 100%;
      background-color: $color-background-white;
      margin: 0 auto;
      width: 100%;

      @media screen and (min-width: $max-content-width - 1) {
        max-width: $max-content-width;
        border-left: 1px solid $color-background-border;
        border-right: 1px solid $color-background-border;
      }
    }

    &-ToastMessages {
      position: sticky;
      top: 65px;
      margin: 0 auto;

      @media screen and (min-width: $desktop-breakpoint - 1) {
        max-width: $max-content-width;
      }
    }

    &-Header {
      position: sticky;
      top: 0;
    }

    &-Footer {
      box-sizing: border-box;
    }
  }
</style>
