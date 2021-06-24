<template>
  <article class="AdminEventDetail">
    <admin-event-toolbar
      :event="event"
      class="AdminEventDetail-Toolbar"
    />

    <the-title
      class="AdminEventDetail-Title"
    >Informações do Evento '{{ event.title }}'</the-title>

    <admin-event-form
      :event="event"
      :redirect-after-save="false"
      class="AdminEventDetail-Form"
      @error="handleError"
      @success="handleSuccess"
    />
  </article>
</template>

<style lang="scss" scoped>
  .AdminEventDetail {
    &-Toolbar {
      padding: 10px 10px 0 10px;
    }

    &-Form {
      box-sizing: border-box;
      margin: 10px;
    }
  }
</style>

<script>
  import { mapGetters } from "vuex";
  import { FETCH_EVENT } from "@/store/actions.type";
  import { DefaultErrorMessage } from "@/common/messages";
  import { RequireAdminMixin } from "@/common/mixins";
  import AdminEventForm from "@/components/forms/AdminEventForm";
  import TheTitle from "@/components/TheTitle";
  import AdminEventToolbar from "@/components/AdminEventToolbar";

  export default {
    name: "AdminEventDetail",

    components: {
      AdminEventToolbar,
      AdminEventForm,
      TheTitle,
    },

    mixins: [RequireAdminMixin],

    data() {
      return {
        event: {},
      };
    },

    computed: {
      ...mapGetters(["events", "currentUser", "isAuthenticated"]),
    },

    beforeMount() {
      this.$store
        .dispatch(FETCH_EVENT, this.$route.params.event_id)
        .then((event) => {
          this.event = event;
          this.hadSuccess = true;
        })
        .catch((error) => {
          if (error.response) {
            this.$emit("alert", DefaultErrorMessage);
            this.$router.push({ name: "admin-event-list" });
            // ToDo: save to a log here
          }
        });
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
