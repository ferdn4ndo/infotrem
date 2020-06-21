<template>
  <a class="icon-link" :href="this.url" target="_blank" :title="this.title">
    <an-icon :icon="this.icon" size="20pt"></an-icon>
  </a>
</template>

<style lang="scss" scoped>
  @import "@/styles/_variables.scss";

  .icon-link {
    text-decoration: none;
  }
</style>

<script>
  import ICON_CLASS_MAP from "../common/icons";
  import AnIcon from "@/components/AnIcon";

  export default {
    components: {
      AnIcon
    },

    props: {
      icon: {
        type: String,
        required: true,
        validator: function(value) {
          // The value must match one of the mapped icons
          return value in ICON_CLASS_MAP;
        }
      },

      url: {
        type: String,
        default: "#"
      },

      title: {
        type: String,
        required: true
      }
    }
  };
</script>
