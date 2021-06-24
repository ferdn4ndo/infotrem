<template>
  <fieldset
    :class="{ 'TextField--hasError': hasError }"
    class="TextField"
  >
    <label
      :class="{
        'TextField-Label--hasText': hasText,
        'TextField-Label--disabled': disabled,
        'TextField--hasError': hasError,
      }"
      :for="id"
      class="TextField-Label"
    >
      {{ placeholder }}
    </label>

    <!-- ToDo: extract textarea to a separated component! -->
    <textarea
      v-if="type === 'textarea'"
      :class="{
        'TextField--hasError': hasError,
        'TextField-Input--disabled': disabled,
      }"
      :disabled="disabled"
      :id="id"
      :name="name"
      :maxlength="maxLength"
      :rows="rows"
      v-model="value"
      class="TextField-Input"
      @change="validate"
      @keyup="keyMonitor"
      @focusout="validate"
    />

    <input
      v-mask="mask"
      v-else
      :type="type"
      :class="{
        'TextField--hasError': hasError,
        'TextField-Input--disabled': disabled,
      }"
      :maxlength="maxLength"
      :disabled="disabled"
      :id="id"
      :name="name"
      v-model="value"
      class="TextField-Input"
      style="height: 30px;"
      @change="validate"
      @keyup="keyMonitor"
      @focusout="validate"
    >

    <div class="TextField-DescriptionBlock">
      <p
        v-if="!hasError"
        class="TextField-Description"
      >
        {{ description }}
      </p>

      <p
        v-if="hasError"
        class="TextField-Description TextField--hasError"
      >
        {{ errorDescription }}
      </p>

      <p
        v-if="required"
        :class="{ 'TextField--hasError': hasError }"
        class="TextField-RequiredMark"
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

  .TextField {
    position: relative;
    border: none;
    margin: 0;
    padding: 0;

    -webkit-transition-property: font-size, left, top, color;
    -webkit-transition-duration: 0.5s;
    -webkit-transition-timing-function: ease-in-out;
    transition-property: font-size, left, top, color;
    transition-duration: 0.5s;
    transition-timing-function: ease-in-out;

    &-Label {
      position: absolute;
      top: 8px;
      left: 5px;
      font-size: 14pt;
      color: $color-text-gray;
      width: 100%;

      &:hover {
        cursor: text;
        font-weight: bold;
      }

      &--disabled {
        cursor: default;
        color: $color-text-gray;
      }

      &--disabled:hover {
        cursor: default;
        font-weight: normal;
      }

      &--hasText {
        font-weight: bold;
        cursor: default;
        font-size: 8pt;
        top: 0;
        left: 5px;
      }
    }

    &-Input {
      width: 100%;
      background: none;
      border: none;
      border-bottom: 2px solid $color-primary-border;
      padding: 5px 5px;
      margin-top: 10px;
      box-sizing: border-box;
      font-size: 14pt;
      color: $color-text-black;
      outline: inherit;

      &:hover {
        font-weight: bold;
      }

      &--disabled {
        cursor: default;
        color: $color-text-gray;
        border-bottom: 2px solid $color-background-border;
      }

      &--disabled:hover {
        cursor: default;
        font-weight: normal;
      }
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

    &-RequiredMark {
      flex: 0 0 auto;
      display: inline-block;
      font-size: 12pt;
      color: $color-text-gray;
      right: 0;
      margin: 0;
      margin-block-start: 0;
      margin-block-end: 0;
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
    name: "TextField",

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

      type: {
        type: String,
        default: "text",
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

      castEmptyToNull: {
        type: Boolean,
        default: true,
      },

      regexValidator: {
        type: RegExp,
        default: null,
      },

      rows: {
        type: Number,
        default: 5,
      },

      mask: {
        type: String | Array,
        default: "",
      },

      maxLength: {
        type: Number,
        default: 1024,
      },
    },

    data: () => ({
      value: "",
      errorDescription: "",
      hasError: false,
      hasText: false,
    }),

    watch: {
      disabled() {
        if (this.disabled) {
          this.hasError = false;
        }
      },

      value() {
        this.hasText = this.value !== "" && this.value !== null;
      },
    },

    methods: {
      keyMonitor: function(event) {
        if (this.hasError) {
          this.validate();
        }

        this.$emit("keyup", event);
      },

      getValue() {
        if (this.value === "" && this.castEmptyToNull) {
          return null;
        }

        return this.value;
      },

      setValue(newValue) {
        if (newValue !== this.value) {
          this.value = newValue;
          document.getElementById(this.id).value = newValue;
          this.validate();
          this.$emit("change", this.value);
        }
      },

      clear() {
        if (this.value !== "" && this.value !== null) {
          this.value = "";
          document.getElementById(this.id).value = "";
          this.$emit("change", this.value);
        }
      },

      validate() {
        let value = document.getElementById(this.id).value;

        if (this.required && (value === "" || value === null)) {
          this.errorDescription = "Campo obrigatório.";
          this.hasError = true;
          return;
        }

        if (this.regexValidator && value !== "" && value !== null) {
          let matcher = new RegExp(this.regexValidator, "g");
          if (!matcher.test(value)) {
            this.errorDescription = "Valor inválido.";
            this.hasError = true;
            return;
          }
        }

        if (value !== this.value) {
          this.$emit("change", this.value);
        }

        this.errorDescription = "";
        this.hasError = false;
      },
    },
  };
</script>
