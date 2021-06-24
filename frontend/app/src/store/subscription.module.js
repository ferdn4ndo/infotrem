import {
  SubscriptionsService,
  SubscriptionEligibilityService,
} from "@/common/api.service";
import {
  FETCH_SUBSCRIPTION,
  FETCH_SUBSCRIPTIONS,
  CHECK_SUBSCRIPTION_ELIGIBILITY, REMOVE_SUBSCRIPTION,
} from "./actions.type";
import {
  APPEND_SUBSCRIPTIONS,
  SET_SUBSCRIPTIONS,
  SET_LOADING,
  RESET_LOADING,
} from "./mutations.type";

const PAGINATION_SIZE = 20;

const initialState = {
  subscriptions: [],
  hasMoreSubscriptions: false,
  subscriptionsOffset: 0,
};

export const state = { ...initialState };

export const actions = {
  async [FETCH_SUBSCRIPTION]({ commit }, subscriptionId) {
    return SubscriptionsService.get(subscriptionId)
      .then(({ data }) => {
        commit(APPEND_SUBSCRIPTIONS, data);

        return data;
      })
      .catch((error) => {
        throw new Error(error);
      });
  },

  async [FETCH_SUBSCRIPTIONS]({ commit }, params) {
    commit(SET_LOADING, "subscriptions");
    commit(SET_SUBSCRIPTIONS, []);

    let queryParams = params === undefined ? {} : params;
    queryParams.offset = state.subscriptionsOffset;
    queryParams.limit = PAGINATION_SIZE;

    return SubscriptionsService.query(queryParams)
      .then(({ data }) => {
        state.subscriptionsOffset =
          state.subscriptionsOffset + data.items.length;
        state.hasMoreSubscriptions = state.subscriptionsOffset < data.count;

        commit(APPEND_SUBSCRIPTIONS, data.items);
        commit(RESET_LOADING, "subscriptions");
      })
      .catch((error) => {
        commit(RESET_LOADING, "subscriptions");
        throw new Error(error);
      });
  },

  async [CHECK_SUBSCRIPTION_ELIGIBILITY]({ commit }, params) {
    commit(SET_LOADING, "subscription_eligibility");

    return SubscriptionEligibilityService.check(params)
      .then(({ data }) => {
        commit(RESET_LOADING, "subscription_eligibility");
        return data;
      })
      .catch((error) => {
        commit(RESET_LOADING, "subscription_eligibility");
        throw new Error(error);
      });
  },

  async [REMOVE_SUBSCRIPTION]({ commit }, params) {
    commit(SET_LOADING, "subscription_remove");

    return SubscriptionsService.delete(params)
      .then(({ data }) => {
        commit(RESET_LOADING, "subscription_remove");
        return data;
      })
      .catch((error) => {
        commit(RESET_LOADING, "subscription_remove");
        throw new Error(error);
      });
  },
};

/* eslint no-param-reassign: ["error", { "props": false }] */
export const mutations = {
  [SET_SUBSCRIPTIONS](state, subscriptions) {
    state.subscriptions = subscriptions;
  },
  [APPEND_SUBSCRIPTIONS](state, subscriptions) {
    let filteredSubs = state.subscriptions.filter((stateSubscription) => {
      return (
        subscriptions.filter((subscription) => {
          return subscription.id === stateSubscription.id;
        }).length === 0
      );
    });

    filteredSubs.push(...subscriptions);

    state.subscriptions = filteredSubs;
  },
};

const getters = {
  subscriptions(state) {
    return state.subscriptions;
  },
};

export default {
  state,
  actions,
  mutations,
  getters,
};
