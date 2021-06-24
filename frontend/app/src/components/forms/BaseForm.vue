<template>
  <form class="BaseForm">
    <slot />

    <the-button
      :text="submitText"
      v-if="showSubmitButton"
      class="BaseForm-Button BaseForm-Button--Primary"
      @click="submit"
    />
  </form>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .BaseForm {
    margin: 0;
    padding: 0;
    border: none;
  }
</style>

<script>
  import TheIcon from "@/components/TheIcon";
  import TheButton from "@/components/TheButton";

  export default {
    components: {
      TheButton,
      TheIcon,
    },

    props: {
      submitText: {
        type: String,
        default: "Enviar",
      },

      showSubmitButton: {
        type: Boolean,
        default: true,
      },

      initialValues: {
        type: Object,
        default: () => {},
      },

      fields: {
        type: Array,
        default: () => [],
      },
    },

    data: () => ({
      valid: false,
      checked: false,
    }),

    watch: {
      fields() {
        this.fillInitialData();
      },

      initialValues() {
        this.fillInitialData();
      },
    },

    mounted() {
      this.fillInitialData();
    },

    methods: {
      submit() {
        this.validate();

        if (!this.valid) {
          this.$emit("failed_validation");
          return;
        }

        let data = this.getFormData();
        this.$emit("submit", data);
      },

      clear() {
        this.fields.forEach((element) => {
          element.clear();
        });
      },

      reset() {
        this.clear();
        this.fillInitialData();
      },

      getFormData() {
        return this.fields
          .filter((element) => !element.disabled)
          .reduce((map, obj) => {
            map[obj.name] = obj.getValue();
            return map;
          }, {});
      },

      validate() {
        this.fields.forEach((element) => {
          element.validate();
        });
        let errorFields = this.fields.filter((element) => element.hasError);

        this.valid = errorFields.length === 0;
        if (!this.valid) {
          this.handleInvalidation(errorFields);
        }
      },

      getFieldsByName(fieldName) {
        return this.fields.filter((obj) => obj.name === fieldName);
      },

      fillInitialData() {
        if (
          this.initialValues === undefined ||
          this.initialValues === null ||
          Object.keys(this.initialValues).length === 0
        ) {
          return;
        }

        const filteredItems = Object.keys(this.initialValues)
          .filter((fieldName) => {
            return this.getFieldsByName(fieldName).length > 0;
          })
          .reduce((obj, key) => {
            obj[key] = this.initialValues[key];
            return obj;
          }, {});

        Object.keys(filteredItems).map((fieldName) => {
          let field = this.getFieldsByName(fieldName)[0];
          field.setValue(filteredItems[fieldName]);
        });
      },

      handleInvalidation(fields) {
        if (fields.length > 1) {
          const fieldsNames = fields
            .map((field) => field.placeholder)
            .join(", ");
          this.$emit(
            "error",
            `Campos inválidos: ${fieldsNames}. Por favor, corrija-os e tente novamente.`
          );
          return;
        }

        let field = fields[0];
        this.$emit(
          "error",
          `O campo ${field.placeholder} está inválido. Por favor, corrija-o e tente novamente.`
        );
      },
    },
  };
</script>
