<template>
  <base-form
    ref="profileForm"
    :initial-values="initialData"
    :fields="fields"
    submit-text="Salvar"
    @error="handleError"
    @submit="handleValidData"
  >
    <!-- Relational Status -->
    <the-field
      ref="profile_relational_status"
      :metadata="{
        items: enums.relational_status,
      }"
      name="relational_status"
      type="select"
      class="ProfileForm-Input"
      placeholder="Estado Civil"
      description="O estado civil que melhor representa sua situação atual."
    />

    <!-- Has Children -->
    <the-field
      ref="profile_has_children"
      name="has_children"
      type="check"
      class="ProfileForm-Input"
      placeholder="Possui filhos(as)?"
      @change="changedHasChildren"
    />

    <!-- Number of Children -->
    <the-field
      v-show="hasChildren"
      ref="profile_total_children"
      :metadata="{
        maxValue: 99,
      }"
      name="total_children"
      type="number"
      class="ProfileForm-Input"
      placeholder="Número de Filhos(as)"
      description="O número de filhos(as) que você possui."
    />

    <!-- Youngest Child Birth Date -->
    <the-field
      v-show="hasChildren"
      ref="profile_youngest_child_birth_date"
      name="youngest_child_birth_date"
      type="date"
      class="ProfileForm-Input"
      placeholder="Data de Nasc. do filho mais novo (dd/mm/aaaa)"
      description="Data de nascimento do filho(a) mais novo, no formato dd/mm/aaaa."
    />

    <!-- Skin Color or Racial Group -->
    <the-field
      ref="profile_skin_color_or_racial_group"
      :metadata="{
        items: enums.skin_colour,
      }"
      name="skin_color_or_racial_group"
      type="select"
      class="ProfileForm-Input"
      placeholder="Etnia"
      description="Selecione a etnia que melhor representa você."
    />

    <!-- Education Level (Self) -->
    <the-field
      ref="profile_education_level_self"
      :metadata="{
        items: enums.education_level,
      }"
      name="education_level_self"
      type="select"
      class="ProfileForm-Input"
      placeholder="Escolaridade (sua)"
      description="Selecione a sua escolaridade."
    />

    <!-- Education Level (Father) -->
    <the-field
      ref="profile_education_level_father"
      :metadata="{
        items: enums.education_level,
      }"
      name="education_level_father"
      type="select"
      class="ProfileForm-Input"
      placeholder="Escolaridade (Pai)"
      description="Selecione a escolaridade do seu pai."
    />

    <!-- Education Level (Mother) -->
    <the-field
      ref="profile_education_level_mother"
      :metadata="{
        items: enums.education_level,
      }"
      name="education_level_mother"
      type="select"
      class="ProfileForm-Input"
      placeholder="Escolaridade (Mãe)"
      description="Selecione a escolaridade da sua mãe."
    />

    <!-- Habitation Level -->
    <the-field
      ref="profile_habitation_level"
      :metadata="{
        items: enums.habitation_level,
      }"
      name="habitation_level"
      type="select"
      class="ProfileForm-Input"
      placeholder="Situação Habitacional"
      description="Selecione a situação habitacional que melhor descreve o seu contexto atual."
    />

    <!-- Number of People Living With You -->
    <the-field
      ref="profile_total_people_living_together"
      :metadata="{
        maxValue: 99,
      }"
      name="total_people_living_together"
      type="number"
      class="ProfileForm-Input"
      placeholder="Número de Familiares na mesma Casa"
      description="O número de familiares que vivem com você na mesma habitação."
    />

    <!-- Family Income Level -->
    <the-field
      ref="profile_family_income_level"
      :metadata="{
        items: enums.family_income_level,
      }"
      name="family_income_level"
      type="select"
      class="ProfileForm-Input"
      placeholder="Renda Familiar Total"
      description="Qual a renda total da família que mora com você, incluindo seus rendimentos?"
    />

    <!-- Financial Status -->
    <the-field
      ref="profile_financial_status"
      :metadata="{
        items: enums.financial_status,
      }"
      name="financial_status"
      type="select"
      class="ProfileForm-Input"
      placeholder="Situação Financeira (incluindo bolsas)"
      description="Qual alternativa melhor descreve sua situação financeira (incluindo bolsas)?"
    />

    <!-- Job Status -->
    <the-field
      ref="profile_job_status"
      :metadata="{
        items: enums.job_status,
      }"
      name="job_status"
      type="select"
      class="ProfileForm-Input"
      placeholder="Situação Trabalhista"
      description="Qual a sua situação de trabalho (exceto estágio ou bolsas)?"
    />
  </base-form>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .ProfileForm {
    &-Input {
      margin-bottom: 5px;
    }

    &-Paragraph {
      cursor: default;
      text-align: justify;

      margin: 5px 0 10px;

      &--bold {
        font-weight: bold;
      }
    }
  }
</style>

<script>
  import { mapGetters } from "vuex";
  import {
    RELATIONAL_STATUS_OPTIONS,
    SKIN_COLOUR_OPTIONS,
    EDUCATION_LEVEL_OPTIONS,
    HABITATION_LEVEL_OPTIONS,
    FAMILY_INCOME_LEVEL_OPTIONS,
    FINANCIAL_STATUS_OPTIONS,
    JOB_STATUS_OPTIONS,
  } from "@/common/enums";
  import { UPDATE_PROFILE } from "@/store/actions.type";
  import BaseForm from "@/components/forms/BaseForm";
  import CheckboxField from "@/components/fields/CheckboxField";
  import SelectField from "@/components/fields/SelectField";
  import TextField from "@/components/fields/TextField";
  import TheIcon from "@/components/TheIcon";
  import TheButton from "@/components/TheButton";
  import TheField from "@/components/fields/TheField";

  export default {
    components: {
      TheField,
      BaseForm,
      CheckboxField,
      SelectField,
      TextField,
      TheIcon,
      TheButton,
    },

    data: () => ({
      enums: {
        relational_status: RELATIONAL_STATUS_OPTIONS,
        skin_colour: SKIN_COLOUR_OPTIONS,
        education_level: EDUCATION_LEVEL_OPTIONS,
        habitation_level: HABITATION_LEVEL_OPTIONS,
        family_income_level: FAMILY_INCOME_LEVEL_OPTIONS,
        financial_status: FINANCIAL_STATUS_OPTIONS,
        job_status: JOB_STATUS_OPTIONS,
      },
      fields: [],
      initialData: {},
      hasChildren: false,
    }),

    computed: {
      ...mapGetters(["currentUser"]),
    },

    watch: {
      currentUser(value) {
        this.initialData = value;
      },
    },

    mounted() {
      this.updateFields();

      if (this.currentUser !== undefined) {
        this.initialData = this.currentUser;
      }
    },

    methods: {
      handleError(error) {
        this.$emit("error", error);
      },

      handleValidData(payload) {
        this.$store
          .dispatch(UPDATE_PROFILE, payload)
          .then(() => {
            this.$emit("success", "Perfil atualizado com sucesso!");
          })
          .catch((error) => {
            if (error.response) {
              if (error.response.status === 400) {
                this.$emit(
                  "error",
                  "Existem campos inválidos. Por favor, confira as informações fornecidas e tente novamente."
                );
              } else if (error.response.status === 409) {
                this.$emit(
                  "error",
                  "E-mail já cadastrado! Utilize a opção 'recuperar senha' (a partir da opção 'Entrar') para recuperar seu acesso."
                );
              } else {
                // ToDo: save to a log here
                this.$emit(
                  "error",
                  "Ocorreu um erro interno ao processar seu cadastro. Por favor, entre em contato relatando o problema."
                );
              }
            }
          });
      },

      changedHasChildren() {
        this.hasChildren = this.$refs.profile_has_children.getValue();
        this.updateFields();
      },

      changedHasOtherDisability() {
        this.hasChildren = this.$refs.profile_other_disability.getValue();
        this.updateFields();
      },

      updateFields() {
        this.fields = [
          this.$refs.profile_relational_status,
          this.$refs.profile_has_children,
          this.$refs.profile_total_children,
          this.$refs.profile_youngest_child_birth_date,
          this.$refs.profile_skin_color_or_racial_group,
          this.$refs.profile_education_level_self,
          this.$refs.profile_education_level_father,
          this.$refs.profile_education_level_mother,
          this.$refs.profile_habitation_level,
          this.$refs.profile_total_people_living_together,
          this.$refs.profile_family_income_level,
          this.$refs.profile_financial_status,
          this.$refs.profile_job_status,
        ];

        this.fields = this.fields.filter((field) => field !== undefined);
      },
    },
  };
</script>
