<template>
  <base-form
    ref="registerForm"
    :fields="fields"
    @error="handleError"
    @submit="handleValidData"
  >
    <!-- Name -->
    <the-field
      ref="register_name"
      :metadata="{
        maxLength: 120,
      }"
      :required="true"
      name="name"
      type="text"
      class="RegisterForm-Input"
      placeholder="Nome completo"
      description="Seu nome completo sem abreviações (ex: Fulano Beltrano)"
    />

    <!-- E-mail -->
    <the-field
      ref="register_email"
      :metadata="{
        type: 'email',
      }"
      :required="true"
      name="email"
      type="text"
      class="RegisterForm-Input"
      placeholder="E-mail"
      description="Seu e-mail que será usado para validar sua conta (ex: fulano@email.com). Você precisará confirmá-lo para poder se cadastrar em algum evento."
    />

    <!-- Password -->
    <the-field
      ref="register_password"
      :metadata="{
        type: 'password',
        maxLength: 64,
      }"
      :required="true"
      name="password"
      type="text"
      class="RegisterForm-Input"
      placeholder="Senha"
      description="Sua senha de acesso."
    />

    <!-- Confirm password -->
    <the-field
      ref="register_password2"
      :metadata="{
        type: 'password',
        maxLength: 64,
      }"
      :required="true"
      name="password2"
      type="text"
      class="RegisterForm-Input"
      placeholder="Confirmar Senha"
      description="Repita sua senha de acesso."
    />

    <!-- RG -->
    <the-field
      ref="register_rg"
      :required="true"
      :metadata="{
        maxLength: 20,
      }"
      name="rg"
      type="text"
      class="RegisterForm-Input"
      description="Seu RG, com pontos e/ou traços."
      placeholder="RG"
    />

    <!-- CPF -->
    <the-field
      ref="register_cpf"
      :metadata="{
        mask: '###.###.###-##',
      }"
      :required="true"
      name="cpf"
      type="number"
      class="RegisterForm-Input"
      description="Seu CPF (Cadastro de Pessoa Física)."
      placeholder="CPF"
    />

    <!-- Birth Date -->
    <the-field
      ref="register_birthdate"
      :required="true"
      name="birth_date"
      type="date"
      class="RegisterForm-Input"
      placeholder="Data de Nascimento (dd/mm/aaaa)"
      description="Sua data de nascimento no formato dia/mês/ano."
    />

    <!-- Address -->
    <the-field
      ref="register_address"
      :metadata="{
        maxLength: 255,
      }"
      :required="true"
      name="address"
      type="text"
      class="RegisterForm-Input"
      placeholder="Endereço"
      description="Seu endereço residencial (sem o número)"
    />

    <!-- Number -->
    <the-field
      ref="register_number"
      :metadata="{
        maxValue: 99999,
      }"
      name="number"
      type="number"
      class="RegisterForm-Input"
      placeholder="Número"
      description="O número de sua residência."
    />

    <!-- Complement -->
    <the-field
      ref="register_complement"
      :metadata="{
        maxLength: 50,
      }"
      name="complement"
      type="text"
      class="RegisterForm-Input"
      placeholder="Complemento"
      description="O complemento do seu endereço (apartamento, bloco, sala, andar, etc)."
    />

    <!-- State -->
    <the-field
      ref="register_state"
      :metadata="{
        items: statesList,
      }"
      name="state_id"
      type="select"
      class="RegisterForm-Input"
      placeholder="Estado"
      description="O estado onde você mora."
      @change="changedLocationState"
    />

    <!-- City -->
    <the-field
      ref="register_city"
      :metadata="{
        items: selectedStateCities,
      }"
      name="city_id"
      type="select"
      class="RegisterForm-Input"
      placeholder="Cidade"
      description="A cidade onde você mora."
    />

    <!-- ZipCode -->
    <the-field
      ref="register_zipcode"
      :metadata="{
        mask: '##.###-###',
      }"
      :required="true"
      name="zipcode"
      type="number"
      class="RegisterForm-Input"
      placeholder="CEP"
      description="O CEP de onde você mora."
    />

    <!-- Phone -->
    <the-field
      ref="register_phone"
      :metadata="{
        mask: '(##) ####-####?#',
      }"
      name="phone"
      type="number"
      class="RegisterForm-Input"
      placeholder="Celular / Telefone"
      description="Seu número de celular ou telefone fixo"
    />

    <!-- Special Needs -->
    <the-field
      ref="register_special_needs"
      name="special_needs"
      type="check"
      class="RegisterForm-Input"
      placeholder="Sou PcD (Pessoa com Deficiência)"
      @change="changedSpecialNeeds"
    />

    <!-- Auditive Disability -->
    <the-field
      v-if="displaySpecialNeeds"
      ref="register_auditive_disability"
      name="auditive_disability"
      type="check"
      class="RegisterForm-Input"
      placeholder="Possuo alguma deficiência auditiva"
    />

    <!-- Physical Disability -->
    <the-field
      v-if="displaySpecialNeeds"
      ref="register_physical_disability"
      name="physical_disability"
      type="check"
      class="RegisterForm-Input"
      placeholder="Possuo alguma deficiência física"
    />

    <!-- Mental Disability -->
    <the-field
      v-if="displaySpecialNeeds"
      ref="register_mental_disability"
      name="mental_disability"
      type="check"
      class="RegisterForm-Input"
      placeholder="Possuo alguma deficiência mental"
    />

    <!-- Motor Disability -->
    <the-field
      v-if="displaySpecialNeeds"
      ref="register_motor_disability"
      name="motor_disability"
      type="check"
      class="RegisterForm-Input"
      placeholder="Possuo alguma deficiência motora"
    />

    <!-- Visual Disability -->
    <the-field
      v-if="displaySpecialNeeds"
      ref="register_visual_disability"
      name="visual_disability"
      type="check"
      class="RegisterForm-Input"
      placeholder="Possuo alguma deficiência visual"
    />

    <!-- Other Disability -->
    <the-field
      v-if="displaySpecialNeeds"
      ref="register_other_disability"
      name="other_disability"
      type="check"
      class="RegisterForm-Input"
      placeholder="Possuo alguma outra deficiência (descrever)"
      @change="changedHasOtherDisability"
    />

    <!-- Other Disability Detail -->
    <the-field
      v-if="displaySpecialNeeds"
      ref="register_other_disability_detail"
      :disabled="!hasOtherDisability"
      :metadata="{
        maxLength: 255,
      }"
      :required="hasOtherDisability"
      name="other_disability_detail"
      type="text"
      class="RegisterForm-Input"
      placeholder="Descrição da deficiência"
      description="Descreva a condição de deficiência que você possui"
    />

    <p
      v-if="displaySpecialNeeds"
      class="RegisterForm-Paragraph"
    >
      OBS: Não serão considerados como deficiência os distúrbios de acuidade
      visual passíveis de correção simples do tipo miopia, astigmatismo,
      estrabismo e congêneres.
    </p>

    <!-- CID -->
    <the-field
      v-if="displaySpecialNeeds"
      ref="register_cid"
      :metadata="{
        maxLength: 50,
      }"
      name="cid"
      type="text"
      class="RegisterForm-Input"
      placeholder="CID (Código Internacional de Doenças)"
      description="Insira o CID associado ao seu atestado (se houver)"
    />

    <!-- Doctor's Name -->
    <the-field
      v-if="displaySpecialNeeds"
      ref="register_doctor"
      :metadata="{
        maxLength: 100,
      }"
      name="doctor"
      type="text"
      class="RegisterForm-Input"
      placeholder="Nome do médico"
      description="Nome do médico que assinou seu atestado (se houver)"
    />

    <!-- Accommodations -->
    <the-field
      v-if="displaySpecialNeeds"
      ref="register_accommodations"
      name="accommodations"
      type="check"
      class="RegisterForm-Input"
      placeholder="Preciso de acomodações especiais"
      @change="changedSpecialAccommodations"
    />

    <!-- Special Accommodation: Reader -->
    <the-field
      v-if="displaySpecialNeeds && displaySpecialAccommodations"
      ref="register_accommodation_reader"
      name="accommodation_reader"
      type="check"
      class="RegisterForm-Input"
      placeholder="Preciso do auxílio de um(a) ledor(a)"
    />

    <!-- Special Accommodation: Enlarged Exam -->
    <the-field
      v-if="displaySpecialNeeds && displaySpecialAccommodations"
      ref="register_accommodation_enlarged_exam"
      name="accommodation_enlarged_exam"
      type="check"
      class="RegisterForm-Input"
      placeholder="Preciso de uma prova ampliada"
    />

    <!-- Special Accommodation: Typist -->
    <the-field
      v-if="displaySpecialNeeds && displaySpecialAccommodations"
      ref="register_accommodation_typist"
      name="accommodation_typist"
      type="check"
      class="RegisterForm-Input"
      placeholder="Preciso do auxílio de um(a) transcritor(a)"
    />

    <!-- Special Accommodation: Other -->
    <the-field
      v-if="displaySpecialNeeds && displaySpecialAccommodations"
      ref="register_other_accommodation"
      name="other_accommodation"
      type="check"
      class="RegisterForm-Input"
      placeholder="Preciso de outro(a) acomodação especial (descrever)"
      @change="changedOtherAccommodations"
    />

    <!-- Other Accommodation Detail -->
    <the-field
      v-if="displaySpecialNeeds && displaySpecialAccommodations"
      ref="register_other_accommodation_detail"
      :disabled="!needsOtherAccommodation"
      :metadata="{
        maxLength: 255,
      }"
      :required="needsOtherAccommodation"
      name="other_accommodation_detail"
      type="text"
      class="RegisterForm-Input"
      placeholder="Descrição da necessidade de acomodação"
      description="Descreva sua(s) necessidade(s) de acomodação para realização da(s) prova(s)."
    />
  </base-form>
</template>

<style lang="scss" scoped>
  @import "~@/styles/_variables.scss";

  .RegisterForm {
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
    FETCH_STATES,
    FETCH_STATE_CITIES,
    REGISTER,
  } from "@/store/actions.type";
  import { DATE_REGEX } from "@/common/regex";
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
      dateRegex: DATE_REGEX,
      displaySpecialNeeds: false,
      displaySpecialAccommodations: true,
      fields: [],
      hasOtherDisability: false,
      needsOtherAccommodation: false,
      statesList: [],
      selectedState: null,
      selectedStateCities: [],
    }),

    computed: {
      ...mapGetters(["states", "stateCities"]),
    },

    mounted() {
      this.updateFields();
      this.updateStates();
    },

    methods: {
      handleError(error) {
        this.$emit("error", error);
      },

      handleValidData(payload) {
        this.$store
          .dispatch(REGISTER, payload)
          .then(() => {
            this.$emit(
              "success",
              "Registro realizado com sucesso! Acesse seu e-mail para validar seu perfil."
            );
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

      changedLocationState(newValue) {
        if (!this.selectedState || this.selectedState.id !== newValue) {
          const state = this.states.filter((state) => state.id === newValue)[0];
          this.selectedState = state;
          this.selectedStateCities = this.getStateCities(state);
        }
      },

      updateStates() {
        //nao foi essa
        if (this.states.length) {
          this.parseStatesList();
          return;
        }

        this.$store
          .dispatch(FETCH_STATES)
          .then(() => {
            this.parseStatesList();
          })
          .catch((error) => {
            this.$emit("error", "Erro ao recuperar a lista de estados");
            console.log(error);
          });
      },

      getStateCities(state) {
        if (
          state &&
          state.abbrev !== undefined in this.stateCities &&
          this.stateCities[state.abbrev] !== undefined
        ) {
          this.selectedStateCities = this.parseStateCitiesList(
            this.stateCities[state.abbrev]
          );
          return;
        }

        this.$store
          .dispatch(FETCH_STATE_CITIES, { state: state })
          .then((cities) => {
            this.parseStateCitiesList(cities);
          })
          .catch((error) => {
            this.$emit("error", "Erro ao recuperar a lista de cidades");
            console.log(error);
          });
      },

      parseStatesList() {
        if (!this.states.length) {
          return [];
        }

        this.statesList = this.states.map((obj) => {
          return {
            text: `${obj.abbrev} - ${obj.name}`,
            value: obj.id,
          };
        });
      },

      parseStateCitiesList(cities) {
        this.selectedStateCities = cities.map((obj) => {
          return {
            text: obj.name,
            value: obj.id,
          };
        });
      },

      changedSpecialNeeds() {
        this.displaySpecialNeeds = this.$refs.register_special_needs.getValue();
        this.updateFields();
      },

      changedOtherAccommodations() {
        this.needsOtherAccommodation = this.$refs.register_other_accommodation.getValue();
        this.updateFields();
      },

      changedSpecialAccommodations() {
        this.displaySpecialAccommodations = this.$refs.register_accommodations.getValue();
        this.updateFields();
      },

      changedHasOtherDisability() {
        this.hasChildren = this.$refs.register_other_disability.getValue();
        this.updateFields();
      },

      updateFields() {
        let fields = [
          this.$refs.register_name,
          this.$refs.register_email,
          this.$refs.register_password,
          this.$refs.register_password2,
          this.$refs.register_rg,
          this.$refs.register_cpf,
          this.$refs.register_birthdate,
          this.$refs.register_address,
          this.$refs.register_number,
          this.$refs.register_complement,
          this.$refs.register_state,
          this.$refs.register_city,
          this.$refs.register_zipcode,
          this.$refs.register_phone,
          this.$refs.register_special_needs,
          this.$refs.register_auditive_disability,
          this.$refs.register_physical_disability,
          this.$refs.register_mental_disability,
          this.$refs.register_motor_disability,
          this.$refs.register_visual_disability,
          this.$refs.register_other_disability,
          this.$refs.register_other_disability_detail,
          this.$refs.register_cid,
          this.$refs.register_doctor,
          this.$refs.register_accommodations,
          this.$refs.register_accommodation_reader,
          this.$refs.register_accommodation_enlarged_exam,
          this.$refs.register_accommodation_typist,
          this.$refs.register_other_accommodation,
          this.$refs.register_other_accommodation_detail,
          this.$refs.register_relational_status,
        ];
        fields = fields.filter((field) => field !== undefined);

        if (this.fields.length !== fields.length) {
          this.fields = fields;
        }
      },
    },
  };
</script>
