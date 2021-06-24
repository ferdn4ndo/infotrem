<template>
  <fieldset
    :class="{ 'CheckboxField--hasError': hasError }"
    class="CheckboxField"
  >
    <input
      :class="{
        'CheckboxField-Input--hasError': hasError,
        'CheckboxField-Input--disabled': disabled,
        'CheckboxField-Input--checked': checked,
      }"
      :disabled="disabled"
      :id="id"
      :name="name"
      class="CheckboxField-Input"
      type="checkbox"
      @change="validate"
    >

    <label
      :class="{ 'CheckboxField--hasError': hasError }"
      :for="id"
      class="CheckboxField-Label"
    >
      {{ placeholder }}
    </label>

    <div class="CheckboxField-DescriptionBlock">
      <p
        v-if="!hasError"
        class="CheckboxField-Description"
      >
        {{ description }}
      </p>

      <p
        v-if="hasError"
        class="CheckboxField-Description CheckboxField--hasError"
      >
        {{ errorDescription }}
      </p>

      <p
        v-if="required"
        :class="{ 'CheckboxField--hasError': hasError }"
        class="CheckboxField-RequiredMark"
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

  .CheckboxField {
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
        /* check http://www.evotech.net/blog/2007/04/named-html-entities-in-numeric-order/ */
        content: '\2713';
        font-size: 19pt;
        font-weight: bold;
        position: absolute;
        top: -6px;
        left: -1px;
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
    name: "CheckboxField",

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

      placeholder: {
        type: String,
        default: "",
      },

      startChecked: {
        type: Boolean,
        default: false,
      },

      disabled: {
        type: Boolean,
        default: false,
      },

      required: {
        type: Boolean,
        default: false,
      },
    },

    data: () => ({
      hasError: false,
      checked: false,
    }),

    watch: {
      checked(value) {
        document.getElementById(this.id).checked = value;
      },
    },

    mounted() {
      if (this.startChecked) {
        this.checked = true;
      }
    },

    methods: {
      getValue() {
        return this.checked;
      },

      setValue(value) {
        this.checked = !!value;
      },

      clear() {
        this.checked = false;
      },

      validate() {
        let value = document.getElementById(this.id).checked;
        this.checked = !!value;

        if (this.required && !this.checked) {
          this.hasError = true;
          return;
        }

        this.hasError = false;

        this.$emit("change", this.checked);
      },
    },
  };
</script>
