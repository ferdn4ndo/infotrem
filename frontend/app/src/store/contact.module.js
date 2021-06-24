import ApiService from "@/common/api.service";
import { CREATE_CONTACT } from "./actions.type";
import { SET_LOADING, RESET_LOADING } from "./mutations.type";

const state = {
  errors: null,
};

const getters = {};

const actions = {
  [CREATE_CONTACT](context, data) {
    return new Promise((resolve, reject) => {
      context.commit(SET_LOADING, "contact");
      ApiService.post("contact", data)
        .then((response) => {
          context.commit(RESET_LOADING, "contact");
          resolve(response);
        })
        .catch((response) => {
          context.commit(RESET_LOADING, "contact");
          reject(response);
        });
    });
  },
};

const mutations = {};

export default {
  state,
  actions,
  mutations,
  getters,
};
