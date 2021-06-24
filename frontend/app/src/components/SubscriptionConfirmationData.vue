<template>
  <div class="SubscriptionConfirmationData">
    <the-title
      class="SubscriptionConfirmationData-Title"
    >Dados Pessoais</the-title>

    <dl class="SubscriptionConfirmationData-DataList">
      <!-- Nome -->
      <dt class="SubscriptionConfirmationData-DataTitle">Nome Completo</dt>
      <dd class="SubscriptionConfirmationData-DataValue">
        {{ currentUser.name }}
      </dd>

      <!-- E-mail -->
      <dt class="SubscriptionConfirmationData-DataTitle">E-mail</dt>
      <dd class="SubscriptionConfirmationData-DataValue">
        {{ currentUser.email }}
      </dd>

      <!-- RG -->
      <dt class="SubscriptionConfirmationData-DataTitle">RG</dt>
      <dd class="SubscriptionConfirmationData-DataValue">
        {{ currentUser.rg }}
      </dd>

      <!-- CPF -->
      <dt class="SubscriptionConfirmationData-DataTitle">CPF</dt>
      <dd class="SubscriptionConfirmationData-DataValue">
        {{ currentUser.cpf | cpf }}
      </dd>

      <!-- Data de Nascimento -->
      <dt class="SubscriptionConfirmationData-DataTitle">Data de Nascimento</dt>
      <dd class="SubscriptionConfirmationData-DataValue">
        {{ currentUser.birth_date | date }}
      </dd>

      <!-- Endereço -->
      <dt class="SubscriptionConfirmationData-DataTitle">Endereço</dt>
      <dd class="SubscriptionConfirmationData-DataValue">
        {{ currentUser.address | cpf }}
      </dd>

      <!-- Número -->
      <dt class="SubscriptionConfirmationData-DataTitle">Número</dt>
      <dd class="SubscriptionConfirmationData-DataValue">
        {{ currentUser.number | blank }}
      </dd>

      <!-- Complemento -->
      <dt class="SubscriptionConfirmationData-DataTitle">Complemento</dt>
      <dd class="SubscriptionConfirmationData-DataValue">
        {{ currentUser.complement | blank }}
      </dd>

      <!-- Estado -->
      <dt class="SubscriptionConfirmationData-DataTitle">Estado</dt>
      <dd class="SubscriptionConfirmationData-DataValue">{{ stateName }}</dd>

      <!-- Cidade -->
      <dt class="SubscriptionConfirmationData-DataTitle">Cidade</dt>
      <dd class="SubscriptionConfirmationData-DataValue">{{ cityName }}</dd>

      <!-- CEP -->
      <dt class="SubscriptionConfirmationData-DataTitle">CEP</dt>
      <dd class="SubscriptionConfirmationData-DataValue">
        {{ currentUser.cep | cep | blank }}
      </dd>

      <!-- Celular/Telefone -->
      <dt class="SubscriptionConfirmationData-DataTitle">Celular / Telefone</dt>
      <dd class="SubscriptionConfirmationData-DataValue">
        {{ currentUser.phone | phone }}
      </dd>

      <!-- PcD -->
      <dt class="SubscriptionConfirmationData-DataTitle">
        É <abbr title="Pessoa com Deficiência">PcD</abbr>
      </dt>
      <dd class="SubscriptionConfirmationData-DataValue">
        {{ currentUser.special_needs | boolean }}
      </dd>
    </dl>

    <the-title
      class="SubscriptionConfirmationData-Title"
    >Dados do Evento</the-title>

    <dl class="SubscriptionConfirmationData-DataList">
      <!-- Evento -->
      <dt class="SubscriptionConfirmationData-DataTitle">Evento</dt>
      <dd class="SubscriptionConfirmationData-DataValue">{{ event.title }}</dd>

      <!-- Vaga/Cargo -->
      <dt class="SubscriptionConfirmationData-DataTitle">
        Vaga/Cargo Pretendido
      </dt>
      <dd class="SubscriptionConfirmationData-DataValue">
        {{ vacancy.job_title }}
      </dd>

      <!-- Total de Vagas -->
      <dt class="SubscriptionConfirmationData-DataTitle">Total de Vagas</dt>
      <dd class="SubscriptionConfirmationData-DataValue">
        {{ vacancy.total_vacancies | vacancy }}
      </dd>

      <!-- Valor da Inscrição -->
      <dt class="SubscriptionConfirmationData-DataTitle">Valor da Inscrição</dt>
      <dd class="SubscriptionConfirmationData-DataValue">
        {{ vacancy.subscription_price | currency }}
      </dd>
    </dl>
  </div>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .SubscriptionConfirmationData {
    &-Title {
      margin-top: 5px;
      margin-bottom: 10px;
    }

    &-DataList {
      display: flex;
      flex-flow: row;
      flex-wrap: wrap;
      font-size: 18px;
    }

    &-DataTitle {
      font-weight: bold;
      flex: 0 0 100%;
      box-sizing: border-box;

      &:after {
        content: ":";
      }

      @media screen and (min-width: $tablet-breakpoint - 1) {
        text-align: right;
        flex: 0 1 33%;
      }
    }

    &-DataValue {
      flex: 0 0 100%;
      text-align: left;
      padding-left: 10px;
      margin-left: 0;
      box-sizing: border-box;
      margin-bottom: 10px;

      @media screen and (min-width: $tablet-breakpoint - 1) {
        margin-left: auto;
        flex: 1 1 66%;
      }
    }

    &-StatusItem {
      margin: 10px 15px 0 10px;
      border-radius: 5px;
    }

    &-Paragraph {
      cursor: default;
      text-align: justify;

      margin: 10px;

      &--bold {
        font-weight: bold;
      }
    }
  }
</style>

<script>
  import { mapGetters } from "vuex";
  import TheModal from "@/components/modals/TheModal";
  import StatusItem from "@/components/StatusItem";
  import { FETCH_CITY, FETCH_STATE } from "@/store/actions.type";
  import TheButton from "@/components/TheButton";
  import TheTitle from "@/components/TheTitle";

  export default {
    name: "SubscriptionConfirmationData",

    components: {
      TheTitle,
      TheButton,
      StatusItem,
      TheModal,
    },

    props: {
      vacancy: {
        type: Object,
        required: true,
      },

      event: {
        type: Object,
        required: true,
      },
    },

    data() {
      return {
        stateName: "-",
        cityName: "-",
      };
    },

    computed: {
      ...mapGetters(["cities", "currentUser", "isAuthenticated", "states"]),

      title() {
        switch (this.currentState) {
          case "check":
            return "Pré-inscrição";
          case "confirm":
            return "Confirmação dos dados";
          case "payment":
            return "Pagamento";
          default:
            return "Erro";
        }
      },
    },

    watch: {
      currentUser() {
        this.getStateName(this.currentUser.state);
        this.getCityName(this.currentUser.state, this.currentUser.city);
      },
    },

    mounted() {
      this.getStateName(this.currentUser.state);
      this.getCityName(this.currentUser.state, this.currentUser.city);
    },

    methods: {
      getStateName(stateId) {
        let filteredStates = this.states.filter((state) => {
          return state.id === stateId;
        });

        if (filteredStates.length === 0) {
          this.$store.dispatch(FETCH_STATE, stateId).then((state) => {
            this.stateName = state.name;
          });
        } else {
          this.stateName = filteredStates[0].name;
        }
      },

      getCityName(stateId, cityId) {
        let filteredCities = this.cities.filter((city) => {
          return city.id === cityId;
        });

        if (filteredCities.length === 0) {
          this.$store
            .dispatch(FETCH_CITY, { stateId: stateId, cityId: cityId })
            .then((city) => {
              this.cityName = city.name;
            });
        } else {
          return filteredCities[0].name;
        }
      },
    },
  };
</script>
