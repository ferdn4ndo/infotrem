<template>
  <section class="CollapseBlock">
    <header
      :class="{ 'CollapseBlock-Header--expanded': expanded }"
      class="CollapseBlock-Header"
      @click="toggleState"
    >
      <the-icon 
        v-if="icon !== null" 
        class="CollapseBlock-Icon" 
        icon="icon"
      />

      <h1 class="CollapseBlock-Title">{{ title }}</h1>

      <div
        :class="{ 'CollapseBlock-CollapseIconWrapper--expanded': expanded }"
        class="CollapseBlock-CollapseIconWrapper"
      >
        <the-icon 
          class="CollapseBlock-CollapseIcon" 
          icon="expand_down"
        />
      </div>
    </header>

    <div
      :class="{ 'CollapseBlock-Content--expanded': expanded }"
      class="CollapseBlock-Content"
    >
      <slot />
    </div>
  </section>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .CollapseBlock {
    &-Header {
      cursor: pointer;
      display: flex;
      padding: 10px 15px;
      box-sizing: border-box;
      color: $foreground-light-color;
      background-color: $background-dark-color;
      border-bottom: 1px solid $background-dark-border;
      border-top-left-radius: 5px;
      border-top-right-radius: 5px;
    }

    &-Icon {
      font-size: 14pt;
      margin-right: 10px;
    }

    &-Title {
      font-size: 14pt;
      font-weight: bold;
      margin: 0;
      padding: 0;
    }

    &-CollapseIconWrapper {
      padding-top: 3px;
      margin-left: auto;
      transform: rotate(0deg);
      transition: transform 0.25s ease-out;
      transform-origin: 50% 50%;

      &--expanded {
        transform: rotate(180deg);
        transition: transform 0.25s ease-in;
      }
    }

    &-CollapseIcon {
      font-size: 12pt;
    }

    &-Content {
      background-color: $background-secondary-color;
      border: 1px solid $background-secondary-border;
      border-top: none;
      box-sizing: border-box;
      max-height: 0;
      overflow: hidden;
      transition: max-height 0.55s cubic-bezier(0, 1.05, 0, 1);

      &--expanded {
        max-height: 99999px;
        transition: max-height 0.55s cubic-bezier(1, 0.01, 0.58, 0.99);
      }
    }
  }
</style>

<script>
  import TheIcon from "@/components/TheIcon";

  export default {
    components: {
      TheIcon,
    },

    props: {
      icon: {
        type: String,
        default: null,
      },

      title: {
        type: String,
        required: true,
      },

      startExpanded: {
        type: Boolean,
        default: false,
      },
    },

    data() {
      return {
        expanded: false,
      };
    },

    mounted() {
      if (this.startExpanded) {
        this.expanded = true;
      }
    },

    methods: {
      toggleState() {
        this.expanded = !this.expanded;
      },
    },
  };
</script>
