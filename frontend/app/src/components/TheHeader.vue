<template>
  <header class="TheHeader">
    <div class="TheHeader-ContentWrapper">
      <router-link
        :to="{ name: 'home' }"
        class="TheHeader-LogoWrapper"
        exact
      >
        <img
          class="TheHeader-Logo"
          src="/img/logo_novo.png"
          alt="Logo da CSC Consultoria (contém um logotipo desenhado com as letras C, S e C)"
        >
      </router-link>

      <nav class="TheHeader-MenuWrapper">
        <menu-list
          :items="menuItems"
          :inline="true"
        />
      </nav>

      <div class="TheHeader-ProfileWrapper">
        <profile-card
          class="TheHeader-ProfileCard"
          @show-register="showRegister"
          @show-login="showLogin"
        />
      </div>

      <div class="TheHeader-MenuButtonWrapper">
        <the-button @click="openMenu()">
          <the-icon
            class="TheHeader-MenuButtonIcon"
            icon="menu"
          />
        </the-button>
      </div>
    </div>
  </header>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .TheHeader {
    width: 100%;
    background-color: $background-dark-color;
    border-bottom: 1px solid $background-dark-border;
    z-index: 1000;
    color: $foreground-light-color;

    @media screen and (min-width: $desktop-breakpoint - 1) {
      flex-wrap: nowrap;
    }

    &-ContentWrapper {
      max-width: $max-content-width;
      display: flex;
      flex-wrap: wrap;
      margin: 0 auto;
    }

    &-LogoWrapper {
      flex: 0 0 auto;
      order: 1;
      height: 60px;
      display: flex;
      flex-direction: column;
      flex-wrap: wrap;
      align-content: flex-start;
      justify-content: center;
      padding-left: 10px;

      text-decoration: none;
      border: none;
      color: $foreground-dark-color;

      &:hover {
        text-decoration: none;
      }
    }

    &-Logo {
      flex: 0 0 32px;
      height: 32px;
      width: auto;
    }

    &-MenuButtonIcon {
      padding: 0 5px;
    }

    &-ProfileWrapper {
      flex: 0 0 auto;
      box-sizing: border-box;
      order: 2;
      display: flex;
      margin-left: auto;
      padding-right: 10px;
      height: 60px;

      flex-direction: column;
      flex-wrap: wrap;
      align-items: flex-end;
      justify-content: center;
    }

    &-MenuButtonWrapper {
      justify-self: end;
      flex: 0 0 auto;
      order: 3;
      padding: 8px 10px 0 0;

      @media screen and (min-width: $desktop-breakpoint - 1) {
        display: none;
      }
    }

    &-MenuWrapper {
      flex: 0 0 100%;
      justify-self: end;
      order: 4;
      justify-content: center;
      align-items: center;
      padding: 10px;
      box-sizing: border-box;
      font-size: 14px;
      display: none;
      color: $foreground-light-color;

      @media screen and (min-width: $desktop-breakpoint - 1) {
        display: flex;
        flex: 1 1 auto;
        order: 2;
      }
    }
  }
</style>

<script>
  import { mapGetters } from "vuex";
  import { LOGOUT } from "@/store/actions.type";
  import { MENU_ADMIN, MENU_HEADER } from "@/common/menus";
  import TheButton from "@/components/TheButton";
  import MenuList from "@/components/MenuList";
  import TheIcon from "@/components/TheIcon";
  import ProfileCard from "@/components/ProfileCard";

  export default {
    components: {
      ProfileCard,
      TheIcon,
      MenuList,
      TheButton,
    },

    data() {
      return {
        isLogged: false,
        menuItems: MENU_HEADER,
      };
    },

    computed: {
      ...mapGetters(["currentUser", "isAuthenticated"]),
    },

    watch: {
      currentUser() {
        this.menuItems = this.getMenuItems();
      },
    },

    methods: {
      getMenuItems() {
        if (
          this.currentUser !== null &&
          typeof this.currentUser !== "undefined" &&
          this.currentUser.is_admin
        ) {
          return [...MENU_HEADER, ...MENU_ADMIN];
        }

        return MENU_HEADER;
      },

      openMenu() {
        this.$emit("show-menu");
      },

      showRegister() {
        this.$emit("show-register");
      },

      showLogin() {
        this.$emit("show-login");
      },

      logoutClick(event) {
        event.preventDefault();

        this.$store.dispatch(LOGOUT);
        this.$router.push({ name: "home" }).catch(() => {});
      },

      profileLinkOpened(linkName) {
        if (linkName === "login") {
          this.$emit("show-login");
        } else if (linkName === "register") {
          this.$emit("show-register");
        } else if (linkName === "logout") {
          this.$store.dispatch(LOGOUT);
          this.$router.push({ name: "home" }).catch(() => {});
        }
      },

      getUserDisplayName() {
        if (
          this.currentUser === null ||
          this.currentUser === undefined ||
          this.currentUser.name === undefined
        ) {
          return "Anônimo";
        }

        return this.currentUser.name.split(" ")[0];
      },
    },
  };
</script>
