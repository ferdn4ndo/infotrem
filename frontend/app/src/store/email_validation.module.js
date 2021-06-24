import { EmailValidationService } from "@/common/api.service";
import { VALIDATE_EMAIL } from "./actions.type";
import { SET_LOADING, RESET_LOADING } from "./mutations.type";

const state = {};

const getters = {};

const actions = {
  [VALIDATE_EMAIL](context, params) {
    return new Promise((resolve, reject) => {
      console.log(params);
      context.commit(SET_LOADING, "email-validation");
      EmailValidationService.get(params.userId, params.hash)
        .then((response) => {
          context.commit(RESET_LOADING, "email-validation");
          resolve(response);
        })
        .catch((response) => {
          context.commit(RESET_LOADING, "email-validation");
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
