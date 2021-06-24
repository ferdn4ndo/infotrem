import { LocationsService } from "@/common/api.service";
import {
  FETCH_CITY,
  FETCH_STATE,
  FETCH_STATES,
  FETCH_STATE_CITIES,
} from "./actions.type";
import {
  RESET_LOADING,
  RESET_STATES,
  RESET_STATE_CITIES,
  SET_LOADING,
  SET_STATES,
  SET_STATE_CITIES,
  SET_STATE,
  SET_CITY,
  RESET_CITY,
} from "./mutations.type";

const initialState = {
  cities: [],
  states: [],
  stateCities: {},
};

export const state = { ...initialState };

export const actions = {
  async [FETCH_CITY](context, params, prevEvent) {
    if (prevEvent !== undefined) {
      return context.commit(SET_CITY, prevEvent);
    }

    context.commit(SET_LOADING, "city");
    let response = await LocationsService.getStateCity(
      params.stateId,
      params.cityId
    );
    let city = response.data;
    context.commit(SET_CITY, city);
    context.commit(RESET_LOADING, "city");

    return city;
  },

  async [FETCH_STATE](context, stateId, prevEvent) {
    if (prevEvent !== undefined) {
      return context.commit(SET_CITY, prevEvent);
    }

    context.commit(SET_LOADING, "state");
    let response = await LocationsService.getState(stateId);
    let state = response.data;
    context.commit(SET_STATE, state);
    context.commit(RESET_LOADING, "state");

    return state;
  },

  async [FETCH_STATES](context, params, prevEvent) {
    // avoid extra network call if event exists
    if (prevEvent !== undefined) {
      return context.commit(SET_STATES, prevEvent);
    }

    context.commit(SET_LOADING, "states");
    context.commit(RESET_STATES);
    let offset = 0;
    let limit = 100;
    let response = await LocationsService.queryStates({
      offset: offset,
      limit: limit,
    });
    let states = response.data.items;

    while (typeof response.data._links.next !== "undefined" && response.data._links.next.href !== null) {
      offset += response.data.items.length;
      response = await LocationsService.queryStates({
        offset: offset,
        limit: limit,
      });
      states = states.concat(response.data.items);
    }

    context.commit(SET_STATES, states);
    context.commit(RESET_LOADING, "states");
    return states;
  },

  async [FETCH_STATE_CITIES](context, params, prevEvent) {
    // avoid extra network call if event exists
    if (prevEvent !== undefined) {
      return context.commit(SET_STATE_CITIES, prevEvent);
    }

    context.commit(SET_LOADING, "cities");
    context.commit(RESET_STATE_CITIES);
    let offset = 0;
    let response = await LocationsService.queryStateCities(params["state"].id, {
      offset: offset,
    });
    let cities = response.data.items;

    while (typeof response.data._links.next !== "undefined" && response.data._links.next.href !== null) {
      offset += response.data.items.length;
      response = await LocationsService.queryStateCities(params["state"].id, {
        offset: offset,
      });
      cities = cities.concat(response.data.items);
    }

    context.commit(SET_STATE_CITIES, {
      abbrev: params["state"].abbrev,
      cities: cities,
    });
    context.commit(RESET_LOADING, "cities");
    return cities;
  },
};

/* eslint no-param-reassign: ["error", { "props": false }] */
export const mutations = {
  [RESET_CITY](state, city_id) {
    state.citiesByUuid = state.citiesByUuid.filter((city) => {
      return city.id !== city_id;
    });
  },

  [SET_CITY](state, city_data) {
    state.cities = state.cities.filter((city) => {
      return city.id !== city_data.id;
    });

    state.cities.push(city_data);
  },

  [SET_STATE](state, state_data) {
    state.states = state.states.filter((stored_state) => {
      return stored_state.id !== state_data.id;
    });

    state.states.push(state_data);
  },

  [RESET_STATES](state) {
    state.states = [];
    state.stateCities = {};
  },

  [SET_STATES](state, states) {
    state.states = states;
  },

  [RESET_STATE_CITIES](state, stateAbbrev) {
    state.stateCities[stateAbbrev] = [];
  },

  [SET_STATE_CITIES](state, params) {
    let stateAbbrev = params.abbrev;

    if (stateAbbrev !== undefined) {
      state.stateCities[params.abbrev] = params.cities;
    }
  },
};

const getters = {
  cities(state) {
    return state.cities;
  },

  states(state) {
    return state.states;
  },

  stateCities(state) {
    return state.stateCities;
  },
};

export default {
  state,
  actions,
  mutations,
  getters,
};
