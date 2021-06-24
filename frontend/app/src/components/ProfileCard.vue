<template>
  <div
    v-if="!isAuthenticated"
    class="ProfileCard"
  >
    <div class="ProfileCard-Name">
      Olá, Visitante
    </div>

    <menu-list
      :items="profileMenuItemsNotLogged"
      :inline="true"
      class="ProfileCard-Menu"
      @link-opened="profileLinkOpened"
    />
  </div>

  <div
    v-else
    class="ProfileCard"
  >
    <div class="ProfileCard-Name">Olá, {{ getUserDisplayName() }}</div>

    <menu-list
      :items="profileMenuItemsLogged"
      :inline="true"
      class="ProfileCard-Menu"
      @link-opened="profileLinkOpened"
    />
  </div>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .ProfileCard {
    box-sizing: border-box;
    text-align: right;

    &-Name {
      font-size: 14px;
      font-weight: bold;
    }

    &-Menu {
      font-size: 12px;
    }
  }
</style>

<script>
  import { mapGetters } from "vuex";
  import { LOGOUT } from "@/store/actions.type";
  import { MENU_PROFILE_NOT_LOGGED, MENU_PROFILE_LOGGED } from "@/common/menus";
  import MenuList from "@/components/MenuList";

  export default {
    components: { MenuList },

    data() {
      return {
        profileMenuItemsNotLogged: MENU_PROFILE_NOT_LOGGED,
        profileMenuItemsLogged: MENU_PROFILE_LOGGED,
      };
    },

    computed: {
      ...mapGetters(["currentUser", "isAuthenticated"]),
    },

    methods: {
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
