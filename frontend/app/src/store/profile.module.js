import ApiService from "@/common/api.service";
import { FETCH_USER, UPDATE_PROFILE } from "./actions.type";
import {
  SET_ERROR,
  SET_USER,
  SET_LOADING,
  RESET_LOADING,
} from "./mutations.type";

const state = {
  errors: {},
  profile: {},
};

const getters = {
  profile(state) {
    return state.profile;
  },
};

const actions = {
  [FETCH_USER](context) {
    return new Promise((resolve, reject) => {
      context.commit(SET_LOADING, "fetch_user");
      ApiService.get("me")
        .then(({ data }) => {
          context.commit(SET_USER, data);
          context.commit(RESET_LOADING, "fetch_user");
          resolve(data);
        })
        .catch((response) => {
          context.commit(RESET_LOADING, "fetch_user");
          reject(response);
        });
    });
  },
  [UPDATE_PROFILE](context, payload) {
    return new Promise((resolve, reject) => {
      context.commit(SET_LOADING, "update_user");
      ApiService.patch("me", payload)
        .then((response) => {
          context.commit(RESET_LOADING, "update_user");
          context.commit(SET_USER, response.data);
          resolve(response);
        })
        .catch((response) => {
          context.commit(RESET_LOADING, "fetch_user");
          reject(response);
        });
    });
  },
};

const mutations = {
  [SET_ERROR](state, error) {
    state.errors = error;
  },
};

export default {
  state,
  actions,
  mutations,
  getters,
};
