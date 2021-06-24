<template>
  <dl 
    :class="`DateIndicator-Styling--${styling}`" 
    class="DateIndicator"
  >
    <dt 
      class="DateIndicator-Title" 
      v-html="title"
    />

    <dd class="DateIndicator-DateBlock">
      <div 
        v-if="icon" 
        class="DateIndicator-Icon"
      >
        <the-icon :icon="icon" />
      </div>

      <time 
        :datetime="date" 
        class="DateIndicator-Date"
      >
        {{ date | date }}
      </time>
    </dd>
  </dl>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .DateIndicator {
    margin-block-start: 0;
    margin-block-end: 0;

    &-Styling {
      color: $foreground-dark-color;

      &--normal {
        color: $color-date-normal;
      }

      &--initial {
        color: $color-date-initial;
      }

      &--final {
        color: $color-date-final;
      }
    }

    &-Title {
      font-size: 16px;
      font-weight: lighter;
      text-transform: uppercase;
      margin-bottom: 5px;
    }

    &-DateBlock {
      font-weight: bold;
      margin-inline-start: 0;
      margin-bottom: 5px;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    &-Icon {
      flex: 0 0 auto;
      font-size: 22px;
    }

    &-Date {
      font-size: 22px;
      margin-left: 10px;
    }
  }
</style>

<script>
  import ICON_CLASS_MAP from "@/common/icons";
  import TheIcon from "@/components/TheIcon";

  export default {
    components: { TheIcon },
    props: {
      date: {
        type: String,
        required: true,
      },

      title: {
        type: String,
        required: true,
      },

      styling: {
        type: String,
        default: "normal",
        validator: function(value) {
          return ["normal", "initial", "final"].indexOf(value) !== -1;
        },
      },

      icon: {
        type: String,
        default: "calendar",
        validator: function(value) {
          // The value must match one of the mapped icons
          return value in ICON_CLASS_MAP;
        },
      },
    },
  };
</script>
