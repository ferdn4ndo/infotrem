<template>
  <div 
    :class="`StatusItem--${status}`" 
    class="StatusItem"
  >
    <the-icon 
      :icon="status" 
      class="StatusItem-Icon"
    />

    <div class="StatusItem-Data">
      <h3 class="StatusItem-Title">{{ title }}</h3>

      <div class="StatusItem-Description">
        <slot>
          {{ description }}
        </slot>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .StatusItem {
    display: flex;
    padding: 10px;

    &-Icon {
      height: 50px;
      font-size: 48px;
      flex: 0 0 auto;
    }

    &-Data {
      margin-left: 10px;
      flex: 1 1 auto;
    }

    &-Title {
      padding: 0;
      margin: 0;
      font-size: 16px;
      font-weight: bold;
    }

    &-Description {
      font-size: 14px;
      padding: 0;
      margin: 0;
    }

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
</style>

<script>
  import TheIcon from "@/components/TheIcon";

  export default {
    name: "StatusItem",

    components: { TheIcon },

    props: {
      description: {
        type: String,
        required: false,
        default: "",
      },

      status: {
        type: String,
        required: true,
        validator: function(value) {
          return (
            ["success", "question", "info", "warning", "error"].indexOf(
              value
            ) !== -1
          );
        },
      },

      title: {
        type: String,
        required: true,
      },
    },
  };
</script>
