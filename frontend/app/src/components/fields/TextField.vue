<script setup>
  import { ref } from "vue"
  import TheIcon from "../TheIcon.vue";

  const props = defineProps({
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
      type: [String, Array],
      default: "",
    },

    maxLength: {
      type: Number,
      default: 1024,
    },
  });

  const emits = defineEmits(["keyup", "change"])

  const fieldValue = ref("");
  const errorDescription = ref("");
  const hasError = ref(false);
  const hasText = ref(false);

  const keyMonitor = (event) => {
    if (hasError.value === true) {
      this.validate();
    }

    emits("keyup", event);
  }

  const getValue = () => {
    if (fieldValue.value === "" && props.castEmptyToNull) {
      return null;
    }

    return fieldValue;
  }

  const setValue = (newValue) => {
    if (newValue !== fieldValue.value) {
      fieldValue.value = newValue;
      document.getElementById(props.id).value = newValue;
      validate();
      emits("change", this.value);
    }
  }

  const clear = () => {
    if (fieldValue.value !== "" && fieldValue.value !== null) {
      fieldValue.value = "";
      document.getElementById(props.id).value = "";
      emits("change", fieldValue.value);
    }
  }

  const setError = (msg) => {
    if (msg === "" || msg === null || typeof msg === "undefined") {
      errorDescription.value = "";
      hasError.value = false;

      return;
    }

    errorDescription.value = msg;
    hasError.value = true;
  }

  const validate = () => {
    let value = document.getElementById(props.id).value;

    if (props.required && (value === "" || value === null)) {
      setError("Campo obrigatório.");

      return;
    }

    if (props.regexValidator && value !== "" && value !== null) {
      let matcher = new RegExp(props.regexValidator, "g");
      if (!matcher.test(value)) {
        setError("Valor inválido.");

        return;
      }
    }

    if (value !== fieldValue.value) {
      //emits("change", fieldValue.value);
    }

    setError(null);
  }

</script>

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

    <input
      :id="id"
      v-model="fieldValue"
      v-maska="mask"
      :type="type"
      :class="{
        'TextField--hasError': hasError,
        'TextField-Input--disabled': disabled,
      }"
      :maxlength="maxLength"
      :disabled="disabled"
      :name="name"
      class="TextField-Input"
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

<style scoped>
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
      text-align: left;
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
      height: 30px;
      border: none;
      text-align: left;
      background-color: var(--background-color-light);
      border-bottom: 2px solid var(--border-color-secondary);
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
