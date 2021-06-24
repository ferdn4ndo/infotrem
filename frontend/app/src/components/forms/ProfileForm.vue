<template>
  <base-form
    ref="profileForm"
    :initial-values="initialData"
    :fields="fields"
    submit-text="Salvar"
    @error="handleError"
    @submit="handleValidData"
  >
    <!-- Name -->
    <the-field
      ref="profile_name"
      :metadata="{
        maxLength: 120,
      }"
      :required="true"
      name="name"
      type="text"
      class="ProfileForm-Input"
      placeholder="Nome completo"
      description="Seu nome completo sem abreviações (ex: Fulano Beltrano)"
    />

    <!-- E-mail -->
    <the-field
      ref="profile_email"
      :metadata="{
        type: 'email',
      }"
      :disabled="true"
      name="email"
      type="text"
      class="ProfileForm-Input"
      placeholder="E-mail"
      description="Seu e-mail que será usado para validar sua conta (ex: fulano@email.com). Você precisará confirmá-lo para poder se cadastrar em algum evento."
    />

    <!-- RG -->
    <the-field
      ref="profile_rg"
      :required="true"
      :metadata="{
        maxLength: 20,
      }"
      name="rg"
      type="text"
      class="ProfileForm-Input"
      description="Seu RG, com pontos e/ou traços."
      placeholder="RG"
    />

    <!-- CPF -->
    <the-field
      ref="profile_cpf"
      :metadata="{
        mask: '###.###.###-##',
      }"
      :required="true"
      name="cpf"
      type="number"
      class="ProfileForm-Input"
      description="Seu CPF (Cadastro de Pessoa Física)."
      placeholder="CPF"
    />

    <!-- Birth Date -->
    <the-field
      ref="profile_birthdate"
      :required="true"
      name="birth_date"
      type="date"
      class="ProfileForm-Input"
      placeholder="Data de Nascimento (dd/mm/aaaa)"
      description="Sua data de nascimento no formato dia/mês/ano."
    />

    <!-- Address -->
    <the-field
      ref="profile_address"
      :metadata="{
        maxLength: 255,
      }"
      :required="true"
      name="address"
      type="text"
      class="ProfileForm-Input"
      placeholder="Endereço"
      description="Seu endereço residencial (sem o número)"
    />

    <!-- Number -->
    <the-field
      ref="profile_number"
      :metadata="{
        maxValue: 99999,
      }"
      name="number"
      type="number"
      class="ProfileForm-Input"
      placeholder="Número"
      description="O número de sua residência."
    />

    <!-- Complement -->
    <the-field
      ref="profile_complement"
      :metadata="{
        maxLength: 50,
      }"
      name="complement"
      type="text"
      class="ProfileForm-Input"
      placeholder="Complemento"
      description="O complemento do seu endereço (apartamento, bloco, sala, andar, etc)."
    />

    <!-- State -->
    <the-field
      ref="profile_state"
      :metadata="{
        items: statesList,
        initialValue: initialState,
      }"
      name="state_id"
      type="select"
      class="ProfileForm-Input"
      placeholder="Estado"
      description="O estado onde você mora."
      @change="changedLocationState"
    />

    <!-- City -->
    <the-field
      ref="profile_city"
      :metadata="{
        items: selectedStateCities,
        initialValue: initialCity,
      }"
      name="city_id"
      type="select"
      class="ProfileForm-Input"
      placeholder="Cidade"
      description="A cidade onde você mora."
    />

    <!-- ZipCode -->
    <the-field
      ref="profile_zipcode"
      :metadata="{
        mask: '##.###-###',
      }"
      :required="true"
      name="zipcode"
      type="number"
      class="ProfileForm-Input"
      placeholder="CEP"
      description="O CEP de onde você mora."
    />

    <!-- Phone -->
    <the-field
      ref="profile_phone"
      :metadata="{
        mask: '(##) ####-####?#',
      }"
      name="phone"
      type="number"
      class="ProfileForm-Input"
      placeholder="Celular / Telefone"
      description="Seu número de celular ou telefone fixo"
    />

    <!-- Special Needs -->
    <the-field
      ref="profile_special_needs"
      name="special_needs"
      type="check"
      class="ProfileForm-Input"
      placeholder="Sou PcD (Pessoa com Deficiência)"
      @change="changedSpecialNeeds"
    />

    <!-- Auditive Disability -->
    <the-field
      v-show="displaySpecialNeeds"
      ref="profile_auditive_disability"
      name="auditive_disability"
      type="check"
      class="ProfileForm-Input"
      placeholder="Possuo alguma deficiência auditiva"
    />

    <!-- Physical Disability -->
    <the-field
      v-show="displaySpecialNeeds"
      ref="profile_physical_disability"
      name="physical_disability"
      type="check"
      class="ProfileForm-Input"
      placeholder="Possuo alguma deficiência física"
    />

    <!-- Mental Disability -->
    <the-field
      v-show="displaySpecialNeeds"
      ref="profile_mental_disability"
      name="mental_disability"
      type="check"
      class="ProfileForm-Input"
      placeholder="Possuo alguma deficiência mental"
    />

    <!-- Motor Disability -->
    <the-field
      v-show="displaySpecialNeeds"
      ref="profile_motor_disability"
      name="motor_disability"
      type="check"
      class="ProfileForm-Input"
      placeholder="Possuo alguma deficiência motora"
    />

    <!-- Visual Disability -->
    <the-field
      v-show="displaySpecialNeeds"
      ref="profile_visual_disability"
      name="visual_disability"
      type="check"
      class="ProfileForm-Input"
      placeholder="Possuo alguma deficiência visual"
    />

    <!-- Other Disability -->
    <the-field
      v-show="displaySpecialNeeds"
      ref="profile_other_disability"
      name="other_disability"
      type="check"
      class="ProfileForm-Input"
      placeholder="Possuo alguma outra deficiência (descrever)"
      @change="changedHasOtherDisability"
    />

    <!-- Other Disability Detail -->
    <the-field
      v-show="displaySpecialNeeds"
      ref="profile_other_disability_detail"
      :disabled="!hasOtherDisability"
      :metadata="{
        maxLength: 255,
      }"
      :required="hasOtherDisability"
      name="other_disability_detail"
      type="text"
      class="ProfileForm-Input"
      placeholder="Descrição da deficiência"
      description="Descreva a condição de deficiência que você possui"
    />

    <p
      v-show="displaySpecialNeeds"
      class="ProfileForm-Paragraph"
    >
      OBS: Não serão considerados como deficiência os distúrbios de acuidade
      visual passíveis de correção simples do tipo miopia, astigmatismo,
      estrabismo e congêneres.
    </p>

    <!-- CID -->
    <the-field
      v-show="displaySpecialNeeds"
      ref="profile_cid"
      :metadata="{
        maxLength: 50,
      }"
      name="cid"
      type="text"
      class="ProfileForm-Input"
      placeholder="CID (Código Internacional de Doenças)"
      description="Insira o CID associado ao seu atestado (se houver)"
    />

    <!-- Doctor's Name -->
    <the-field
      v-show="displaySpecialNeeds"
      ref="profile_doctor"
      :metadata="{
        maxLength: 100,
      }"
      name="doctor"
      type="text"
      class="ProfileForm-Input"
      placeholder="Nome do médico"
      description="Nome do médico que assinou seu atestado (se houver)"
    />

    <!-- Accommodations -->
    <the-field
      v-show="displaySpecialNeeds"
      ref="profile_accommodations"
      name="accommodations"
      type="check"
      class="ProfileForm-Input"
      placeholder="Preciso de acomodações especiais"
      @change="changedSpecialAccommodations"
    />

    <!-- Special Accommodation: Reader -->
    <the-field
      v-show="displaySpecialNeeds && displaySpecialAccommodations"
      ref="profile_accommodation_reader"
      name="accommodation_reader"
      type="check"
      class="ProfileForm-Input"
      placeholder="Preciso do auxílio de um(a) ledor(a)"
    />

    <!-- Special Accommodation: Enlarged Exam -->
    <the-field
      v-show="displaySpecialNeeds && displaySpecialAccommodations"
      ref="profile_accommodation_enlarged_exam"
      name="accommodation_enlarged_exam"
      type="check"
      class="ProfileForm-Input"
      placeholder="Preciso de uma prova ampliada"
    />

    <!-- Special Accommodation: Typist -->
    <the-field
      v-show="displaySpecialNeeds && displaySpecialAccommodations"
      ref="profile_accommodation_typist"
      name="accommodation_typist"
      type="check"
      class="ProfileForm-Input"
      placeholder="Preciso do auxílio de um(a) transcritor(a)"
    />

    <!-- Special Accommodation: Other -->
    <the-field
      v-show="displaySpecialNeeds && displaySpecialAccommodations"
      ref="profile_other_accommodation"
      name="other_accommodation"
      type="check"
      class="ProfileForm-Input"
      placeholder="Preciso de outro(a) acomodação especial (descrever)"
      @change="changedOtherAccommodations"
    />

    <!-- Other Accommodation Detail -->
    <the-field
      v-if="displaySpecialNeeds && displaySpecialAccommodations"
      ref="profile_other_accommodation_detail"
      :disabled="!needsOtherAccommodation"
      :metadata="{
        maxLength: 255,
      }"
      :required="needsOtherAccommodation"
      name="other_accommodation_detail"
      type="text"
      class="ProfileForm-Input"
      placeholder="Descrição da necessidade de acomodação"
      description="Descreva sua(s) necessidade(s) de acomodação para realização da(s) prova(s)."
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
    FETCH_STATES,
    FETCH_STATE_CITIES,
    UPDATE_PROFILE,
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
      initialData: {},
      initialState: null,
      initialCity: null,
      hasChildren: false,
      hasOtherDisability: false,
      needsOtherAccommodation: false,
      statesList: [],
      selectedState: null,
      selectedStateCities: [],
    }),

    computed: {
      ...mapGetters(["currentUser", "states", "stateCities"]),
    },

    watch: {
      currentUser(value) {
        this.initialData = value;
        this.initialCity = this.initialData.city;
        this.initialState = this.initialData.state;
      },
    },

    mounted() {
      if (this.currentUser !== undefined && this.currentUser !== null) {
        this.initialData = this.currentUser;
        this.initialCity = this.currentUser.city;
        this.initialState = this.currentUser.state;
      }

      this.updateFields();
      this.updateStates();
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

      changedLocationState(newValue) {
        if (!this.selectedState || this.selectedState.id !== newValue) {
          const state = this.states.filter((state) => state.id === newValue)[0];
          this.selectedState = state;
          this.selectedStateCities = this.getStateCities(state);
        }
      },

      updateStates() {
        if (this.states.length) {
          this.parseStatesList();
          return;
        }

        this.$store
          .dispatch(FETCH_STATES)
          .then(() => this.parseStatesList())
          .catch(() => {
            this.$emit("error", "Erro ao recuperar a lista de estados");
          });
      },

      getStateCities(state) {
        if (
          state &&
          state.abbrev !== undefined in this.stateCities &&
          this.stateCities[state.abbrev] !== undefined
        ) {
          this.parseSelectedStateCitiesList(this.stateCities[state.abbrev]);
          return;
        }

        this.$store
          .dispatch(FETCH_STATE_CITIES, { state: state })
          .then((cities) => {
            this.parseSelectedStateCitiesList(cities);
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

        if (this.initialData.state) {
          this.$refs.profile_state.setValue(this.initialData.state);
        }
      },

      parseSelectedStateCitiesList(cities) {
        this.selectedStateCities = cities.map((obj) => {
          return {
            text: obj.name,
            value: obj.id,
          };
        });
      },

      changedSpecialNeeds() {
        this.displaySpecialNeeds = this.$refs.profile_special_needs.getValue();
      },

      changedOtherAccommodations() {
        this.needsOtherAccommodation = this.$refs.profile_other_accommodation.getValue();
      },

      changedSpecialAccommodations() {
        this.displaySpecialAccommodations = this.$refs.profile_accommodations.getValue();
      },

      changedHasOtherDisability() {
        this.hasOtherDisability = this.$refs.profile_other_disability.getValue();
      },

      updateFields() {
        let fields = [
          this.$refs.profile_name,
          this.$refs.profile_email,
          this.$refs.profile_rg,
          this.$refs.profile_cpf,
          this.$refs.profile_birthdate,
          this.$refs.profile_address,
          this.$refs.profile_number,
          this.$refs.profile_complement,
          this.$refs.profile_state,
          this.$refs.profile_city,
          this.$refs.profile_zipcode,
          this.$refs.profile_phone,
          this.$refs.profile_special_needs,
          this.$refs.profile_auditive_disability,
          this.$refs.profile_physical_disability,
          this.$refs.profile_mental_disability,
          this.$refs.profile_motor_disability,
          this.$refs.profile_visual_disability,
          this.$refs.profile_other_disability,
          this.$refs.profile_other_disability_detail,
          this.$refs.profile_cid,
          this.$refs.profile_doctor,
          this.$refs.profile_accommodations,
          this.$refs.profile_accommodation_reader,
          this.$refs.profile_accommodation_enlarged_exam,
          this.$refs.profile_accommodation_typist,
          this.$refs.profile_other_accommodation,
          this.$refs.profile_other_accommodation_detail,
        ];
        fields = fields.filter((field) => field !== undefined);

        if (this.fields.length !== fields.length) {
          this.fields = fields;
        }
      },
    },
  };
</script>
