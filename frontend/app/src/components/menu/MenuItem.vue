<template>
  <li class="MenuItem">
    <a
      :title="description"
      :class="[
        { 'MenuItem-Link--current': active },
        `MenuItem-Link--${colorScheme}`,
      ]"
      class="MenuItem-Link"
      @click="openRoute"
    >{{ title }}</a>
  </li>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .MenuItem {
    flex: 0 1 auto;

    &-Link {
      &--current {
        font-weight: bold;
      }

      &--light {
        color: $foreground-light-color;

        &:hover {
          color: $foreground-tertiary-color;
          text-decoration: none;
        }

        &:active {
          color: $foreground-secondary-color;
        }
      }

      &--dark {
        color: black;
      }
    }
  }
</style>

<script>
  export default {

    props: {
      colorScheme: {
        type: String,
        default: "light",
        validator: function(value) {
          return ["light", "dark"].indexOf(value) !== -1;
        },
      },

      path: {
        type: String,
        default: "#",
      },

      name: {
        type: String,
        default: "self",
      },

      title: {
        type: String,
        default: "Self",
      },

      description: {
        type: String,
        default: "Clique para seguir o link",
      },
    },
    data() {
      return {
        active: false,
      };
    },

    watch: {
      $route(to) {
        this.active = to.path === this.path;
      },
    },

    methods: {
      openRoute(event) {
        event.preventDefault();

        if (this.path !== "#") {
          this.$router.push({ path: this.path }).catch(() => {});
        }

        this.$emit("link-open", this.name);
      },
    },
  };
</script>
