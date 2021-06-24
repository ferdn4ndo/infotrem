<template>
  <the-modal
    :visible="visible"
    class="EventFileEditModal"
    title="Editar Arquivo"
    @close="$emit('close')"
  >
    <admin-event-file-form
      :event="event"
      :file="eventFile"
      :redirect-after-save="false"
      class="EventFileEditModal-Form"
      ref="eventFileEditForm"
      @error="handleError"
      @success="handleSuccess"
    />
  </the-modal>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .EventFileEditModal {
    &-Paragraph {
      cursor: default;
      text-align: justify;
      margin: 10px;

      &--bold {
        font-weight: bold;
      }
    }
  }
</style>

<script>
  import { mapGetters } from "vuex";
  import TheModal from "@/components/modals/TheModal";
  import AdminEventFileForm from "@/components/forms/AdminEventFileForm";

  export default {
    name: "EventFileEditModal",

    components: {
      AdminEventFileForm,
      TheModal,
    },

    props: {
      event: {
        type: Object,
        required: true,
      },

      fileUuid: {
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
        eventFile: {},
      };
    },

    computed: {
      ...mapGetters(["currentUser", "isAuthenticated"]),
    },

    watch: {
      visible(value) {
        if (value) {
          this.reset();
        }
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
        this.$emit("alert", { text: msg, style: "error", expSecs: 10 });
      },

      handleSuccess(msg) {
        this.$emit("alert", { text: msg, style: "success", expSecs: 10 });
        this.$emit("close");
      },

      reset() {
        if (this.event && 'files' in this.event) {
          const filteredFiles = this.event.files.filter((file) => file.id === this.fileUuid);

          if (filteredFiles.length === 0) {
            console.log("The informed file ID wasn't found in the event files.");
            this.$emit("close");
          }

          this.eventFile = filteredFiles[0];
        }

        this.$refs.eventFileEditForm.$refs.adminEventFileForm.reset();
        this.$refs.eventFileEditForm.$refs.adminEventFileForm.validate();
      },
    },
  };
</script>
