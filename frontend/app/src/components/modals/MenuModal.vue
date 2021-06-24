<template>
  <the-modal
    :visible="visible"
    class="MenuModal"
    title="Menu"
    @close="$emit('close')"
  >
    <div class="MenuModal-Profile">
      <div
        v-if="!isAuthenticated"
        class="MenuModal-ProfileWrapper"
      >
        <div class="MenuModal-ProfileName">
          Olá, Visitante
        </div>
        <ul class="MenuModal-ProfileActionsList">
          <li class="MenuModal-ProfileActionsItem">
            <a
              class="MenuModal-ProfileActionsLink"
              href="#"
              @click="openLogin()"
            >
              Entrar
            </a>
          </li>
          <li class="MenuModal-ProfileActionsItem">
            <a
              class="MenuModal-ProfileActionsLink"
              href="#"
              @click="openRegister"
            >
              Registrar
            </a>
          </li>
        </ul>
      </div>

      <div
        v-else
        class="MenuModal-ProfileWrapper"
      >
        <div class="MenuModal-ProfileName">
          <router-link
            :to="{
              name: 'profile',
              params: { username: 'currentUser.username' },
            }"
            class="MenuModal-ProfileActionsLink"
            active-class="MenuModal-ProfileActionsLink--active"
            exact
          >
            Olá, {{ currentUser ? currentUser.name : "An&ocirc;nimo" }}
          </router-link>
        </div>
        <ul class="MenuModal-ProfileActionsList">
          <li class="MenuModal-ProfileActionsItem">
            <a
              href="#"
              title="Clique para ir ao seu perfil e editar seus dados pessoais"
              class="MenuModal-ProfileActionsLink"
              @click="openProfile"
            >
              <span>Meus Perfil</span>
            </a>
          </li>
          <li class="MenuModal-ProfileActionsItem">
            <a
              href="#"
              title="Clique para sair da sua conta"
              class="MenuModal-ProfileActionsLink"
              @click="logoutClick"
            >Sair</a>
          </li>
        </ul>
      </div>
    </div>

    <nav class="MenuModal-MenuWrapper">
      <menu-list
        :items="menuItems"
        color-scheme="dark"
        @link-opened="linkOpened"
      />
    </nav>
  </the-modal>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .MenuModal {
    padding: 0;

    &-Profile {
      width: 100%;
      box-sizing: border-box;
      padding: 10px;
      background-color: $color-secondary-background-light;
    }

    &-ProfileWrapper {
      display: flex;
      margin-left: auto;
      padding-right: 10px;

      flex-direction: column;
      flex-wrap: wrap;
      align-content: flex-start;
      justify-content: center;
    }

    &-ProfileName {
      flex: 0 0 auto;
      font-size: 14px;
      font-weight: bold;
    }

    &-ProfileActionsList {
      flex: 0 0 auto;
      list-style-type: none;
      margin: 0;
      padding: 0;
      display: flex;
    }

    &-ProfileActionsItem {
      font-size: 12px;
      flex: 0 1 auto;
    }

    &-ProfileActionsItem + &-ProfileActionsItem:before {
      padding: 0 5px;
      color: $color-primary-border;
      content: "|";
    }

    &-MenuWrapper {
      font-size: 18pt;
      margin: 25px 50px;
      line-height: 40px;
    }
  }
</style>

<script>
  import { mapGetters } from "vuex";
  import { LOGOUT } from "@/store/actions.type";
  import { MENU_ADMIN, MENU_ALL } from "@/common/menus";
  import MenuList from "@/components/MenuList";
  import TheModal from "@/components/modals/TheModal";

  export default {
    components: {
      MenuList,
      TheModal,
    },

    props: {
      visible: {
        type: Boolean,
        default: false,
      },
    },

    data() {
      return {
        menuItems: MENU_ALL,
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
          return [...MENU_ALL, ...MENU_ADMIN];
        }

        return MENU_ALL;
      },

      linkOpened() {
        this.$emit("close");
      },

      openLogin() {
        this.$emit("show-login");
        this.$emit("close");
      },

      openRegister() {
        this.$emit("show-register");
        this.$emit("close");
      },

      openProfile() {
        this.$router.push({ name: "profile" }).catch(() => {});
        this.$emit("close");
      },

      logoutClick(event) {
        event.preventDefault();

        this.$store.dispatch(LOGOUT);
        this.$router.push({ name: "home" }).catch(() => {});
        this.$emit("close");
      },
    },
  };
</script>
