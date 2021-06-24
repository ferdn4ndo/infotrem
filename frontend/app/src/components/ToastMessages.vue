<template>
  <div class="ToastMessages">
    <transition-group
      name="ToastMessages-ToastEffect"
      tag="div"
      class="ToastMessages-Wrapper"
    >
      <div
        v-for="message in messages"
        :class="`ToastMessages-Styles--${message.style}`"
        :key="message.id"
        class="ToastMessages-Message"
      >
        <the-icon 
          :icon="message.icon" 
          class="ToastMessages-MessageIcon"
        />

        <p 
          class="ToastMessages-MessageText" 
          v-html="message.text"
        />

        <a
          v-if="message.closeable"
          class="ToastMessages-MessageCloseLink"
          href="#"
          @click="clickToRemoveMessage(message, $event)"
        >
          &times;
        </a>
      </div>
    </transition-group>
  </div>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .ToastMessages {
    z-index: 9999;
    position: fixed;
    height: 0;
    width: 100%;
    overflow: visible;

    &-Wrapper {
      box-sizing: border-box;
      margin: 10px;
    }

    &-Message {
      margin: 0 0 10px 0;
      width: 100%;
      display: flex;
      align-items: center;
      background-color: $color-primary-background-mid;
      color: $color-primary-foreground;
      border: 1px solid $color-primary-border;
      border-radius: 5px;
      box-sizing: border-box;
      box-shadow: 1px 1px 3px $color-shadow;
    }

    &-MessageIcon {
      flex: 0 0 auto;
      margin: 2px 10px;
      font-size: 13pt;
      font-weight: bold;
    }

    &-MessageText {
      margin: 0;
      padding: 10px 5px;
      flex: 1 1 auto;
      font-size: 12pt;
    }

    &-MessageCloseLink {
      flex: 0 0 auto;
      font-size: 20pt;
      padding: 2px 10px;
      margin-left: auto;
      color: inherit;

      &:hover {
        text-decoration: none;
      }
    }

    &-ToastEffect {
      &-item {
        display: inline-block;
        margin-right: 10px;
      }

      &-enter-active,
      &-leave-active {
        transition: all 0.666s;
      }

      &-enter, &-leave-to /* .list-leave-active below version 2.1.8 */ {
        opacity: 0;
        transform: translateY(30px);
      }
    }

    &-Styles {
      &--error {
        background-color: $color-background-error;
        color: $color-primary-foreground;
        border-color: $color-border-error;
      }

      &--info,
      &--question {
        background-color: $color-background-info;
        color: $color-primary-foreground;
        border-color: $color-border-info;
      }

      &--warning {
        background-color: $color-border-warning;
        color: $color-primary-foreground;
        border-color: $color-border-warning;
      }

      &--success {
        background-color: $color-border-success;
        color: $color-primary-foreground;
        border-color: $color-border-success;
      }
    }
  }
</style>

<script>
  import ICON_CLASS_MAP from "../common/icons";
  import TheIcon from "@/components/TheIcon";

  export default {
    components: { TheIcon },

    props: {},

    data() {
      return {
        messages: [],
      };
    },

    computed: {
      iconClass() {
        return ICON_CLASS_MAP[this.icon];
      },
    },

    methods: {
      addMessage(
        text,
        style = "info",
        icon = "auto",
        expSecs = 5,
        closeable = true
      ) {
        let message = {
          id: Math.random(),
          text: text,
          icon: this.getIcon(icon, style),
          style: style,
          expSecs: expSecs,
          closeable: closeable,
        };

        this.messages.push(message);

        if (expSecs > 0) {
          setTimeout(() => this.removeMessage(message), expSecs * 1000);
        }
      },

      clickToRemoveMessage(messageToBeRemoved, event) {
        this.removeMessage(messageToBeRemoved);

        event.preventDefault();
      },

      removeMessage(messageToBeRemoved) {
        this.messages = this.messages.filter((message) => {
          return message.id !== messageToBeRemoved.id;
        });
      },

      getIcon(icon, style) {
        if (icon === "auto") {
          // auto means it'll guess from the style
          if (
            ["success", "question", "info", "warning", "error"].indexOf(
              style
            ) !== -1
          ) {
            return style;
          }
        }

        return icon;
      },
    },
  };
</script>
