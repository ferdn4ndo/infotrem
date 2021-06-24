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
    :max-length="maxLength()"
    @change="hasChanged"
  />
</template>

<script>
  import createNumberMask from "text-mask-addons/dist/createNumberMask";
  import TextField from "@/components/fields/TextField";

  export default {
    name: "NumberField",

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

      allowDecimal: {
        type: Boolean,
        default: false,
      },

      requireDecimal: {
        type: Boolean,
        default: false,
      },

      decimalPrecision: {
        type: Number,
        default: 2,
      },

      allowNegative: {
        type: Boolean,
        default: false,
      },

      prefix: {
        type: String,
        default: "",
      },

      suffix: {
        type: String,
        default: "",
      },

      decimalSeparator: {
        type: String,
        default: ",",
      },

      punctuateThousands: {
        type: Boolean,
        default: true,
      },

      thousandSeparator: {
        type: String,
        default: ".",
      },

      maxValue: {
        type: Number,
        default: 2147483647, // int32 max
      },

      allowLeadingZeroes: {
        type: Boolean,
        default: true,
      },
    },

    data: () => ({
      hasError: false,
    }),

    computed: {
      computedMask() {
        if (this.mask !== null) {
          return this.mask;
        }

        return createNumberMask({
          prefix: this.prefix,
          suffix: this.suffix,
          allowDecimal: this.allowDecimal,
          decimalSymbol: this.decimalSeparator,
          decimalLimit: this.decimalPrecision,
          includeThousandsSeparator: this.punctuateThousands,
          thousandsSeparatorSymbol: this.thousandSeparator,
          allowNegative: this.allowNegative,
          integerLimit: this.maxLength,
          requireDecimal: this.requireDecimal,
          allowLeadingZeroes: this.allowLeadingZeroes,
        });
      },
    },

    methods: {
      getValue() {
        let value = this.$refs.field.getValue();

        if (value === null || value === "") {
          return null;
        }

        value = value.toString();
        if (this.allowDecimal && this.mask === null) {
          const sanitizeRegex = `/[^0-9${this.decimalSeparator}]/`;
          value = value.to.replace(sanitizeRegex, "");
          value = value.replace(this.decimalSeparator, ".");
        } else {
          value = value.replace(/[^0-9]/g, "");
        }

        return parseInt(value);
      },

      setValue(newValue) {
        this.$refs.field.setValue(newValue);
      },

      clear() {

      },

      validate() {
        this.$refs.field.validate();
        this.hasError = this.$refs.field.hasError;
      },

      hasChanged(value) {
        this.$emit("change", value);
      },

      maxLength() {
        if (this.mask) {
          return Array.isArray(this.mask)
            ? this.mask[0].length
            : this.mask.length;
        }

        let maxChars = Math.ceil(Math.log10(this.maxValue));

        if (this.allowDecimal) {
          maxChars += this.decimalSeparator.length + this.decimalPrecision;
        }

        if (this.punctuateThousands) {
          maxChars += Math.floor(Math.log10(this.maxValue) / 3);
        }

        return Math.round(maxChars);
      },
    },
  };
</script>
