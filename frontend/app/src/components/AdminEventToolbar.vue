<template>
  <nav class="AdminEventToolbar">
    <the-button 
      class="AdminEventToolbar-Button" 
      @click="openGeneralInfo()"
    >
      <the-icon 
        class="AdminEventToolbar-Icon" 
        icon="map"
      />
      Informações Gerais
    </the-button>

    <the-button 
      class="AdminEventToolbar-Button" 
      @click="openFiles()"
    >
      <the-icon 
        class="AdminEventToolbar-Icon" 
        icon="files"
      />
      Arquivos
    </the-button>

    <the-button 
      class="AdminEventToolbar-Button" 
      @click="openLinks()"
    >
      <the-icon 
        class="AdminEventToolbar-Icon" 
        icon="globe"
      />
      Links
    </the-button>

    <the-button 
      class="AdminEventToolbar-Button" 
      @click="openSubscriptions()"
    >
      <the-icon 
        class="AdminEventToolbar-Icon" 
        icon="users"
      />
      Inscrições
    </the-button>
  </nav>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .AdminEventToolbar {
    width: 100%;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    box-sizing: border-box;
    padding: 20px;

    &-Button {
      flex: 1 1 100%;
      margin: 10px;
      text-align: center;
      box-sizing: border-box;

      @media screen and (min-width: $tablet-breakpoint - 1) {
        flex: 1 1 20%;
        max-width: 50%;
      }
    }

    &-Icon {
      display: block;
      margin: 10px;
      font-size: 22pt;
    }
  }
</style>

<script>
  import TheTitle from "@/components/TheTitle";
  import TheButton from "@/components/TheButton";
  import TheIcon from "@/components/TheIcon";

  export default {
    name: "AdminEventToolbar",

    components: {
      TheIcon,
      TheButton,
      TheTitle,
    },

    props: {
      event: {
        type: Object,
        required: true,
      },
    },

    methods: {
      openGeneralInfo() {
        this.$router.push({
          name: "admin-event-detail",
          params: { event_id: this.event.id },
        });
      },

      openFiles() {
        this.$router.push({
          name: "admin-event-files",
          params: { event_id: this.event.id },
        });
      },

      openLinks() {
        this.$router.push({
          name: "admin-event-links",
          params: { event_id: this.event.id },
        });
      },

      openSubscriptions() {
        this.$router.push({
          name: "admin-event-subscriptions",
          params: { event_id: this.event.id },
        });
      },
    },
  };
</script>
