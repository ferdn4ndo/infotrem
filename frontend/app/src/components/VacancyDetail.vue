<template>
  <the-card class="VacancyDetail">
    <header class="VacancyDetail-Header">
      <h1 class="VacancyDetail-HeaderText">
        {{ vacancy.job_title }}
      </h1>
    </header>

    <section class="VacancyDetail-Data">
      <div class="VacancyDetail-DataLine">
        <h2 class="VacancyDetail-DataTitle">Total de vagas:</h2>

        <p class="VacancyDetail-DataInfo">
          {{ vacancy.total_vacancies | vacancy }}
        </p>
      </div>

      <div class="VacancyDetail-DataLine">
        <h2 class="VacancyDetail-DataTitle">
          Valor da inscri&ccedil;&atilde;o:
        </h2>

        <p class="VacancyDetail-DataInfo">
          {{ vacancy.subscription_price | currency }}
        </p>
      </div>
    </section>

    <section class="VacancyDetail-Actions">
      <div 
        v-if="isSubscribedToVacancy(vacancy)" 
        class="VacancyDetail-Action"
      >
        <the-button text="Minha inscrição"/>
      </div>

      <div 
        v-if="allowSubscription(vacancy)" 
        class="VacancyDetail-Action"
      >
        <the-button
          text="Inscrever-se!"
          @click="subscribe(vacancy, $event)"
        />
      </div>
    </section>
  </the-card>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .VacancyDetail {
    display: flex;
    box-sizing: border-box;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: center;

    &-Header {
      flex: 0 0 100%;
      padding: 5px 15px;
      text-align: left;
      box-sizing: border-box;
      border-top-left-radius: 5px;
      border-top-right-radius: 5px;
      color: $foreground-dark-color;
      background-color: $background-tertiary-color;
      border-bottom: 1px solid $background-tertiary-border;
      min-height: 40px;
      display: flex;
    }

    &-HeaderText {
      align-self: center;
      font-size: 14pt;
      font-weight: bold;
      margin: 0;
    }

    &-Data {
      flex: 0 0 100%;
      box-sizing: border-box;

      @media screen and (min-width: $mobile-breakpoint - 1) {
        flex: 1 1 50%;
      }
    }

    &-Actions {
      flex: 0 0 100%;
      box-sizing: border-box;

      @media screen and (min-width: $mobile-breakpoint - 1) {
        flex: 1 1 20%;
      }
    }

    &-DataLine {
      margin: 5px 10px 10px;
    }

    &-DataTitle {
      display: inline-block;
      padding: 0;
      font-weight: bold;
      font-size: 13pt;
      margin: 0 5px 0 0;
    }

    &-DataInfo {
      display: inline-block;
      margin: 0;
      padding: 0;
      font-size: 13pt;
    }

    &-Action {
      box-sizing: border-box;
      width: 100%;
      padding: 10px;
    }
  }
</style>

<script>
  import TheCard from "@/components/TheCard";
  import TheButton from "@/components/TheButton";

  export default {
    components: {
      TheButton,
      TheCard,
    },

    props: {
      event: {
        type: Object,
        required: true,
      },

      vacancy: {
        type: Object,
        required: true,
      },
    },

    data: () => ({}),

    mounted() {
      this.updateVacancyGroups();
    },

    methods: {
      hasDescription() {
        return this.event.description && this.event.description !== "";
      },

      hasNotice() {
        return this.event.notice_text && this.event.notice_text !== "";
      },

      updateVacancyGroups() {
        this.vacancyGroups = this.event.vacancies.reduce((accum, vacancy) => {
          let groupName =
            vacancy.type !== null ? vacancy.type.name : "Todos os Níveis";

          if (!(groupName in accum)) {
            accum[groupName] = [];
          }

          accum[groupName].push(vacancy);
          return accum;
        }, {});
      },

      isSubscribedToVacancy(vacancy) {
        // ToDo: get from subscription module
        return vacancy === "won't happen";
      },

      isSubscribedToEvent(event) {
        // ToDo: get from subscription module
        return event === "won't happen";
      },

      allowSubscription(vacancy) {
        const open = this.event.is_open_for_subscriptions;
        const allow_multiple = this.event.allow_multiple_vacancy_subscription;
        const subscribed_event = this.isSubscribedToEvent(this.event);

        return (
          open &&
          !this.isSubscribedToVacancy(vacancy) &&
          (allow_multiple || !subscribed_event)
        );
      },

      subscribe(vacancy) {
        this.$emit("subscribe", vacancy);
      },
    },
  };
</script>
