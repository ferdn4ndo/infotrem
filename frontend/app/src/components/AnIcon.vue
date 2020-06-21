<template>
  <span class="an-icon" :style="{'font-size': size}">
    <i :class="iconClass"></i>
  </span>
</template>

<style lang="scss" scoped>
  @import "@/styles/_variables.scss";

  .an-icon {
    font-size: 24pt;
    font-weight: 800;

    padding: 0 7px;

    @media screen and (min-width: $desktop-breakpoint) {
      padding: 0 10px;
    }
  }
</style>

<script>
  import ICON_CLASS_MAP from "../common/icons";

  export default {
    props: {
      icon: {
        type: String,
        required: true,
        validator: function(value) {
          // The value must match one of the mapped icons
          return value in ICON_CLASS_MAP;
        }
      },

      size: {
        type: String,
        default: "24pt",
      }
    },

    computed: {
      iconClass() {
        return ICON_CLASS_MAP[this.icon];
      }
    }
  };
</script>
