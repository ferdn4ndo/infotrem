<template>
  <the-modal
    :title="title"
    :visible="visible"
    class="EventLinkModal"
    @close="$emit('close')"
  >
    <toast-messages ref="EventLinkModalToastMessages" />

    <admin-event-link-form
      :event="event"
      :link="eventLink"
      :redirect-after-save="false"
      class="EventLinkModal-Form"
      ref="eventLinkForm"
      @error="handleError"
      @success="handleSuccess"
    />
  </the-modal>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .EventLinkModal {
    &-Form {
      margin: 10px 20px 0;
    }
  }
</style>

<script>
  import { mapGetters } from "vuex";
  import TheModal from "@/components/modals/TheModal";
  import AdminEventFileForm from "@/components/forms/AdminEventFileForm";
  import AdminEventLinkForm from "@/components/forms/AdminEventLinkForm";
  import ToastMessages from "@/components/ToastMessages";

  export default {
    name: "EventLinkModal",

    components: {
      ToastMessages,
      AdminEventLinkForm,
      AdminEventFileForm,
      TheModal,
    },

    props: {
      event: {
        type: Object,
        required: true,
      },

      linkId: {
        type: String,
        required: true,
      },

      visible: {
        type: Boolean,
        default: false,
      },
    },

    data() {
      return {
        eventLink: {},
      };
    },

    computed: {
      ...mapGetters(["currentUser", "isAuthenticated"]),

      title() {
        return this.linkId !== "" ? "Editar Link" : "Cadastrar Link";
      },
    },

    watch: {
      visible(value) {
        if (value) {
          this.reset();
        }
      },

      linkId() {
        this.reset();
      },
    },

    mounted() {
      if (
        typeof this.currentUser === "undefined"
        || typeof this.isAuthenticated === "undefined"
        || this.currentUser === null
        || !this.currentUser.is_admin
        || !this.isAuthenticated
      ) {
        console.log("Event file upload requires admin-level authentication.");
        this.$emit("close");
      }

      this.reset();
    },

    methods: {
      handleError(msg) {
        let toasts = this.$refs.EventLinkModalToastMessages;
        toasts.addMessage(msg, "error", "error", 10);
      },

      handleSuccess(msg) {
        this.$emit("alert", { text: msg, style: "success", expSecs: 10 });
        this.$emit("close");
      },

      reset() {
        if (!this.linkId) {
          this.eventLink = {};
          this.$refs.eventLinkForm.$refs.adminEventLinkForm.clear();
          return;
        }

        if (this.event && 'links' in this.event) {
          const filteredLinks = this.event.links.filter((link) => link.id === this.linkId);

          if (filteredLinks.length === 0) {
            console.log("The informed link ID wasn't found in the event links.");
            this.$emit("close");
          }

          this.eventLink = filteredLinks[0];
        }

        this.$refs.eventLinkForm.$refs.adminEventLinkForm.reset();
        this.$refs.eventLinkForm.$refs.adminEventLinkForm.validate();
      },
    },
  };
</script>
