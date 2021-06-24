<template>
  <fieldset
    :class="{ 'SelectField--hasError': hasError }"
    class="SelectField"
  >
    <label
      :class="{
        'SelectField-Label--hasText': inputText !== '',
        'SelectField--hasError': hasError,
      }"
      :for="id"
      class="SelectField-Label"
    >
      {{ placeholder }}
    </label>

    <div
      class="SelectField-DropdownIcon"
      @click="toggleDropdown"
    >
      <the-icon
        :class="{ 'SelectField-DropdownIcon--Rotated': displayDropdown }"
        icon="down"
        size="12pt"
      />
    </div>

    <input
      :class="{
        'SelectField--hasError': hasError,
        'SelectField-Input--disabled': disabled,
      }"
      :disabled="disabled"
      :id="id"
      :name="name"
      v-model="inputText"
      class="SelectField-Input"
      type="text"
      @click="toggleDropdown"
      @keyup="keyMonitor"
    >

    <div class="SelectField-DescriptionBlock">
      <p
        v-if="!hasError"
        class="SelectField-Description"
      >
        {{ description }}
      </p>

      <p
        v-if="hasError"
        class="SelectField-Description SelectField--hasError"
      >
        {{ errorDescription }}
      </p>

      <p
        v-if="required"
        :class="{ 'SelectField--hasError': hasError }"
        class="SelectField-RequiredMark"
        title="Campo obrigatório"
      >
        <the-icon
          icon="asterisk"
          size="12pt"
        />
      </p>
    </div>

    <ul
      v-show="displayDropdown"
      :id="`${name}_dropdown`"
      class="SelectField-DropdownList"
    >
      <li
        v-for="item in dropdownItems"
        :key="item.value"
        class="SelectField-DropdownItem"
        @click="setValue(item.value, $event)"
      >
        <a
          :title="`Selecionar opção '${item.text}'`"
          href="#"
          class="SelectField-DropdownItemOption"
          @click="setValue(item.value, $event)"
        >
          {{ item.text }}
        </a>
      </li>

      <li
        v-if="dropdownItems.length === 0"
        class="SelectField-DropdownItem"
        @click="setValue(null, $event)"
      >
        Nenhum resultado encontrado.
      </li>
    </ul>
  </fieldset>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .SelectField {
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

      &--hasText {
        font-weight: bold;
        cursor: default;
        font-size: 8pt;
        top: 0;
        left: 5px;
      }
    }

    &-DropdownIcon {
      position: absolute;
      top: 8px;
      right: 10px;
      font-size: 14pt;
      color: $color-text-gray;
      cursor: pointer;
      z-index: 888;

      -webkit-animation: spin 4s linear infinite;
      -moz-animation: spin 4s linear infinite;
      animation: spin 4s linear infinite;

      transition: transform 1s;
      transition-timing-function: linear;

      &--Rotated {
        transform: rotate(180deg);
      }
    }

    &-DropdownList {
      position: absolute;
      top: 42px;
      left: 0;
      width: 100%;
      background-color: $color-background-gray;

      list-style-type: none;
      margin-block-start: 0;
      margin-block-end: 0;
      margin-inline-start: 0;
      margin-inline-end: 0;
      padding-inline-start: 0;
      z-index: 999;

      max-height: 150px;
      overflow-x: hidden;
      overflow-y: scroll;
    }

    &-DropdownItem {
      display: block;
      word-wrap: break-word;
      padding: 0;
      margin: 0;
      box-sizing: border-box;
      color: $color-text-gray;

      &:hover {
        background-color: $color-primary-background-dark;
        color: $color-primary-foreground;
      }
    }

    &-DropdownItemOption {
      display: block;
      width: 100%;
      padding: 2px 10px;
      margin: 0;
      background-color: $color-background-gray;
      color: $color-text-gray;

      &:visited {
        background-color: $color-background-gray;
        color: $color-text-gray;
        text-decoration: none;
      }

      &:hover,
      &:active {
        background-color: $color-primary-background-dark;
        color: $color-primary-foreground;
        cursor: pointer;
        text-decoration: none;
      }
    }

    &-Input {
      width: 100%;
      height: 30px;
      background: none;
      border: none;
      border-bottom: 2px solid $color-primary-border;
      padding: 5px 5px;
      margin-top: 10px;
      box-sizing: border-box;
      font-size: 14pt;
      color: $color-text-black;
      outline: inherit;

      &--disabled {
        color: $color-text-gray;
        border-bottom: 2px solid $color-background-border;
      }

      &:hover {
        font-weight: bold;
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
    name: "SelectField",

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

      items: {
        type: Array,
        default: () => [
          {
            text: "Text 1",
            value: "text1",
          },
          {
            text: "Text 2",
            value: "text2",
          },
        ],
      },

      initialValue: {
        type: String,
        default: null,
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

      allowEmpty: {
        type: Boolean,
        default: false,
      },

      required: {
        type: Boolean,
        default: false,
      },

      maxLength: {
        type: Number,
        default: 1024,
      },
    },

    data: () => ({
      value: null,
      dropdownFocused: false,
      inputFocused: false,
      displayDropdown: false,
      dropdownItems: [],
      initialValueWasSet: false,
      inputText: "",
      errorDescription: "",
      hasError: false,
    }),

    watch: {
      items() {
        if (this.initialValue && !this.initialValueWasSet) {
          let filteredItems = this.items.filter(
            (item) => item.value === this.initialValue
          );

          if (filteredItems.length > 0) {
            this.setValue(this.initialValue);
            this.initialValueWasSet = true;
          }
        }

        this.filterDropdownItems(this.inputText);
      },
    },

    mounted() {
      this.dropdownItems = this.items;
    },

    methods: {
      changedValue() {
        this.hideDropdown();
        this.validate();
        this.$emit("change", this.value);
      },

      getValue() {
        return this.value;
      },

      validate() {
        if (this.required && this.value === null) {
          this.errorDescription = "Campo obrigatório.";
          this.hasError = true;
          return;
        }

        if (this.inputText !== "" && this.value === null) {
          this.errorDescription = "Valor inválido.";
          this.hasError = true;
          return;
        }

        this.errorDescription = "";
        this.hasError = false;
      },

      keyMonitor: function(event) {
        this.filterDropdownItems(this.inputText);

        if (this.dropdownItems.length > 0 && event.key === "Enter") {
          this.setValue(this.dropdownItems[0].value, event);
        } else if (this.dropdownItems.length === 0 && event.key === "Enter") {
          this.setValue(null, event);
        } else if (event.key === "Escape") {
          this.setValue(null, event);
          this.hideDropdown();
        } else {
          this.showDropdown();
        }
      },

      toggleDropdown() {
        if (this.displayDropdown) {
          this.hideDropdown();
        } else {
          this.showDropdown();
        }
      },

      setValue(value = null, event = null) {
        if (event !== null) {
          event.preventDefault();
        }

        if (value === this.value) {
          // no value changed
          this.hideDropdown();
          return;
        }

        if (value === null || value === undefined) {
          this.value = null;
          this.inputText = "";
          this.changedValue();
          return;
        }

        let filteredItems = this.items.filter((item) => item.value === value);

        if (filteredItems.length === 0) {
          if (this.value !== null) {
            this.value = null;
            this.changedValue();
          }

          return;
        }

        this.inputText = filteredItems[0].text;
        if (this.value !== filteredItems[0].value) {
          this.value = filteredItems[0].value;
          this.changedValue();
        }
      },

      clear() {
        if (this.value !== null) {
          this.value = null;
          this.inputText = "";
          this.$emit("change", this.value);
        }
        this.hideDropdown();
      },

      hideDropdown() {
        if (this.displayDropdown) {
          this.displayDropdown = false;
        }
      },

      showDropdown() {
        if (!this.displayDropdown) {
          this.displayDropdown = true;
        }
      },

      filterDropdownItems(query = null) {
        if (query === null || query === undefined || query.toString() === "") {
          this.dropdownItems = this.items;
          return;
        }

        this.dropdownItems = this.items.filter((item) => {
          const dropdownText = item.text
            .toLowerCase()
            .normalize("NFD")
            .replace(/[\u0300-\u036f]/g, "");

          const typedText = query
            .toLowerCase()
            .normalize("NFD")
            .replace(/[\u0300-\u036f]/g, "");

          return dropdownText.indexOf(typedText) > -1;
        });
      },
    },
  };
</script>
