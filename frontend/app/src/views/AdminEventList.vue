<template>
  <article class="AdminEventList">
    <the-title class="AdminEventList-Title">Listar Eventos</the-title>

    <div class="AdminEventList-TableWrapper">
      <data-table
        :rows="events"
        :headers="headers"
        class="AdminEventList-Table"
        @click="showEventDetail"
      />
    </div>
  </article>
</template>

<style lang="scss" scoped>
  .AdminEventList {
    &-TableWrapper {
      width: 100%;
      padding: 10px;
      box-sizing: border-box;
    }

    &-Table {
      width: 100%;
    }
  }
</style>

<script>
  import { mapGetters } from "vuex";
  import { FETCH_EVENTS } from "@/store/actions.type";
  import { RequireAdminMixin } from "@/common/mixins";
  import DataTable from "@/components/DataTable";
  import TheTitle from "@/components/TheTitle";

  export default {
    name: "AdminEventList",

    components: {
      DataTable,
      TheTitle,
    },

    mixins: [RequireAdminMixin],

    data() {
      return {
        headers: [
          {
            title: "Título",
            field: "title",
            isLink: true,
            displayCallback: (value) => {
              return value;
            },
          },
          {
            title: "Tipo",
            field: "event_type",
            isLink: false,
            displayCallback: this.displayEventType,
          },
        ],
      };
    },

    computed: {
      ...mapGetters(["events", "currentUser", "isAuthenticated"]),
    },

    beforeMount() {
      this.$store.dispatch(FETCH_EVENTS);
    },

    mounted() {
      if (
        !this.isAuthenticated ||
        this.currentUser === null ||
        typeof this.currentUser === "undefined" ||
        !this.currentUser.is_admin
      ) {
        this.$router.push({ name: "home" });
      }
    },

    methods: {
      handleError(msg) {
        this.$emit("alert", { text: msg, style: "error", expSecs: 10 });
      },

      handleSuccess(msg) {
        this.$emit("alert", { text: msg, style: "success", expSecs: 10 });
      },

      displayEventType(value) {
        if (value === "SELECTION_PROCESS") {
          return "Processo Seletivo";
        } else if (value === "PUBLIC_TENDER") {
          return "Concurso Público";
        }

        return "Desconhecido";
      },

      showEventDetail(eventId) {
        this.$router
          .push({ path: `/administrador/editar-evento/${eventId}` })
          .catch(() => {});
      },
    },
  };
</script>
