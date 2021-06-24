<template>
  <article class="AdminEventCreate">
    <the-title class="Company-Title">Criar Novo Evento</the-title>

    <admin-event-form
      class="AdminEventCreate-Form"
      @error="handleError"
      @success="handleSuccess"
    />
  </article>
</template>

<style lang="scss" scoped>
  .AdminEventCreate {
    &-Form {
      box-sizing: border-box;
      margin: 10px;
    }
  }
</style>

<script>
  import { mapGetters } from "vuex";
  import { RequireAdminMixin } from "@/common/mixins";
  import AdminEventForm from "@/components/forms/AdminEventForm";
  import TheTitle from "@/components/TheTitle";

  export default {
    name: "AdminEventCreate",

    components: {
      AdminEventForm,
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
      handleError(msg) {
        this.$emit("alert", { text: msg, style: "error", expSecs: 10 });
      },

      handleSuccess(msg) {
        this.$emit("alert", { text: msg, style: "success", expSecs: 10 });
      },
    },
  };
</script>
