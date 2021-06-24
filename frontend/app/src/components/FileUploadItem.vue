<template>
  <div class="FileUploadItem">
    <div
      :class="`FileUploadItem-Styles--${style}`"
      class="FileUploadItem-Container"
    >
      <div
        :class="`FileUploadItem-Styles--${style}`"
        class="FileUploadItem-IconWrapper"
      >
        <the-icon
          :icon="fileIcon"
          class="FileUploadItem-Icon"
        />
      </div>

      <div
        :class="`FileUploadItem-Styles--${style}`"
        class="FileUploadItem-Data"
      >
        <template v-if="canEdit">
          <event-file-upload-form
            class="FileUploadItem-Form"
            ref="eventFileUploadForm"
            :show-submit-button="false"
            :initial-data="{
              title: fileName,
            }"
          />
        </template>

        <template v-else>
          <div class="FileUploadItem-Name">
            {{ file.name }}
          </div>

          <div class="FileUploadItem-Details">
            {{ fileDataDetails }}
          </div>
        </template>

        <div class="FileUploadItem-Description">
          {{ description }}
        </div>
      </div>

      <div
        v-if="canRemove"
        :class="`FileUploadItem-ReactiveStyles--${style}`"
        class="FileUploadItem-Remove"
        title="Toque para remover este arquivo da fila de envio"
        @click="remove"
      >
        <the-icon
          icon="times"
          class="FileUploadItem-RemoveIcon"
        />
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .FileUploadItem {
    margin-bottom: 10px;

    &-Container {
      color: $color-primary-foreground;
      border: 1px solid $background-tertiary-border;
      border-radius: 5px;
      display: flex;
    }

    &-IconWrapper {
      flex: 0 0 50px;
      text-align: center;
      padding: 10px;
    }

    &-Icon {
      font-size: 32pt;
    }

    &-Data {
      padding: 0 10px;
      flex: 1 1 100%;
      display: flex;
      flex-direction: column;
      justify-content: space-evenly;
      border-left: 1px solid $background-tertiary-border;
      border-right: 1px solid $background-tertiary-border;
    }

    &-Form {
      margin-top: 10px;
      background-color: $background-secondary-color;
      border: 1px solid $background-secondary-border;
    }

    &-Name {
      font-size: 14pt;
      font-weight: bold;
    }

    &-Description {
      font-size: 12pt;
    }

    &-Remove {
      flex: 0 0 50px;
      cursor: pointer;
      display: flex;
      justify-content: center;
      align-items: center;
      font-size: 22pt;

      &:hover {
        font-size: 24pt;
      }
    }

    &-RemoveButton {
      width: 50px;
      height: 50px;
    }

    &-RemoveIcon {
    }

    &-Styles {
      &--error {
        background-color: $color-background-error;
        border-color: $color-border-error;
      }

      &--info,
      &--question {
        background-color: $color-background-info;
        border-color: $color-border-info;
      }

      &--warning {
        background-color: $color-border-warning;
        border-color: $color-border-warning;
      }

      &--success {
        background-color: $color-border-success;
        border-color: $color-border-success;
      }
    }

    &-ReactiveStyles {
      &--error {
        &:hover {
          background-color: $color-hover-error;
        }

        &:active {
          background-color: $color-active-error;
        }
      }

      &--info,
      &--question {
        &:hover {
          background-color: $color-hover-info;
        }

        &:active {
          background-color: $color-active-info;
        }
      }

      &--warning {
        &:hover {
          background-color: $color-hover-warning;
        }

        &:active {
          background-color: $color-active-warning;
        }
      }

      &--success {
        &:hover {
          background-color: $color-hover-success;
        }

        &:active {
          background-color: $color-active-success;
        }
      }
    }
  }
</style>

<script>
  import {
    ALLOWED_MIME_TYPES,
    getIconFromMimeType,
    getTypeFromMimeType,
  } from "@/common/filemgr.service";
  import TheButton from "@/components/TheButton";
  import TheIcon from "@/components/TheIcon";
  import { POST_FILE, CREATE_EVENT_FILE } from "@/store/actions.type";
  import { EVENT_FILE_CATEGORY_OPTIONS, EVENT_FILE_VISIBILITY_OPTIONS } from "@/common/enums";
  import ButtonIcon from "@/components/ButtonIcon";
  import ButtonIconSmall from "@/components/ButtonIconSmall";
  import TheField from "@/components/fields/TheField";
  import EventFileUploadForm from "@/components/forms/EventFileUploadForm";

  const MAXIMUM_UPLOAD_FILE_SIZE = 25 * 1024 * 1024;

  export default {
    name: "FileUploadItem",

    components: {
      EventFileUploadForm,
      TheField,
      ButtonIconSmall,
      ButtonIcon,
      TheIcon,
      TheButton,
    },

    props: {
      event: {
        type: Object,
        required: true,
      },

      file: {
        type: File,
        required: true,
      },
    },

    data() {
      return {
        statuses: {
          readyToUpload: {
            id: "READY_TO_UPLOAD",
            style: "info",
            description: "O arquivo está pronto para ser enviado.",
          },

          rejectedTooBig: {
            id: "REJECTED_TOO_BIG",
            style: "error",
            description: "O tamanho máximo para envio de arquivos é 25 MB.",
          },

          rejectedInternal: {
            id: "REJECTED_INTERNAL",
            style: "error",
            description: "Ocorreu um erro interno com o arquivo. Tente novamente mais tarde.",
          },

          rejectedType: {
            id: "REJECTED_TYPE",
            style: "error",
            description: "Só são permitidos documentos de texto e imagens.",
          },

          rejectedInvalidData: {
            id: "REJECTED_INVALID_DATA",
            style: "error",
            description: "Foram informados dados inválidos.",
          },

          uploading: {
            id: "UPLOADING",
            style: "info",
            description: "O arquivo está sendo enviado...",
          },

          uploadedSuccessfully: {
            id: "UPLOADED",
            style: "success",
            description: "Arquivo enviado com sucesso!",
          },
        },
        status: null,
        style: "info",
        description: "",
        uploadResponse: null,
        eventResponse: null,
        fileName: "",
        fileVisibility: "",
        fileCategory:  "",
      };
    },

    computed: {
      fileIcon() {
        return getIconFromMimeType(this.file.type);
      },

      fileType() {
        return getTypeFromMimeType(this.file.type);
      },

      canRemove() {
        return [
          this.statuses.uploadedSuccessfully,
          this.statuses.uploading,
        ].indexOf(this.status) === -1;
      },

      canEdit() {
        return [
          this.statuses.readyToUpload,
          this.statuses.rejectedInvalidData,
        ].indexOf(this.status) !== -1;
      },

      fileDataDetails() {
        let fileCategory = "";
        switch (this.fileCategory) {
          case EVENT_FILE_CATEGORY_OPTIONS[0].value:
            fileCategory = "Editorial";
            break;
          case EVENT_FILE_CATEGORY_OPTIONS[1].value:
            fileCategory = "Mat. de Apoio";
            break;
          default:
            fileCategory = this.fileCategory;
            break;
        }

        let fileVisibility = "";
        switch (this.fileVisibility) {
          case EVENT_FILE_VISIBILITY_OPTIONS[0].value:
            fileVisibility = "Público";
            break;
          case EVENT_FILE_VISIBILITY_OPTIONS[1].value:
            fileVisibility = "Inscritos";
            break;
          case EVENT_FILE_VISIBILITY_OPTIONS[2].value:
            fileVisibility = "Não Listado";
            break;
          default:
            fileVisibility = this.fileVisibility;
            break;
        }

        return `${fileCategory} | ${fileVisibility}`;
      },
    },

    watch: {
      file(value) {
        this.fileName = value.name;
        this.refreshStatus();
      },
    },

    mounted() {
      this.fileName = this.file.name;
      this.refreshStatus();
    },

    methods: {
      setStatus(status) {
        this.status = status;
        this.style = status.style;
        this.description = status.description;
      },

      refreshStatus() {
        if (typeof this.file !== "object") {
          this.setStatus(this.statuses.rejectedInternal);
          this.$emit('invalid', this.file);
          return;
        }

        if (this.file.size > MAXIMUM_UPLOAD_FILE_SIZE) {
          this.setStatus(this.statuses.rejectedTooBig);
          this.$emit('invalid', this.file);
          return;
        }

        if (!ALLOWED_MIME_TYPES.includes(this.file.type)) {
          this.setStatus(this.statuses.rejectedType);
          this.$emit('invalid', this.file);
          return;
        }

        this.setStatus(this.statuses.readyToUpload);
      },

      remove() {
        this.$emit('remove', this.file);
      },

      upload() {
        return new Promise((resolve, reject) => {
          if ([this.statuses.readyToUpload, this.statuses.rejectedInvalidData].indexOf(this.status) === -1) {
            reject('File is not ready to be uploaded!');
            return;
          }

          this.$refs.eventFileUploadForm.$refs.eventFileUploadForm.submit();

          if (!this.$refs.eventFileUploadForm.$refs.eventFileUploadForm.valid) {
            this.setStatus(this.statuses.rejectedInvalidData);
            reject(this.statuses.rejectedInvalidData.description);
            return;
          }

          const formData = this.$refs.eventFileUploadForm.$refs.eventFileUploadForm.getFormData();

          this.$store
            .dispatch(POST_FILE, this.file)
            .then((response) => {
              let eventFileParams = {
                event_id: this.event.id,
                payload: {
                  visibility: formData.visibility,
                  filemgr_uuid: response.data.id,
                  category: formData.category,
                  file_type: this.fileType,
                  title: formData.title,
                },
              };
              this.uploadResponse = response.data;

              this.fileName = response.data.title;
              this.fileCategory = response.data.category;
              this.fileVisibility = response.data.visibility;

              this.$store
                .dispatch(CREATE_EVENT_FILE, eventFileParams)
                .then((eventFileResponse) => {
                  this.eventResponse = eventFileResponse.data;
                  this.setStatus(this.statuses.uploadedSuccessfully);
                  resolve({...eventFileResponse.data, filemgr_response: response.data});
                })
                .catch((error) => {
                  console.log(error);
                  this.setStatus(this.statuses.rejectedInternal);
                  reject(error);
                });
            }).catch((error) => {
              console.log(error);
              this.setStatus(this.statuses.rejectedInternal);
              reject(error);
            });
        });
      },
    },
  };
</script>
