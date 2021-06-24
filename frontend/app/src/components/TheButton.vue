<template>
  <button
    :class="getClasses()"
    :disabled="disabled"
    :style="`width: ${width};`"
    :type="type"
    class="CscButton"
    @click="click"
  >
    <slot>
      {{ text }}
    </slot>
  </button>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .CscButton {
    background: none;
    color: inherit;
    border: none;
    padding: 5px;
    font: inherit;
    font-size: 16pt;
    font-weight: bold;
    cursor: pointer;
    outline: inherit;
    border-radius: 5px;
    display: block;
    box-sizing: border-box;

    &--info,
    &--primary {
      background: $color-button-primary-background;
      border: 1px solid $color-button-primary-border;
      color: $color-button-primary-foreground;

      &:hover {
        background: $color-button-primary-hover;
      }

      &:active {
        background: $color-button-primary-active;
      }

      &--clicked {
        background: $color-button-primary-clicked;
      }
    }

    &--secondary {
      background: $color-button-secondary-background;
      border: 1px solid $color-button-secondary-border;
      color: $color-button-secondary-foreground;

      &:hover {
        background: $color-button-secondary-hover;
      }

      &:active {
        background: $color-button-secondary-active;
      }

      &--clicked {
        background: $color-button-secondary-clicked;
      }
    }

    &--error,
    &--danger {
      background: $color-button-danger-background;
      border: 1px solid $color-button-danger-border;
      color: $color-button-danger-foreground;

      &:hover {
        background: $color-button-danger-hover;
      }

      &:active {
        background: $color-button-danger-active;
      }

      &--clicked {
        background: $color-button-danger-clicked;
      }
    }

    &--disabled {
      cursor: default;
      background: $color-button-disabled-background;
      border: 1px solid $color-button-disabled-border;
      color: $color-button-disabled-foreground;

      &--clicked {
        background: $color-button-disabled-clicked;
      }
    }
  }
</style>

<script>
  export default {
    props: {
      text: {
        type: String,
        default: "",
      },

      type: {
        type: String,
        default: "button",
        validator: function(value) {
          return ["button", "submit", "reset"].indexOf(value) !== -1;
        },
      },

      styling: {
        type: String,
        default: "primary",
        validator: function(value) {
          return ["primary", "secondary", "danger"].indexOf(value) !== -1;
        },
      },

      clicked: {
        type: Boolean,
        default: false,
      },

      disabled: {
        type: Boolean,
        default: false,
      },

      width: {
        type: String,
        default: "100%",
      },
    },

    methods: {
      click() {
        if (!this.disabled) {
          this.$emit("click");
        }
      },

      getClasses() {
        let classes = [];
        let clickedStyling = "";

        if (this.disabled) {
          classes.push(`CscButton--disabled`);
          clickedStyling = "disabled";
        } else {
          classes.push(`CscButton--${this.styling}`);
          clickedStyling = this.styling;
        }

        if (this.clicked) {
          classes.push(`CscButton--${clickedStyling}--clicked`);
        }

        return classes;
      },
    },
  };
</script>
