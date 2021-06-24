<template>
  <article class="CscEventsList">
    <header-background
      :image-src="headerImageSrc"
      :title="typeName"
      class="CscEventsList-Header"
    />

    <section class="CscEventsList-Section">
      <the-title>Inscri&ccedil;&otilde;es abertas ({{ eventsOpenCount }})</the-title>

      <div class="CscEventsList-CardList">
        <div
          v-for="event in eventsOpen"
          :key="event.id"
          class="CscEventsList-CardWrapper"
        >
          <event-card
            :event="event"
            class="CscEventsList-Card"
          />
        </div>
      </div>
    </section>

    <section class="CscEventsList-Section">
      <the-title>Em Andamento ({{ eventsOngoingCount }})</the-title>

      <div class="CscEventsList-CardList">
        <div
          v-for="event in eventsOngoing"
          :key="event.id"
          class="CscEventsList-CardWrapper"
        >
          <event-card
            :event="event"
            class="CscEventsList-Card"
          />
        </div>
      </div>
    </section>

    <section class="CscEventsList-Section">
      <the-title>Finalizados ({{ eventsClosedCount }})</the-title>

      <div class="CscEventsList-CardList">
        <div
          v-for="event in eventsClosed"
          :key="event.id"
          class="CscEventsList-CardWrapper"
        >
          <event-card
            :event="event"
            class="CscEventsList-Card"
          />
        </div>
      </div>
    </section>
  </article>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .CscEventsList {
    &-Header {
    }

    &-Section {
      margin: 20px 0;
    }

    &-CardList {
      width: 100%;
      display: flex;
      flex-wrap: wrap;
      //justify-content: space-around;
    }

    &-CardWrapper {
      box-sizing: border-box;
      min-width: 300px;
      max-width: 100%;
      flex: 1 1 auto;
      padding: 10px;

      @media screen and (min-width: $mobile-breakpoint - 1) {
        max-width: 50%;
      }

      @media screen and (min-width: $desktop-breakpoint - 1) {
        max-width: 33%;
      }
    }

    &-Card {
      margin: 0;
    }
  }
</style>

<script>
  import { mapGetters } from "vuex";
  import TheTitle from "@/components/TheTitle";
  import EventCard from "@/components/EventCard";
  import { FETCH_EVENTS } from "@/store/actions.type";
  import HeaderBackground from "../components/HeaderBackground";

  export default {
    name: "Events",

    components: {
      HeaderBackground,
      EventCard,
      TheTitle,
    },

    computed: {
      ...mapGetters([
        "isAuthenticated",
        "eventsOpenCount",
        "eventsOngoingCount",
        "eventsClosedCount",
        "eventsTotalCount",
        "eventsOpen",
        "eventsOngoing",
        "eventsClosed",
        "isLoading",
      ]),

      typeName() {
        switch (this.$route.query.type) {
          case "PROC_SELETIVO":
            return "Processos Seletivos";
          case "CONCURSO":
            return "Concursos";
          default:
            return "Todos os Eventos";
        }
      },

      headerImageSrc() {
        switch (this.$route.query.type) {
          case "PROC_SELETIVO":
            return "/img/backgrounds/csc-01.jpg";
          case "CONCURSO":
            return "/img/backgrounds/csc-02.jpg";
          default:
            return "/img/backgrounds/csc-03.jpg";
        }
      },
    },

    mounted() {
      this.$store.dispatch(FETCH_EVENTS, { type: this.$route.query.type });
    },
  };
</script>
