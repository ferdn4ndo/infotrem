<template>
  <the-modal
    :visible="visible"
    class="EventFileUploadModal"
    title="Enviar Arquivo(s)"
    @close="$emit('close')"
  >
    <p class="EventFileUploadModal-Paragraph">
      Utilize a seção abaixo para fazer o envio de novos arquivos para o evento
      {{ event.name }}.
    </p>

    <file-upload
      class="EventFileUploadModal-FileUpload"
      ref="fileUpload"
      :event="event"
      @fileUploaded="fileUploaded"
      @close="$emit('close')"
    />
  </the-modal>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .EventFileUploadModal {
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
  import FileUpload from "@/components/FileUpload";

  export default {
    name: "EventFileUploadModal",

    components: {
      FileUpload,
      TheModal,
    },

    props: {
      event: {
        type: Object,
        required: true,
      },

      visible: {
        type: Boolean,
        default: false,
      },
    },

    data() {
      return {
        filesUploaded: [],
      };
    },

    computed: {
      ...mapGetters(["currentUser", "isAuthenticated"]),

      title() {
        switch (this.currentState) {
          case "check":
            return "Pré-inscrição";
          case "confirm":
            return "Confirmação dos dados";
          case "payment":
            return "Pagamento";
          default:
            return "Erro";
        }
      },
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
      fileUploaded(file) {
        console.log('File Uploaded: ', file);
        this.filesUploaded.push(file);
      },

      reset() {
        this.filesUploaded = [];
        this.$refs.fileUpload.reset();
      },
    },
  };
</script>
