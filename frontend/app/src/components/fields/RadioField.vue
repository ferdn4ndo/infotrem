<template>
  <fieldset
    :class="{ 'RadioField--hasError': hasError }"
    class="RadioField"
  >
    <div
      class="RadioField-OptionBlock"
      :class="{ 'RadioField-OptionBlock--fullWidth': oneOptionPerLine }"
      v-for="(item, index) in items"
    >
      <input
        :class="{
          'RadioField-Input--hasError': hasError,
          'RadioField-Input--disabled': disabled,
          'RadioField-Input--checked': checked,
        }"
        :disabled="isItemDisabled(item)"
        :checked="isItemChecked(item, index)"
        :id="computeItemId(index)"
        :name="name"
        :value="item.value"
        class="RadioField-Input"
        type="radio"
        v-model="value"
        @change="validate"
      >

      <label
        :class="{ 'RadioField--hasError': hasError }"
        :for="computeItemId(index)"
        class="RadioField-Label"
      >
        {{ item.label }}
      </label>
    </div>

    <div class="RadioField-DescriptionBlock">
      <p
        v-if="!hasError"
        class="RadioField-Description"
      >
        {{ description }}
      </p>

      <p
        v-if="hasError"
        class="RadioField-Description RadioField--hasError"
      >
        {{ errorDescription }}
      </p>

      <p
        v-if="required"
        :class="{ 'RadioField--hasError': hasError }"
        class="RadioField-RequiredMark"
        title="Campo obrigatório"
      >
        <the-icon
          icon="asterisk"
          size="12pt"
        />
      </p>
    </div>
  </fieldset>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .RadioField {
    display: flex;
    border: none;
    padding: 0;
    margin: 0;

    -webkit-transition-property: font-size, left, top, color;
    -webkit-transition-duration: 0.5s;
    -webkit-transition-timing-function: ease-in-out;
    transition-property: font-size, left, top, color;
    transition-duration: 0.5s;
    transition-timing-function: ease-in-out;

    &-Input {
      -webkit-appearance: none;
      background-color: #fafafa;
      border: 1px solid #cacece;
      box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05),
        inset 0px -15px 10px -12px rgba(0, 0, 0, 0.05);
      padding: 9px;
      border-radius: 3px;
      display: inline-block;
      position: relative;
      flex: 0 0 auto;

      &:checked {
        border: 1px solid $foreground-primary-color--border;
      }

      &:checked:after {
        content: "x";
        font-size: 20px;
        font-weight: bold;
        position: absolute;
        top: -3px;
        left: 3px;
        color: $foreground-dark-color;
      }

      &:disabled {
        background-color: $disabled-background-color;
        color: $disabled-foreground-color;
      }
    }

    &-Label {
      flex: 1 1 auto;
      font-size: 14pt;
      color: $color-text-gray;
      width: 100%;

      &:hover {
        cursor: pointer;
        font-weight: bold;
      }
    }

    &-MustAcceptMark {
      flex: 0 0 auto;
      font-size: 12pt;
      color: $color-text-gray;
      right: 0;
      margin: 0;
      margin-block-start: 0;
      margin-block-end: 0;
    }

    &-DescriptionBlock {
      display: flex;
    }

    &-Description {
      display: inline-block;
      font-size: 10pt;
      color: $color-text-gray;
      margin: 5px 10px 5px 5px;
      cursor: default;
      margin-block-start: 0;
      margin-block-end: 0;
      text-align: justify;
      flex: 1 1 auto;
    }

    &--checked {
    }

    &--disabled {
    }

    &--hasError {
      color: $color-text-error;
      border-color: $color-text-error;
    }
  }
</style>

<script>
  import TheIcon from "@/components/TheIcon";

  export default {
    name: "RadioField",

    components: {
      TheIcon,
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

      description: {
        type: String,
        default: "",
      },

      oneOptionPerLine: {
        type: Boolean,
        default: false,
      },

      startValue: {
        type: String,
        default: null,
      },

      disabled: {
        type: Boolean,
        default: false,
      },

      required: {
        type: Boolean,
        default: false,
      },

      items: {
        type: Array,
        default: function() {
          return [];
        },
        validator: function(value) {
          return value.filter((item) => {
            return (('label' in item) && ('value' in item));
          }).length === value.length;
        },
      },
    },

    data: () => ({
      hasError: false,
      checked: false,
      options: [],
      value: null,
    }),

    watch: {
      checked(value) {
        document.getElementById(this.id).checked = value;
      },

      value(newValue) {
        this.$emit('changed', newValue);

        this.validate();
      },
    },

    mounted() {
      if (this.startChecked) {
        this.checked = true;
      }
    },

    methods: {
      getValue() {
        return this.value;
      },

      setValue(value) {
        this.value = value;
      },

      clear() {
        this.value = null;
      },

      validate() {
        if (this.required && this.value === null) {
          this.hasError = true;
          return;
        }

        this.hasError = false;

        this.$emit("change", this.value);
      },

      computeItemId(index) {
        return `${this.id}-${index}`;
      },

      isItemDisabled(item) {
        return this.disabled || ('disabled' in item && item.disabled);
      },

      isItemChecked(item, index) {
        if (this.startValue === null) {
          return index === 0;
        }

        return item.value === this.startValue;
      },
    },
  };
</script>
