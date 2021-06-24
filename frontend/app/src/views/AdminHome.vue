<template>
  <article class="AdminHome">
    <the-title class="AdminHome-Title">Portal de Administração</the-title>

    <p class="AdminHome-Paragraph">
      Bem-vindo ao portal de administração. Selecione uma das opções abaixo para
      continuar.
    </p>

    <div class="AdminHome-Toolbar">
      <the-button
        class="AdminHome-ToolbarButton"
        @click="openEventCreate()"
      >
        <the-icon
          class="AdminHome-ToolbarIcon"
          icon="calendar_plus"
        />
        Criar Novo Evento
      </the-button>

      <the-button
        class="AdminHome-ToolbarButton"
        @click="openEventList()"
      >
        <the-icon
          class="AdminHome-ToolbarIcon"
          icon="calendar"
        />
        Listar Eventos Existentes
      </the-button>

      <the-button
        class="AdminHome-ToolbarButton"
        @click="openUserCreate()"
      >
        <the-icon
          class="AdminHome-ToolbarIcon"
          icon="user_plus"
        />
        Criar Novo Usuário
      </the-button>

      <the-button
        class="AdminHome-ToolbarButton"
        @click="openUserList()"
      >
        <the-icon
          class="AdminHome-ToolbarIcon"
          icon="users"
        />
        Listar Usuários Existentes
      </the-button>
    </div>
  </article>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .AdminHome {
    width: 100%;

    &-Title {
      margin: 15px 20px;
    }

    &-Paragraph {
      margin: 15px 30px;
    }

    &-Toolbar {
      display: flex;
      flex-direction: row;
      flex-wrap: wrap;
      padding: 20px;
    }

    &-ToolbarButton {
      flex: 1 1 100%;
      margin: 10px;
      text-align: center;
      box-sizing: border-box;

      @media screen and (min-width: $tablet-breakpoint - 1) {
        flex: 1 1 45%;
      }
    }

    &-ToolbarIcon {
      display: block;
      margin: 10px;
      font-size: 22pt;
    }
  }
</style>

<script>
  import { mapGetters } from "vuex";
  import TheTitle from "@/components/TheTitle";
  import TheButton from "@/components/TheButton";
  import TheIcon from "@/components/TheIcon";
  import { RequireAdminMixin } from "@/common/mixins";

  export default {
    name: "CscServices",

    components: {
      TheIcon,
      TheButton,
      TheTitle,
    },

    mixins: [RequireAdminMixin],

    data() {
      return {};
    },

    computed: {
      ...mapGetters(["currentUser", "isAuthenticated"]),
    },

    methods: {
      openEventCreate() {
        this.$router.push({ name: "admin-event-create" });
      },

      openEventList() {
        this.$router.push({ name: "admin-event-list" });
      },

      openUserCreate() {
        this.$router.push({ name: "home" });
      },

      openUserList() {
        this.$router.push({ name: "home" });
      },
    },
  };
</script>
