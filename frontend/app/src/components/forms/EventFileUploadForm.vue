<template>
  <base-form
    ref="eventFileUploadForm"
    :initial-values="initialData"
    :fields="fields"
    :show-submit-button="showSubmitButton"
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

  .EventFileUploadForm {
    &-Input {
      margin-bottom: 5px;
    }
  }
</style>

<script>
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
      initialData: {
        type: Object,
        default() { return {}; },
      },

      showSubmitButton: {
        type: Boolean,
        default: true,
      },
    },

    data: () => ({
      fileCategoryOptions: EVENT_FILE_CATEGORY_OPTIONS,
      fileVisibilityOptions: EVENT_FILE_VISIBILITY_OPTIONS,
      fields: [],
    }),

    mounted() {
      this.updateFields();
    },

    methods: {
      handleError(error) {
        this.$emit("error", error);
      },

      handleValidData(payload) {
        this.$emit("success", payload);
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
