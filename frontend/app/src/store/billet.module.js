import { BilletGatewayService, BilletService } from "@/common/api.service";
import {
  FETCH_BILLET,
  FETCH_BILLETS,
  FETCH_BILLET_GATEWAYS,
} from "./actions.type";
import {
  APPEND_BILLET,
  SET_BILLETS,
  SET_BILLET_GATEWAYS,
  SET_LOADING,
  RESET_LOADING,
} from "./mutations.type";

const PAGINATION_SIZE = 20;

const initialState = {
  billets: [],
  billetsOffset: 0,
  billetGateways: [],
  hasMoreBillets: false,
};

export const state = { ...initialState };

export const actions = {
  async [FETCH_BILLET]({ commit }, billetId) {
    return BilletService.get(billetId)
      .then(({ data }) => {
        commit(APPEND_BILLET, data);
        return data;
      })
      .catch((error) => {
        throw new Error(error);
      });
  },

  async [FETCH_BILLETS]({ commit }, params) {
    commit(SET_LOADING, "billets");

    let queryParams = params === undefined ? {} : params;
    queryParams.offset = state.billetsOffset;
    queryParams.limit = PAGINATION_SIZE;

    return BilletService.query(queryParams)
      .then(({ data }) => {
        state.billetsOffset = state.billetsOffset + data.items.length;
        state.hasMoreBillets = state.billetsOffset < data.count;

        data.items.map((billet) => {
          commit(APPEND_BILLET, billet);
        });

        commit(RESET_LOADING, "billets");

        return data;
      })
      .catch((error) => {
        commit(RESET_LOADING, "billets");
        throw new Error(error);
      });
  },

  async [FETCH_BILLET_GATEWAYS]({ commit }, params) {
    commit(SET_LOADING, "billet_gateways");

    return BilletGatewayService.query(params)
      .then(({ data }) => {
        commit(RESET_LOADING, "billet_gateways");
        commit(SET_BILLET_GATEWAYS, data.items);
        return data.items;
      })
      .catch((error) => {
        commit(RESET_LOADING, "billet_gateways");
        throw new Error(error);
      });
  },
};

/* eslint no-param-reassign: ["error", { "props": false }] */
export const mutations = {
  [SET_BILLETS](state, billets) {
    state.billets = billets;
  },
  [SET_BILLET_GATEWAYS](state, billet_gateways) {
    state.billetGateways = billet_gateways;
  },
  [APPEND_BILLET](state, billet) {
    let filteredBillets = state.billets.filter((stateBillet) => {
      return stateBillet.id !== billet.id;
    });

    state.billets = filteredBillets.push(billet);
  },
};

const getters = {
  billetGateways(state) {
    return state.billetGateways;
  },
  billets(state) {
    return state.billets;
  },
};

export default {
  state,
  actions,
  mutations,
  getters,
};
