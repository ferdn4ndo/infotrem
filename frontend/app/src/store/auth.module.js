import ApiService from "@/common/api.service";
import JwtService from "@/common/jwt.service";
import { LOGIN, LOGOUT, REGISTER, CHECK_AUTH } from "./actions.type";
import {
  SET_AUTH,
  PURGE_AUTH,
  RESET_LOADING,
  SET_LOADING,
  SET_USER,
} from "./mutations.type";

const state = {
  user: null,
  token: JwtService.getToken(),
  expiresAt: JwtService.getExp(),
  isAuthenticated: !!JwtService.getToken(),
};

const getters = {
  isAuthenticated(state) {
    return state.isAuthenticated;
  },

  currentUser(state) {
    return state.user;
  },
};

const actions = {
  [LOGIN](context, credentials) {
    return new Promise((resolve, reject) => {
      context.commit(SET_LOADING, "login");
      ApiService.post("login", credentials)
        .then((loginResponse) => {
          context.commit(SET_AUTH, loginResponse.data);

          ApiService.get("me")
            .then((response) => {
              context.commit(RESET_LOADING, "login");
              context.commit(SET_USER, response.data);

              resolve(loginResponse);
            })
            .catch(() => {
              context.commit(RESET_LOADING, "login");
              context.commit(PURGE_AUTH);

              reject(loginResponse);
            });
        })
        .catch((response) => {
          context.commit(RESET_LOADING, "login");

          reject(response);
        });
    });
  },
  [LOGOUT](context) {
    context.commit(PURGE_AUTH);
  },
  [REGISTER](context, formData) {
    return new Promise((resolve, reject) => {
      context.commit(SET_LOADING, "register");
      ApiService.post("register", formData)
        .then((response) => {
          context.commit(SET_AUTH, response.data);
          context.commit(RESET_LOADING, "register");
          resolve(response);
        })
        .catch((response) => {
          context.commit(RESET_LOADING, "register");
          reject(response);
        });
    });
  },
  [CHECK_AUTH](context) {
    const token = JwtService.getToken();
    if (token !== "undefined" && token !== null) {
      context.commit(SET_LOADING, "check_auth");
      ApiService.get("me")
        .then((response) => {
          context.commit(RESET_LOADING, "check_auth");
          context.commit(SET_USER, response.data);
        })
        .catch(() => {
          context.commit(RESET_LOADING, "check_auth");
          context.commit(PURGE_AUTH);
        });
    } else {
      context.commit(PURGE_AUTH);
    }
  },
};

const mutations = {
  [SET_AUTH](state, data) {
    state.isAuthenticated = true;
    state.token = data.access_token;
    state.expiresAt = data.access_token_exp;
    JwtService.saveToken(data.access_token);
  },
  [PURGE_AUTH](state) {
    state.isAuthenticated = false;
    state.token = null;
    state.expiresAt = null;
    JwtService.destroyToken();
  },
  [SET_USER](state, data) {
    state.user = data;
  },
};

export default {
  state,
  actions,
  mutations,
  getters,
};
