<template>
  <footer class="TheFooter">
    <div class="TheFooter-Wrapper">
      <div class="TheFooter-Left">
        Copyright &copy; CSC Consultoria <br >
        CNPJ 13.337.870/0001-00
      </div>

      <div class="TheFooter-Right">
        <nav class="TheFooter-Menu">
          <menu-list 
            :items="menuItems" 
            :inline="true"
          />
        </nav>

        <div class="TheFooter-Credits">
          Feito com <the-icon 
            class="TheFooter-CreditsIcon" 
            icon="heart"
          /> por
          <a
            class="TheFooter-CreditsLink"
            href="https://fconstantino.me"
            title="Site do Fernando Constantino"
          >
            Fernando Constantino
          </a>
        </div>
      </div>
    </div>
  </footer>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .TheFooter {
    width: 100%;
    box-sizing: border-box;
    border-top: 1px solid $background-dark-border;
    background-color: $background-dark-color;
    line-height: 20px;
    color: $foreground-light-color;

    &-Wrapper {
      margin: 0 auto;
      box-sizing: border-box;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      padding: 5px;
      display: flex;
      max-width: $max-content-width;

      @media screen and (min-width: $desktop-breakpoint - 1) {
        flex-direction: row;
        justify-content: space-between;
      }
    }

    &-Left {
      flex: 0 0 auto;
      font-size: 12px;
    }

    &-Right {
      flex: 0 0 auto;
      display: flex;
      flex-direction: column;
      align-items: center;

      @media screen and (min-width: $desktop-breakpoint - 1) {
        align-items: flex-end;
      }
    }

    &-Credits {
      flex: 0 0 auto;
      font-size: 8px;
    }

    &-CreditsLink {
      color: $foreground-light-color;
      font-weight: bold;

      &:hover {
        color: $foreground-tertiary-color;
        text-decoration: none;
      }

      &:active {
        color: $foreground-secondary-color;
      }
    }

    &-CreditsIcon {
      padding: 0;
      font-size: 9px;
    }

    &-Menu {
      font-size: 14px;
    }
  }
</style>

<script>
  import { MENU_FOOTER } from "@/common/menus";
  import MenuList from "@/components/MenuList";
  import TheIcon from "@/components/TheIcon";

  export default {
    components: {
      MenuList,
      TheIcon,
    },

    data() {
      return {
        menuItems: MENU_FOOTER,
      };
    },
  };
</script>
