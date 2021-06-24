<template>
  <text-field
    v-mask="computedMask"
    ref="field"
    :id="id"
    :name="name"
    :disabled="disabled"
    :required="required"
    :placeholder="placeholder"
    :description="description"
    :regex-validator="computedRegex"
    @change="hasChanged"
  />
</template>

<script>
  import moment from "moment";
  import { DATE_REGEX } from "@/common/regex";
  import TextField from "@/components/fields/TextField";

  export default {
    name: "DateField",

    components: {
      TextField,
    },

    props: {
      id: {
        type: String,
        default: null,
      },

      name: {
        type: String,
        required: true,
      },

      placeholder: {
        type: String,
        default: "",
      },

      description: {
        type: String,
        default: "",
      },

      disabled: {
        type: Boolean,
        default: false,
      },

      required: {
        type: Boolean,
        default: false,
      },

      mask: {
        type: String | Array,
        default: null,
      },

      regexValidator: {
        type: RegExp,
        default: null,
      },

      format: {
        type: String,
        default: "dd/mm/yyyy",
      },
    },

    data: () => ({
      dateRegex: DATE_REGEX,
      hasError: false,
    }),

    computed: {
      computedMask() {
        return this.mask !== null ? this.mask : "##/##/####";
      },

      computedRegex() {
        return this.regexValidator !== null ? this.regexValidator : DATE_REGEX;
      },
    },

    methods: {
      getValue() {
        let value = this.$refs.field.getValue();

        if (value === null || value === undefined || value === "") {
          return null;
        }

        let date = moment(value, this.format.toUpperCase());
        if (!date.isValid()) {
          console.log("value is invalid: ", value);
          this.setValue(null);
          return null;
        }

        return date.format("YYYY-MM-DD").toString();
      },

      setValue(newValue) {
        if (!newValue) {
          this.clear();
          return;
        }

        let date = moment(newValue);
        if (date.isValid()) {
          this.$refs.field.setValue(
            date.format(this.format.toUpperCase()).toString()
          );
        } else {
          console.log("Tried to set a invalid date: ", newValue);
        }
      },

      clear() {
        this.$refs.field.setValue("");
      },

      validate() {
        this.$refs.field.validate();
        this.hasError = this.$refs.field.hasError;
      },

      hasChanged(value) {
        this.$emit("change", value);
      },
    },
  };
</script>
