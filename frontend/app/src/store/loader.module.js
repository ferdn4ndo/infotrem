import { SET_LOADING, RESET_LOADING } from "./mutations.type";

const state = {
  loadingProccesses: [],
};

const getters = {
  isLoading(state) {
    return state.loadingProccesses.length > 0;
  },
};

const actions = {};

/* eslint no-param-reassign: ["error", { "props": false }] */
const mutations = {
  [SET_LOADING](state, proccessName) {
    if (state.loadingProccesses.indexOf(proccessName) === -1) {
      state.loadingProccesses.push(proccessName);
    }
  },

  [RESET_LOADING](state, proccessName) {
    state.loadingProccesses = state.loadingProccesses.filter(
      (proccess) => proccess !== proccessName
    );
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
