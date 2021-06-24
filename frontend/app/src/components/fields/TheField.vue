<template>
  <component
    ref="field"
    :id="uid"
    :name="name"
    :placeholder="placeholder"
    :required="required"
    :description="description"
    :disabled="disabled"
    v-bind="metadata"
    :is="getFieldComponentName()"
    class="TheField"
    @change="hasChanged"
    @keyup="$emit('keyup', $event)"
  />
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .TheField {
  }
</style>

<script>
  import CheckboxField from "@/components/fields/CheckboxField";
  import NumberField from "@/components/fields/NumberField";
  import SelectField from "@/components/fields/SelectField";
  import TextField from "@/components/fields/TextField";
  import DateField from "@/components/fields/DateField";

  let uid = 0;

  export default {
    name: "TheField",

    components: {
      CheckboxField,
      DateField,
      NumberField,
      SelectField,
      TextField,
    },

    props: {
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

      type: {
        type: String,
        required: true,
        validator: function(value) {
          return ["date", "number", "text", "select", "check"].includes(value);
        },
      },

      disabled: {
        type: Boolean,
        default: false,
      },

      initialValue: {
        type: [String, Number, Boolean],
        default: null,
      },

      required: {
        type: Boolean,
        default: false,
      },

      metadata: {
        type: Object,
        default() {
          return {};
        },
      },
    },

    data() {
      uid += 1;
      return {
        uid: `the-field-${uid}`,
        fieldMap: {
          check: "CheckboxField",
          date: "DateField",
          number: "NumberField",
          select: "SelectField",
          text: "TextField",
        },
      };
    },

    computed: {
      hasError() {
        return this.$refs.field.hasError;
      },
    },

    mounted() {
      if (this.initialValue !== null) {
        this.setValue(this.initialValue);
      }
    },

    methods: {
      getFieldComponentName() {
        return this.fieldMap[this.type];
      },

      getValue() {
        return this.$refs.field.getValue();
      },

      hasChanged(value) {
        this.$emit("change", value);
      },

      setValue(value) {
        this.$refs.field.setValue(value);
        return this.getValue();
      },

      clear() {
        this.$refs.field.clear();
      },

      validate() {
        return this.$refs.field.validate();
      },
    },
  };
</script>
