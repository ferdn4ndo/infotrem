<template>
  <base-form
    ref="adminEventFileForm"
    class="AdminEventFileForm"
    :initial-values="initialData"
    :fields="fields"
    submit-text="Salvar"
    @error="handleError"
    @submit="handleValidData"
  >
    <!-- Title -->
    <the-field
      ref="title"
      :metadata="{
        maxLength: 120,
      }"
      :required="true"
      name="title"
      type="text"
      class="EventFileUploadForm-Input"
      placeholder="Nome do Arquivo"
      description="Insira o nome (título) do arquivo."
    />

    <!-- Category -->
    <the-field
      ref="category"
      :metadata="{
        items: fileCategoryOptions,
      }"
      :required="true"
      name="category"
      type="select"
      class="EventFileUploadForm-Input"
      placeholder="Categoria do Arquivo"
      description="Editorial (Editais, erratas, etc) ou Material de Apoio (apostila, curso, etc)."
    />

    <!-- Visibility -->
    <the-field
      ref="visibility"
      :metadata="{
        items: fileVisibilityOptions,
      }"
      :required="true"
      name="visibility"
      type="select"
      class="EventFileUploadForm-Input"
      placeholder="Visibilidade do Arquivo"
      description="Define quem poderá ver o arquivo publicamente"
    />
  </base-form>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .AdminEventFileForm {
    &-Input {
      margin-bottom: 5px;
    }

    &-Paragraph {
      cursor: default;
      text-align: justify;

      margin: 5px 0 10px;

      &--bold {
        font-weight: bold;
      }
    }
  }
</style>

<script>
  import { mapGetters } from "vuex";
  import { UPDATE_EVENT_FILE } from "@/store/actions.type";
  import { EVENT_FILE_CATEGORY_OPTIONS, EVENT_FILE_VISIBILITY_OPTIONS } from "@/common/enums";
  import BaseForm from "@/components/forms/BaseForm";
  import CheckboxField from "@/components/fields/CheckboxField";
  import SelectField from "@/components/fields/SelectField";
  import TextField from "@/components/fields/TextField";
  import TheIcon from "@/components/TheIcon";
  import TheButton from "@/components/TheButton";
  import TheField from "@/components/fields/TheField";

  export default {
    components: {
      TheField,
      BaseForm,
      CheckboxField,
      SelectField,
      TextField,
      TheIcon,
      TheButton,
    },

    props: {
      event: {
        type: Object,
        default: () => {},
      },

      file: {
        type: Object,
        default: () => {},
      },

      redirectAfterSave: {
        type: Boolean,
        default: true,
      },
    },

    data: () => ({
      fileCategoryOptions: EVENT_FILE_CATEGORY_OPTIONS,
      fileVisibilityOptions: EVENT_FILE_VISIBILITY_OPTIONS,
      fields: [],
      initialData: {},
    }),

    computed: {
      ...mapGetters(["currentUser", "billetGateways"]),
    },

    watch: {
      file(value) {
        if (value !== null && typeof value !== "undefined") {
          this.initialData = value;
        }
      },
    },

    mounted() {
      this.updateFields();
    },

    methods: {
      handleError(error) {
        this.$emit("error", error);
      },

      handleValidData(payload) {
        const finalPayload = { ...payload, file_id: this.file.id, event_id: this.event.id };

        this.$store
          .dispatch(UPDATE_EVENT_FILE, finalPayload)
          .then((event) => {
            this.$emit("success", `Arquivo atualizado com sucesso!`);

            if (this.redirectAfterSave) {
              this.$router.push({
                name: "admin-event-files",
                params: { event_id: event.id },
              });
            }
          })
          .catch((error) => {
            if (error.response) {
              if (error.response.status === 400) {
                this.$emit(
                  "error",
                  "Existem campos inválidos. Por favor, confira as informações fornecidas e tente novamente."
                );
              } else {
                // ToDo: save to a log here
                this.$emit(
                  "error",
                  "Ocorreu um erro interno ao processar seu cadastro. Por favor, entre em contato relatando o problema."
                );
              }
            }
          });
      },

      updateFields() {
        this.fields = [
          this.$refs.title,
          this.$refs.category,
          this.$refs.visibility,
        ];
      },
    },
  };
</script>
