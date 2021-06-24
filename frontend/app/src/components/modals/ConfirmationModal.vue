<template>
  <the-modal
    :title="title"
    :visible="visible"
    :small="true"
    class="ConfirmationModal"
    @close="$emit('close')"
  >
    <div class="ConfirmationModal-Body">
      <div 
        v-if="showIcon" 
        class="ConfirmationModal-IconWrapper"
      >
        <the-icon 
          :icon="icon" 
          class="ConfirmationModal-Icon"
        />
      </div>

      <div class="ConfirmationModal-Content">
        <slot>
          <div v-html="message" />
        </slot>
      </div>

      <div class="ConfirmationModal-Actions">
        <the-button
          :text="confirmButtonText"
          class="ConfirmationModal-Button"
          styling="secondary"
          @click="$emit('confirm', $event)"
        />

        <the-button
          :text="cancelButtonText"
          class="ConfirmationModal-Button"
          styling="primary"
          @click="$emit('close', $event)"
        />
      </div>
    </div>
  </the-modal>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .ConfirmationModal {
    &-Body {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
    }

    &-IconWrapper {
      text-align: center;
      flex: 1 1 100%;
      height: 100px;
      padding: 20px;
      display: flex;
      justify-content: center;
      align-items: center;

      @media screen and (min-width: $tablet-breakpoint - 1) {
        flex: 0 0 100px;
      }
    }

    &-Icon {
      font-size: 60pt;
      color: $foreground-dark-color;
    }

    &-Content {
      flex: 1 1 100%;
      font-size: 14pt;
      padding: 10px;
      text-align: center;
      min-height: 100px;
      display: flex;
      justify-content: center;
      align-items: center;

      @media screen and (min-width: $tablet-breakpoint - 1) {
        flex: 1 1 auto;
      }
    }

    &-Actions {
      flex: 1 1 100%;
      text-align: right;
      border-top: 1px solid $color-background-border;
      padding-top: 20px;
    }

    &-Button {
      display: inline-block;
      max-width: 200px;
      margin-right: 20px;
    }

    &-TableWrapper {
      width: 100%;
      padding: 10px;
      box-sizing: border-box;
    }

    &-Table {
      width: 100%;
    }
  }
</style>

<script>
  import TheModal from "@/components/modals/TheModal";
  import ICON_CLASS_MAP from "@/common/icons";
  import TheIcon from "@/components/TheIcon";
  import TheButton from "@/components/TheButton";

  export default {
    components: { TheButton, TheIcon, TheModal },

    props: {
      visible: {
        type: Boolean,
        default: false,
      },

      title: {
        type: String,
        default: "Tem certeza?",
      },

      message: {
        type: String,
        default: "Deseja realmente continuar?",
      },

      icon: {
        type: String,
        default: "question",
        validator: (icon) => {
          return icon === "" || icon in ICON_CLASS_MAP;
        },
      },

      confirmButtonText: {
        type: String,
        default: "Sim, executar",
      },

      cancelButtonText: {
        type: String,
        default: "Não, cancelar",
      },
    },

    computed: {
      showIcon() {
        return this.icon !== "";
      },
    },
  };
</script>
