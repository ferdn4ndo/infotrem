<template>
  <ul 
    :class="{ 'MenuList--inline': inline }" 
    class="MenuList"
  >
    <menu-item
      v-for="(menu, key) in items"
      :class="{ 'MenuList-MenuItem--inline': inline }"
      :color-scheme="colorScheme"
      :description="menu.description"
      :inline="inline"
      :key="key"
      :name="menu.name"
      :title="menu.title"
      :path="menu.path"
      class="MenuList-MenuItem"
      @link-open="linkOpened(menu.name)"
    />
  </ul>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .MenuList {
    margin: 0;
    padding: 0;

    &--inline {
      display: flex;
      list-style-type: none;
      justify-content: center;
      flex-wrap: wrap;
    }

    &-MenuItem {
      flex: 0 1 auto;

      &--inline + &--inline:before {
        padding: 0 5px;
        content: "|";
      }

      &--light {
        color: $foreground-light-color;
      }

      &--dark {
        color: black;
      }
    }

    &-MenuLink {
      &--current {
        font-weight: bold;
      }

      &--light {
        color: $foreground-light-color;
      }

      &--dark {
        color: black;
      }
    }
  }
</style>

<script>
  import MenuItem from "@/components/menu/MenuItem";

  export default {
    components: {
      MenuItem,
    },

    props: {
      inline: {
        type: Boolean,
        default: false,
      },

      items: {
        type: Array,
        required: true,
      },

      colorScheme: {
        type: String,
        default: "light",
        validator: function(value) {
          return ["light", "dark"].indexOf(value) !== -1;
        },
      },
    },

    methods: {
      linkOpened(linkName) {
        this.$emit("link-opened", linkName);
      },
    },
  };
</script>
