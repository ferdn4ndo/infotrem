<template>
  <div class="FileUpload">
    <div
      class="FileUpload-UploadArea"
      @dragenter="startDragging"
      @click="selectFileToUpload"
      @dragleave="endDragging"
      @drop.prevent="dropFile"
      @dragover.prevent
    >
      <input
        :id="fileFieldId"
        class="FileUpload-Field"
        multiple="multiple"
        type="file"
        @change="selectedFile"
      >

      <div
        v-show="!isDroppingFile"
        class="FileUpload-UploadAreaMessageWrapper FileUpload-NoDrag"
      >
        <div class="FileUpload-IconWrapper FileUpload-NoDrag">
          <the-icon
            class="FileUpload-Icon FileUpload-NoDrag"
            icon="files"
          />
        </div>

        <p class="FileUpload-UploadAreaText FileUpload-NoDrag" >
          Arraste e solte o(s) arquivo(s) neste local ou clique aqui para abrir
          a janela de seleção de arquivos do sistema.
        </p>
      </div>

      <div
        v-show="isDroppingFile"
        class="FileUpload-UploadAreaDrop FileUpload-NoDrag"
      >
        <p class="FileUpload-UploadAreaText--bigger FileUpload-NoDrag">
          Solte o(s) arquivo(s) aqui!
        </p>
      </div>
    </div>

    <div class="FileUpload-UploadedFiles">
      <file-upload-item
        v-for="file in filesToUpload"
        ref="fileRefs"
        :file="file"
        :event="event"
        :key="file.name"
        class="FileUpload-UploadedFile"
        @remove="removeFile"
        @invalid="invalidateFile"
      />
    </div>

    <div class="FileUpload-ButtonWrapper">
      <the-button
        :text="uploadButtonText"
        :disabled="!readyToUploadFiles"
        class="FileUpload-Button"
        @click="performUpload"
      />
    </div>
  </div>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .FileUpload {
    &-NoDrag {
      pointer-events: none;
    }

    &-Field {
      display: none;
    }

    &-Button {
    }

    &-ButtonWrapper {
      padding: 0 15px 5px 10px;
      box-sizing: border-box;

      @media screen and (min-width: $tablet-breakpoint - 1) {
        max-width: 250px;
        margin-left: auto;
      }
    }

    &-UploadArea {
      position: relative;
      cursor: pointer;
      display: flex;
      justify-content: center;
      align-items: center;
      outline-offset: -10px;
      outline: $color-gray-medium dashed 2px;
      color: $color-text-gray;
      background-color: $color-gray-light;
      min-height: 40vh;
      width: 100%;
      height: 100%;
    }

    &-UploadAreaDrop {
      position: relative;
      display: flex;
      justify-content: center;
      align-items: center;
      width: 100%;
      height: 100%;
      outline: $color-primary-border dashed 2px;
      outline-offset: -10px;
      background-color: $color-primary-background-mid;
      min-height: 40vh;
    }

    &-UploadAreaMessageWrapper {
      margin: 10px;
    }

    &-UploadAreaText {
      font-size: 12pt;
      cursor: default;
      margin: 20px;
      text-align: center;

      &--bigger {
        font-size: 14pt;
        font-weight: bold;
      }
    }

    &-UploadedFiles {
      margin: 10px 10px 0;
      box-sizing: border-box;
    }

    &-UploadedFile {
    }

    &-IconWrapper {
      text-align: center;
      padding: 10px 10px 0 10px;
      margin: 10px 0;
    }

    &-Icon {
      margin-left: auto;
      margin-right: auto;
      font-size: 36pt;
    }

    &-Paragraph {
      cursor: default;
      text-align: justify;

      margin: 10px;

      &--bold {
        font-weight: bold;
      }
    }

    &-FadeTransition {
      &-leave-active {
        transition: all 1s;
      }

      &-leave-to {
        opacity: 0;
      }
    }
  }
</style>

<script>
  import { mapGetters } from "vuex";
  import TheButton from "@/components/TheButton";
  import TheIcon from "@/components/TheIcon";
  import FileUploadItem from "@/components/FileUploadItem";

  export default {
    name: "FileUpload",

    components: {
      FileUploadItem,
      TheIcon,
      TheButton,
    },

    props: {
      event: {
        type: Object,
        required: true,
      },

      multiple: {
        type: Boolean,
        default: () => false,
      },
    },

    data() {
      return {
        readyToUploadFiles: false,
        isDroppingFile: false,
        filesToUpload: [],
        invalidFiles: [],
        uploadedFiles: [],
      };
    },

    computed: {
      ...mapGetters(["currentUser", "isAuthenticated"]),

      fileFieldId() {
        return `fileField-${this._uid}`;
      },

      uploadButtonText() {
        if (this.filesToUpload.length === 0 ) {
          return 'Nenhum arquivo';
        } else if(this.filesToUpload.length === 1) {
          return 'Enviar arquivo';
        } else {
          return `Enviar ${this.filesToUpload.length} arquivos`;
        }
      },
    },

    watch: {
      filesToUpload() {
        this.checkIfCanUpload();
      },

      invalidFiles() {
        this.checkIfCanUpload();
      },
    },

    methods: {
      selectFileToUpload() {
        document.getElementById(this.fileFieldId).click();
      },

      hasCompletedUploading() {
        return this.$refs.fileRefs.filter((file) => {
          return file.status.id !== 'UPLOADED';
        }).length === 0;
      },

      reset() {
        this.filesToUpload = [];
        this.invalidFiles = [];
        this.uploadedFiles = [];
      },

      performUpload() {
        this.$refs.fileRefs
          .filter((file) => {
            return [file.statuses.readyToUpload, file.statuses.rejectedInvalidData].indexOf(file.status) !== -1;
          })
          .forEach((file) => {
            file.upload().then((file_data) => {
              this.$emit('fileUploaded', file_data);

              if (this.hasCompletedUploading()) {
                this.reset();
                this.$emit('close');
              }
            }).catch((error) => {
              console.log(`[FileUpload] ERROR: ${error}`);
            });
        });
      },

      startDragging(event) {
        this.isDroppingFile = true;
      },

      endDragging(event) {
        this.isDroppingFile = false;
      },

      dropFile(event) {
        let droppedFiles = event.dataTransfer.files;
        this.endDragging();

        this.addFilesToUpload(droppedFiles);
      },

      selectedFile(event) {
        let selectedFiles = event.target.files;

        this.addFilesToUpload(selectedFiles);
      },

      addFilesToUpload(files) {
        if (!files || typeof files === "undefined" || files.length === 0) {
          return;
        }

        // Cast FileList to array
        ([...files]).forEach(file => {
          this.filesToUpload.push(file);
        });

        this.checkIfCanUpload();
      },

      removeFile(fileToRemove){
        this.filesToUpload = this.filesToUpload.filter(file => {
          return file !== fileToRemove;
        });

        this.invalidFiles = this.invalidFiles.filter(file => {
          return file !== fileToRemove;
        });

        this.checkIfCanUpload();
      },

      checkIfCanUpload() {
        this.readyToUploadFiles = (
          this.filesToUpload.length > 0 && this.invalidFiles.length === 0
        );
      },

      invalidateFile(file) {
        console.log('invalidate file', file);
        this.invalidFiles.push(file);
      },
    },
  };
</script>
