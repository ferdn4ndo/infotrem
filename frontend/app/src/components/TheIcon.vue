<script setup>
  import { ref, computed } from "vue"
  import ICON_CLASS_MAP from "../common/icons";

  const icons = ICON_CLASS_MAP;

  defineProps({
    icon: {
      type: String,
      required: true,
      validator: function(value) {
        // The value must match one of the mapped icons
        return value in ICON_CLASS_MAP;
      },
    },
  });

  const getIconClass = computed(() => ICON_CLASS_MAP[this.icon]);
</script>

<template>
  <i
    :class="getIconClass"
    class="TheIcon"
  />
</template>

<style scoped>
  .TheIcon {
    display: inline-block;
  }
</style>
