import { EventsService } from "@/common/api.service";
import {
  CLEAR_EVENTS,
  FETCH_EVENTS,
  FETCH_SLIDES,
  OPEN_MODAL,
} from "./actions.type";
import {
  APPEND_EVENTS,
  INCREMENT_EVENTS_OFFSET,
  RESET_LOADING,
  SET_EVENTS,
  SET_EVENT,
  SET_LOADING,
  SET_SLIDES,
  SET_HAS_OPEN_MODAL,
  SET_HAS_MORE_EVENTS,
} from "./mutations.type";
import moment from "moment";

const PAGINATION_SIZE = 10;

const state = {
  events: [],
  eventsOpen: [],
  eventsOngoing: [],
  eventsClosed: [],
  eventsOpenCount: 0,
  eventsOngoingCount: 0,
  eventsClosedCount: 0,
  eventsTotalCount: 0,
  hasMoreEvents: false,
  hasOpenModal: false,
  currentOffset: 0,
  slides: [],
  slidesAreLoading: true,
};

const getters = {
  eventsOpenCount(state) {
    return parseInt(state.eventsOpenCount);
  },

  eventsOngoingCount(state) {
    return parseInt(state.eventsOngoingCount);
  },

  eventsClosedCount(state) {
    return parseInt(state.eventsClosedCount);
  },

  eventsTotalCount(state) {
    return parseInt(state.eventsTotalCount);
  },

  eventsOpen(state) {
    return state.eventsOpen;
  },

  eventsOngoing(state) {
    return state.eventsOngoing;
  },

  eventsClosed(state) {
    return state.eventsClosed;
  },

  hasOpenModal(state) {
    return state.hasOpenModal;
  },

  slides(state) {
    return state.slides;
  },

  slidesAreLoading(state) {
    return state.slidesAreLoading;
  },

  hasMoreEvents(state) {
    return state.hasMoreEvents;
  },

  currentOffset(state) {
    return state.currentOffset;
  },
};

const actions = {
  [FETCH_SLIDES]({ commit }) {
    let data = {
      items: [
        {
          imageSrc: "img/backgrounds/csc-01.jpg",
          text:
            "Empresa que mais se destacou no mercado pelas inovações para adaptação em relação à pandemia, focando na segurança de todos",
          imageAlt: "A imagem contém um fundo abstrato com a logomarca da CSC",
        },
        {
          imageSrc: "img/backgrounds/csc-02.jpg",
          text:
            "Empresa líder nos segmentos de Concursos Públicos, Processos Seletivos e Capacitações",
          imageAlt: "A imagem contém um fundo abstrato com a logomarca da CSC",
        },
        {
          imageSrc: "img/backgrounds/csc-03.jpg",
          text: "Trabalhamos com integridade, honestidade e seriedade",
          imageAlt: "A imagem contém um fundo abstrato com a logomarca da CSC",
        },
      ],
    };

    commit(SET_LOADING, "slides");

    let imageLoaded = 0;
    data.items.forEach((slide) => {
      const img = new Image();
      img.src = slide.imageSrc;

      img.onload = () => {
        imageLoaded++;

        if (imageLoaded === data.items.length) {
          commit(RESET_LOADING, "slides");
        }
      };
    });

    commit(SET_SLIDES, data);
  },

  [FETCH_EVENTS]({ commit }, params) {
    commit(SET_LOADING, "events");
    let queryParams = params === undefined ? {} : params;
    queryParams.offset = queryParams.hasOwnProperty("offset")
      ? queryParams.offset
      : state.currentOffset;
    queryParams.limit = queryParams.hasOwnProperty("limit")
      ? queryParams.limit
      : PAGINATION_SIZE;

    return EventsService.query(queryParams)
      .then(({ data }) => {
        commit(APPEND_EVENTS, data.items);

        data.items.map((event) => {
          commit(SET_EVENT, event);
        });

        commit(SET_HAS_MORE_EVENTS, state.currentOffset < data.count);
        commit(INCREMENT_EVENTS_OFFSET, data.items.length);

        commit(RESET_LOADING, "events");
      })
      .catch((error) => {
        commit(RESET_LOADING, "events");
        throw new Error(error);
      });
  },

  [CLEAR_EVENTS]({ commit }) {
    state.currentOffset = 0;
    commit(SET_EVENTS, []);
  },

  [OPEN_MODAL]({ commit }, value) {
    commit(SET_HAS_OPEN_MODAL, value);
  },
};

function filterByDateRange(events, start_field, end_field = null) {
  return events.filter(function(event) {
    let now = moment();
    let start = moment(event[start_field]);

    if (end_field) {
      let end = moment(event[end_field]);
      return start <= now && now <= end;
    }

    return start <= now;
  });
}

/* eslint no-param-reassign: ["error", { "props": false }] */
const mutations = {
  [SET_EVENTS](state, events) {
    state.events = events;
    state.eventsOpen = filterByDateRange(
      state.events,
      "registration_start_date",
      "registration_end_date"
    );
    state.eventsOngoing = filterByDateRange(
      state.events,
      "registration_end_date",
      "results_final_date"
    );
    state.eventsClosed = filterByDateRange(state.events, "results_final_date");

    state.eventsOpenCount = state.eventsOpen.length;
    state.eventsOngoingCount = state.eventsOngoing.length;
    state.eventsClosedCount = state.eventsClosed.length;
    state.eventsTotalCount = events.length;
  },

  [APPEND_EVENTS](state, items) {
    let filteredEvents = state.events.filter((stateEvent) => {
      return (
        items.filter((event) => {
          return stateEvent.id === event.id;
        }).length === 0
      );
    });

    filteredEvents.push(...items);
    state.events = filteredEvents;

    state.eventsOpen = filterByDateRange(
      state.events,
      "registration_start_date",
      "registration_end_date"
    );
    state.eventsOngoing = filterByDateRange(
      state.events,
      "registration_end_date",
      "results_final_date"
    );
    state.eventsClosed = filterByDateRange(state.events, "results_final_date");

    state.eventsOpenCount = state.eventsOpen.length;
    state.eventsOngoingCount = state.eventsOngoing.length;
    state.eventsClosedCount = state.eventsClosed.length;
    state.eventsTotalCount = state.events.length;
  },

  [INCREMENT_EVENTS_OFFSET](state, value) {
    state.currentOffset = state.currentOffset + parseInt(value);
  },

  [SET_HAS_MORE_EVENTS](state, value) {
    state.hasMoreEvents = value;
  },

  [SET_SLIDES](state, data) {
    state.slides = data.items;
  },

  [SET_HAS_OPEN_MODAL](state, value) {
    state.hasOpenModal = value;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
