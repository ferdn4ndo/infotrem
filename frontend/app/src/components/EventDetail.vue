<template>
  <article class="EventDetail">
    <section 
      v-if="hasDescription()" 
      class="EventDetail-Description"
    >
      <p class="EventDetail-Paragraph">
        {{ event.description }}
      </p>
    </section>

    <div 
      v-if="hasNotice()" 
      class="EventDetail-Description EventDetail-Notice"
    >
      <the-icon 
        icon="info" 
        class="EventDetail-NoticeIcon"
      />

      <b>Atualiza&ccedil;&atilde;o:&nbsp;</b>

      <span v-html="event.notice_text" />
    </div>

    <the-title>Datas</the-title>

    <section class="EventDetail-Dates">
      <div class="EventDetail-Date">
        <date-indicator
          :date="event.registration_start_date"
          icon="calendar_check"
          styling="initial"
          title="Abertura das inscri&ccedil;&otilde;es"
        />
      </div>

      <div class="EventDetail-Date">
        <date-indicator
          :date="event.registration_end_date"
          icon="calendar_times"
          styling="final"
          title="Encerramento das inscri&ccedil;&otilde;es"
        />
      </div>

      <div class="EventDetail-Date">
        <date-indicator
          :date="event.results_final_date"
          icon="results_final"
          title="Data da classifica&ccedil;&atilde;o final"
        />
      </div>

      <div 
        v-if="event.payment_limit_date !== null" 
        class="EventDetail-Date"
      >
        <date-indicator
          :date="event.payment_limit_date"
          icon="money"
          title="Data limite de pagamento da inscri&ccedil;&atilde;o"
        />
      </div>

      <div 
        v-if="event.exam_objective_date !== null" 
        class="EventDetail-Date"
      >
        <date-indicator
          :date="event.exam_objective_date"
          icon="exam_objective"
          title="Data da prova objetiva"
        />
      </div>

      <div 
        v-if="event.exam_practical_date !== null" 
        class="EventDetail-Date"
      >
        <date-indicator
          :date="event.exam_practical_date"
          icon="exam_practical"
          title="Data da prova pr&aacute;tica"
        />
      </div>

      <div
        v-if="event.results_objective_date !== null"
        class="EventDetail-Date"
      >
        <date-indicator
          :date="event.results_objective_date"
          icon="results_objective"
          title="Data da classifica&ccedil;&atilde;o geral da prova objetiva"
        />
      </div>

      <div
        v-if="event.results_practical_date !== null"
        class="EventDetail-Date"
      >
        <date-indicator
          :date="event.results_practical_date"
          icon="results_practical"
          title="Data da classifica&ccedil;&atilde;o geral da prova pr&aacute;tica"
        />
      </div>
    </section>

    <the-title>Vagas</the-title>

    <section 
      v-if="hasVacancies" 
      class="EventDetail-VacanciesGroups"
    >
      <collapse-block
        v-for="(vacancies, typeName) in vacancyGroups"
        :title="typeName"
        :start-expanded="onlyOneGroup()"
        :key="typeName"
        class="EventDetail-VacancyGroup"
      >
        <section class="EventDetail-Vacancies">
          <article
            v-for="vacancy in vacancies"
            :key="vacancy.id"
            class="EventDetail-Vacancy"
          >
            <vacancy-detail
              :event="event"
              :vacancy="vacancy"
              @subscribe="subscribe"
            />
          </article>
        </section>
      </collapse-block>
    </section>

    <p 
      v-if="!hasVacancies" 
      class="EventDetail-NoVacancies"
    >
      Não existem vagas cadastrados para este evento.
    </p>
  </article>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .EventDetail {
    display: flex;
    flex-direction: column;
    justify-content: center;

    &-Dates {
      display: flex;
      flex-direction: row;
      flex-wrap: wrap;
      justify-content: space-around;
      align-items: stretch;
      margin: 0 10px;
    }

    &-Date {
      flex: 1 1 auto;
      padding: 20px;
      margin: 10px;
      border: 1px solid $background-secondary-border;
      border-radius: 10px;
      background-color: $background-secondary-color;
      box-sizing: border-box;
      text-align: center;
      display: flex;
      justify-content: center;
      align-items: center;

      @media screen and (min-width: $mobile-breakpoint - 1) {
        flex: 1 1 45%;
        max-width: 45%;
      }

      @media screen and (min-width: $desktop-breakpoint - 1) {
        flex: 1 1 30%;
        max-width: 30%;
      }
    }

    &-Description {
      font-size: 16px;
      font-weight: lighter;
      margin: 20px 10px;
      text-align: justify;
      word-wrap: break-word;
      box-sizing: border-box;
    }

    &-Paragraph {
      margin: 0;
    }

    &-NoVacancies {
      margin: 0 0 30px 0;
      font-size: 14pt;
      text-align: center;
    }

    &-Notice {
      margin: 0 20px;
      box-sizing: border-box;
      padding: 10px 20px;
      background-color: $foreground-tertiary-color;
      border: 1px solid $color-background-border;
      //border-bottom: 1px solid $color-background-border;
    }

    &-NoticeIcon {
      margin-right: 5px;
    }

    &-Action {
      box-sizing: border-box;
      padding: 10px;
      width: 100%;
    }

    &-Button {
      width: 100%;
    }

    &-VacanciesGroups {
      margin: 0 20px;
    }

    &-VacancyGroup {
      margin-bottom: 30px;
      align-self: center;
    }

    &-Vacancies {
      display: flex;
      flex-wrap: wrap;
    }

    &-Vacancy {
      flex: 1 1 100%;

      @media screen and (min-width: $desktop-breakpoint - 1) {
        flex: 1 1 50%;
        max-width: 50%;
      }
    }
  }
</style>

<script>
  import DateIndicator from "@/components/DateIndicator";
  import TheCard from "@/components/TheCard";
  import TheButton from "@/components/TheButton";
  import TheIcon from "@/components/TheIcon";
  import CollapseBlock from "@/components/CollapseBlock";
  import TheTitle from "@/components/TheTitle";
  import VacancyDetail from "@/components/VacancyDetail";

  export default {
    components: {
      VacancyDetail,
      TheTitle,
      CollapseBlock,
      TheIcon,
      DateIndicator,
      TheButton,
      TheCard,
    },

    props: {
      event: {
        type: Object,
        required: true,
      },
    },

    data: () => ({
      vacancyGroups: {},
    }),

    computed: {
      hasVacancies() {
        return Object.keys(this.vacancyGroups).length > 0;
      },
    },

    mounted() {
      this.updateVacancyGroups();
    },

    methods: {
      displayVacancyCount(value) {
        if (value === 0) {
          return "Cadastro Reserva";
        }

        return value.toString();
      },

      hasDescription() {
        return this.event.description && this.event.description !== "";
      },

      hasNotice() {
        return this.event.notice_text && this.event.notice_text !== "";
      },

      onlyOneGroup() {
        return Object.keys(this.vacancyGroups).length === 1;
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

      subscribe(vacancy) {
        this.$emit("subscribe", vacancy);
      },
    },
  };
</script>
