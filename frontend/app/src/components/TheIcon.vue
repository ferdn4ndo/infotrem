<template>
  <i 
    :class="iconClass" 
    class="TheIcon"
  />
</template>

<style lang="scss" scoped>
  .TheIcon {
  }
</style>

<script>
  import ICON_CLASS_MAP from "@/common/icons";

  export default {
    props: {
      icon: {
        type: String,
        required: true,
        validator: function(value) {
          // The value must match one of the mapped icons
          return value in ICON_CLASS_MAP;
        },
      },
    },

    computed: {
      iconClass() {
        return ICON_CLASS_MAP[this.icon];
      },
    },
  };
</script>
