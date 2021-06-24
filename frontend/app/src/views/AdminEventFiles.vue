<template>
  <article class="AdminEventFiles">
    <admin-event-toolbar
      :event="event"
      class="AdminEventFiles-Toolbar"
    />

    <the-title
      class="AdminEventFiles-Title"
    >Arquivos do Evento '{{ event.title }}'</the-title>

    <div class="AdminEventFiles-TableWrapper">
      <data-table
        :rows="files"
        :headers="headers"
        :allow-removal="true"
        :allow-creation="true"
        class="AdminEventFiles-Table"
        creation-button-text="Enviar"
        @click="showEventFile"
        @create="showFileUploadModal"
        @remove="showRemoveConfirmation"
      />
    </div>

    <event-file-upload-modal
      :event="event"
      :visible="displayUploadModal"
      @close="hideFileUploadModal"
    />

    <event-file-edit-modal
      :event="event"
      :file-uuid="fileUuid"
      :visible="displayEditModal"
      @close="hideFileEditModal"
    />

    <confirmation-modal
      ref="SubscriptionRemoveConfirmationModal"
      :message="removeConfirmationMessage"
      :visible="removeConfirmationVisible"
      @close="hideRemoveConfirmation"
      @confirm="removeFile"
    />
  </article>
</template>

<style lang="scss" scoped>
  .AdminEventFiles {
    &-Toolbar {
      padding: 10px 10px 0 10px;
    }

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
import {FETCH_EVENT, REMOVE_EVENT_FILE} from "@/store/actions.type";
  import { DefaultErrorMessage } from "@/common/messages";
  import { RequireAdminMixin } from "@/common/mixins";
  import AdminEventForm from "@/components/forms/AdminEventForm";
  import DataTable from "@/components/DataTable";
  import TheTitle from "@/components/TheTitle";
  import AdminEventToolbar from "@/components/AdminEventToolbar";
  import EventFileUploadModal from "@/components/modals/EventFileUploadModal";
  import EventFileEditModal from "@/components/modals/EventFileEditModal";
  import ConfirmationModal from "@/components/modals/ConfirmationModal";

  export default {
    name: "AdminEventFiles",

    components: {
      ConfirmationModal,
      EventFileEditModal,
      EventFileUploadModal,
      AdminEventToolbar,
      AdminEventForm,
      DataTable,
      TheTitle,
    },

    mixins: [RequireAdminMixin],

    data() {
      return {
        displayUploadModal: false,
        displayEditModal: false,
        event: {},
        fileToRemove: {},
        fileUuid: "",
        files: [],
        headers: [
          {
            title: "Nome",
            field: "title",
            isLink: true,
            displayCallback: (value) => {
              return value;
            },
          },
          {
            title: "Categoria",
            field: "category",
            isLink: false,
            displayCallback: this.displayFileCategory,
          },
          {
            title: "Visibilidade",
            field: "visibility",
            isLink: false,
            displayCallback: this.displayFileVisibility,
          },
          {
            title: "Tipo",
            field: "file_type",
            isLink: false,
            displayCallback: this.displayFileType,
          },
        ],
        removeConfirmationVisible: false,
        removeConfirmationMessage: "",
      };
    },

    beforeMount() {
      this.refreshFilesList();
    },

    methods: {
      showEventFile(eventFileId) {
        this.fileUuid = eventFileId;
        this.displayEditModal = true;
      },

      refreshFilesList() {
        this.$store
        .dispatch(FETCH_EVENT, this.$route.params.event_id)
        .then((event) => {
          this.event = event;
          this.files = event.files;
        })
        .catch(() => {
          this.$emit("alert", DefaultErrorMessage);
          this.$router.push({ name: "admin-event-list" });
        });
      },

      showFileUploadModal() {
        this.displayUploadModal = true;
      },

      hideFileUploadModal() {
        this.refreshFilesList();
        this.displayUploadModal = false;
      },

      hideFileEditModal() {
        this.refreshFilesList();
        this.displayEditModal = false;
      },

      displayFileCategory(value) {
        if (value === "EDITORIAL") {
          return "Editorial (Edital, Errata, etc)";
        } else if (value === "STUDY") {
          return "Material de Apoio";
        }

        return "Desconhecido";
      },

      displayFileVisibility(value) {
        if (value === "EVERYONE") {
          return "Todos (visível publicamente)";
        } else if (value === "SUBSCRIBED") {
          return "Apenas para inscritos";
        } else if (value === "UNLISTED") {
          return "Não listado (acessível por link)";
        }

        return "Desconhecido";
      },

      displayFileType(value) {
        if (value === "DOCUMENT") {
          return "Documento de Texto";
        } else if (value === "IMAGE") {
          return "Imagem";
        } else if (value === "VIDEO") {
          return "Vídeo";
        } else if (value === "COMPRESSED") {
          return "Arq. Comprimido";
        }

        return "Desconhecido";
      },

      showRemoveConfirmation(file) {
        this.fileToRemove = file;
        this.removeConfirmationMessage = `Deseja realmente continuar? <br> Isto irá remover completamente o arquivo de código <b>${file.id}</b>.`;
        this.removeConfirmationVisible = true;
      },

      hideRemoveConfirmation() {
        this.removeConfirmationVisible = false;
      },

      removeFile() {
        const params = {
          event_id: this.event.id,
          file_id: this.fileToRemove.id,
        };

        this.$store
          .dispatch(REMOVE_EVENT_FILE, params)
          .then(() => {
            this.$emit("alert", {text: "Arquivo removido com sucesso!", style: "success", expSecs: 3})
            this.refreshFilesList();
            this.fileToRemove = {};
            this.removeConfirmationVisible = false;
          })
          .catch(() => {
            this.$emit("alert", DefaultErrorMessage);
            this.$router.push({ name: "admin-event-list" });
          });

      },
    },
  };
</script>
