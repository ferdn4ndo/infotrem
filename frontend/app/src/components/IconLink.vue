<template>
  <a
    :href="url"
    :title="title"
    class="icon-link"
    target="_blank"
  >
    <an-icon
      :icon="icon"
      size="20pt"
    />
  </a>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .icon-link {
    text-decoration: none;
  }
</style>

<script>
  import ICON_CLASS_MAP from "../common/icons";
  import AnIcon from "@/components/TheIcon";

  export default {
    components: {
      AnIcon,
    },

    props: {
      icon: {
        type: String,
        required: true,
        validator: function(value) {
          // The value must match one of the mapped icons
          return value in ICON_CLASS_MAP;
        },
      },

      url: {
        type: String,
        default: "#",
      },

      title: {
        type: String,
        required: true,
      },
    },
  };
</script>
