import {
  EventsService,
  EventFilesService,
  EventLinksService,
  EventSubscriptionsService,
  EventVacancySubscriptionService,
} from "@/common/api.service";
import {
  CREATE_EVENT,
  CREATE_EVENT_FILE,
  CREATE_EVENT_LINK,
  CREATE_VACANCY_SUBSCRIPTION,
  FETCH_EVENT,
  UPDATE_EVENT,
  FETCH_EVENT_SUBSCRIPTIONS,
  REMOVE_EVENT_FILE,
  REMOVE_EVENT_LINK,
  UPDATE_EVENT_FILE,
  UPDATE_EVENT_LINK,
} from "./actions.type";
import {
  SET_EVENT,
  SET_LOADING,
  RESET_LOADING,
  APPEND_SUBSCRIPTIONS,
  APPEND_EVENTS,
} from "./mutations.type";

const initialState = {
  events: [],
};

export const state = { ...initialState };

export const actions = {
  async [FETCH_EVENT](context, eventSlug, prevEvent) {
    context.commit(SET_LOADING, "event");

    if (prevEvent !== undefined) {
      return context.commit(SET_EVENT, prevEvent);
    }

    const { data } = await EventsService.get(eventSlug);
    context.commit(SET_EVENT, data);
    context.commit(RESET_LOADING, "event");

    return data;
  },

  async [FETCH_EVENT_SUBSCRIPTIONS](context, eventSlug, prevEvent) {
    context.commit(SET_LOADING, "event_subscriptions");

    if (prevEvent !== undefined) {
      return prevEvent;
    }

    const { data } = await EventSubscriptionsService.query(eventSlug);
    context.commit(RESET_LOADING, "event_subscriptions");

    return data;
  },

  async [CREATE_VACANCY_SUBSCRIPTION](context, params, prevSubscriptionCall) {
    if (prevSubscriptionCall !== undefined) {
      return context.commit(APPEND_SUBSCRIPTIONS, [prevSubscriptionCall]);
    }

    context.commit(SET_LOADING, "vacancy_subscription");

    return EventVacancySubscriptionService.post(
      params.event.id,
      params.vacancy.id
    )
      .then(({ data }) => {
        context.commit(APPEND_SUBSCRIPTIONS, [data]);
        context.commit(RESET_LOADING, "vacancy_subscription");

        return data;
      })
      .catch((error) => {
        context.commit(RESET_LOADING, "vacancy_subscription");
        throw new Error(error);
      });
  },

  async [CREATE_EVENT](context, data, prevSubscriptionCall) {
    if (prevSubscriptionCall !== undefined) {
      return context.commit(APPEND_EVENTS, [prevSubscriptionCall]);
    }

    context.commit(SET_LOADING, "create_event");

    return EventsService.post(data.payload)
      .then((responseData) => {
        context.commit(APPEND_EVENTS, [responseData.data]);
        context.commit(RESET_LOADING, "create_event");

        return responseData;
      })
      .catch((error) => {
        context.commit(RESET_LOADING, "create_event");
        throw new Error(error);
      });
  },

  async [UPDATE_EVENT](context, data, prevSubscriptionCall) {
    if (prevSubscriptionCall !== undefined) {
      return context.commit(APPEND_EVENTS, [prevSubscriptionCall]);
    }

    context.commit(SET_LOADING, "update_event");

    return EventsService.patch(data.event_id, data.payload)
      .then((responseData) => {
        context.commit(APPEND_EVENTS, [responseData.data]);
        context.commit(RESET_LOADING, "update_event");

        return responseData;
      })
      .catch((error) => {
        context.commit(RESET_LOADING, "update_event");
        throw new Error(error);
      });
  },

  [CREATE_EVENT_FILE](context, params, prevSubscriptionCall) {
    if (prevSubscriptionCall !== undefined) {
      return context.commit(CREATE_EVENT_FILE, [prevSubscriptionCall]);
    }

    context.commit(SET_LOADING, "create_event_file");

    return EventFilesService.post(params.event_id, params.payload)
      .then(({ data }) => {
        context.commit(APPEND_EVENTS, [data]);

        return EventsService.get(params.event_id).then((eventData) => {
          context.commit(RESET_LOADING, "create_event_file");
          context.commit(SET_EVENT, eventData);

          return data;
        }).catch((error) => {
          context.commit(RESET_LOADING, "create_event_file");
          throw new Error(error);
        });
      })
      .catch((error) => {
        context.commit(RESET_LOADING, "create_event_file");
        throw new Error(error);
      });
  },

  [UPDATE_EVENT_FILE](context, params, prevCall) {
    if (prevCall !== undefined) {
      return prevCall;
    }

    context.commit(SET_LOADING, "update_event_file");

    return EventFilesService.patch(params.event_id, params.file_id, params)
      .then(({ data }) => {
        return EventsService.get(params.event_id).then((eventData) => {
          context.commit(RESET_LOADING, "update_event_file");
          context.commit(SET_EVENT, eventData);

          return data;
        }).catch((error) => {
          context.commit(RESET_LOADING, "update_event_file");
          throw new Error(error);
        });
      })
      .catch((error) => {
        context.commit(RESET_LOADING, "update_event_file");
        throw new Error(error);
      });
  },

  [REMOVE_EVENT_FILE](context, params, prevCall) {
    if (prevCall !== undefined) {
      return prevCall;
    }

    context.commit(SET_LOADING, "remove_event_file");

    return EventFilesService.delete(params.event_id, params.file_id)
      .then(({ data }) => {
        return EventsService.get(params.event_id).then((eventData) => {
          context.commit(RESET_LOADING, "remove_event_file");
          context.commit(SET_EVENT, eventData);

          return data;
        }).catch((error) => {
          context.commit(RESET_LOADING, "remove_event_file");
          throw new Error(error);
        });
      })
      .catch((error) => {
        context.commit(RESET_LOADING, "remove_event_file");
        throw new Error(error);
      });
  },

  [CREATE_EVENT_LINK](context, params, previousCall) {
    return new Promise((resolve, reject) => {
      if (previousCall !== undefined) {
        return previousCall;
      }
      context.commit(SET_LOADING, "create_event_link");

      EventLinksService.post(params.event_id, params.payload)
        .then(({ data }) => {
          context.commit(APPEND_EVENTS, [data]);

          EventsService.get(params.event_id).then((eventData) => {
            context.commit(RESET_LOADING, "create_event_link");
            context.commit(SET_EVENT, eventData);

            resolve(data);
          }).catch((error) => {
            context.commit(RESET_LOADING, "create_event_link");
            reject(error);
          });
        })
        .catch((error) => {
          context.commit(RESET_LOADING, "create_event_link");
          reject(error);
        });
    });
  },

  [UPDATE_EVENT_LINK](context, params, previousCall) {
    return new Promise((resolve, reject) => {
      if (previousCall !== undefined) {
        return previousCall;
      }

      context.commit(SET_LOADING, "update_event_link");

      EventLinksService.patch(params.event_id, params.link_id, params)
        .then(({ data }) => {
          EventsService.get(params.event_id).then((eventData) => {
            context.commit(RESET_LOADING, "update_event_link");
            context.commit(SET_EVENT, eventData);

            resolve(data);
          }).catch((error) => {
            context.commit(RESET_LOADING, "update_event_link");
            reject(error);
          });
        })
        .catch((error) => {
          context.commit(RESET_LOADING, "update_event_link");
          reject(error);
        });
    });
  },

  [REMOVE_EVENT_LINK](context, params, previousCall) {
    return new Promise((resolve, reject) => {
      if (previousCall !== undefined) {
        return previousCall;
      }

    context.commit(SET_LOADING, "remove_event_link");

    EventLinksService.delete(params.event_id, params.link_id)
      .then(({ data }) => {
        EventsService.get(params.event_id).then((eventData) => {
          context.commit(RESET_LOADING, "remove_event_link");
          context.commit(SET_EVENT, eventData);

          resolve(data);
        }).catch((error) => {
          context.commit(RESET_LOADING, "remove_event_link");
          reject(error);
        });
      })
      .catch((error) => {
        context.commit(RESET_LOADING, "remove_event_link");
        reject(error);
      });
    });
  },
};

/* eslint no-param-reassign: ["error", { "props": false }] */
export const mutations = {
  [SET_EVENT](state, event) {
    let filteredEvents = state.events.filter((stateEvent) => {
      return stateEvent.id !== event.id;
    });
    filteredEvents.push(event);

    state.events = filteredEvents;
  },
};

const getters = {
  events(state) {
    return state.events;
  },
};

export default {
  state,
  actions,
  mutations,
  getters,
};
