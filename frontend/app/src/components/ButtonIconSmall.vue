<template>
  <the-button 
    class="ButtonIconSmall-Button" 
    @click="$emit('click', $event)"
  >
    <the-icon 
      v-if="showIcon" 
      :icon="icon" 
      class="ButtonIconSmall-Icon"
    />

    <slot>
      {{ text }}
    </slot>
  </the-button>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .ButtonIconSmall {
    &-Button {
      padding: 0 0 3px 0;
      font-size: 14pt;
    }

    &-Icon {
      margin: 10px 10px 0 0;
      font-size: 14pt;
    }
  }
</style>

<script>
  import TheButton from "@/components/TheButton";
  import TheIcon from "@/components/TheIcon";

  export default {
    components: { TheIcon, TheButton },

    props: {
      icon: {
        type: String,
        default: "",
      },

      text: {
        type: String,
        default: "",
      },
    },

    computed: {
      showIcon() {
        return (
          this.icon !== "" && typeof this.icon !== "undefined" && this.icon
        );
      },
    },
  };
</script>
