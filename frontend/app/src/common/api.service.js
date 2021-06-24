import axios from "axios";
import JwtService from "@/common/jwt.service";

const DEFAULT_CONTENT_TYPE = "application/json";

const apiAxios = axios.create({
  baseURL: process.env.VUE_APP_API_URL,
  timeout: 10000,
  headers: {
    'Content-Type': DEFAULT_CONTENT_TYPE,
  },
});

const ApiService = {
  init() {
    apiAxios.defaults.baseURL = process.env.VUE_APP_API_URL;

    // Add a request interceptor
    apiAxios.interceptors.request.use(function(config) {
      const token = JwtService.getToken();
      if (token !== "undefined" && token !== null) {
        config.headers.Authorization = `Token ${token}`;
      }
      return config;
    });
  },

  query(resource, params) {
    return apiAxios.get(resource, params);
  },

  get(resource, slug = "") {
    let url = slug ? `${resource}/${slug}` : resource;
    return apiAxios.get(url);
  },

  post(resource, params) {
    return apiAxios.post(`${resource}`, params, {
      headers: {
        "Content-Type": "application/json",
      },
    });
  },

  patch(resource, params) {
    return apiAxios.patch(`${resource}`, params, {
      headers: {
        "Content-Type": "application/json",
      },
    });
  },

  put(resource, params) {
    return apiAxios.put(`${resource}`, params, {
      headers: {
        "Content-Type": "application/json",
      },
    });
  },

  delete(resource) {
    return apiAxios.delete(resource);
  },
};

export default ApiService;

export const LocationsService = {
  queryStates(params) {
    return ApiService.query("states/", { params: params });
  },

  getState(stateId = "") {
    return ApiService.get(`states/${stateId}/`);
  },

  queryStateCities(stateId, params) {
    return ApiService.query(`states/${stateId}/cities/`, { params: params });
  },

  getStateCity(stateId, cityId) {
    return ApiService.get(`states/${stateId}/cities/${cityId}/`);
  },
};

export const EventsService = {
  query(params) {
    return ApiService.query("events/", { params: params });
  },

  get(slug = "") {
    return ApiService.get(`events/${slug}/`);
  },

  post(params) {
    return ApiService.post(`events/`, params);
  },

  patch(slug = "", params) {
    return ApiService.patch(`events/${slug}/`, params);
  },
};

export const EventSubscriptionsService = {
  query(eventId, params) {
    return ApiService.query(`events/${eventId}/subscriptions/`, {
      params: params,
    });
  },

  get(eventId, slug = "") {
    return ApiService.get(`events/${eventId}/subscriptions/${slug}/`);
  },
};

export const EventFilesService = {
  query(eventId, params) {
    return ApiService.query(`events/${eventId}/files/`, {
      params: params,
    });
  },

  get(eventId, slug = "") {
    return ApiService.get(`events/${eventId}/files/${slug}/`);
  },

  post(eventId, params) {
    return ApiService.post(`events/${eventId}/files/`, params);
  },

  patch(eventId, slug = "", params) {
    return ApiService.patch(`events/${eventId}/files/${slug}/`, params);
  },

  delete(eventId, slug = "") {
    return ApiService.delete(`events/${eventId}/files/${slug}/`);
  },
};

export const EventLinksService = {
  query(eventId, params) {
    return ApiService.query(`events/${eventId}/links/`, {
      params: params,
    });
  },

  get(eventId, slug = "") {
    return ApiService.get(`events/${eventId}/links/${slug}/`);
  },

  post(eventId, params) {
    return ApiService.post(`events/${eventId}/links/`, params);
  },

  patch(eventId, slug = "", params) {
    return ApiService.patch(`events/${eventId}/links/${slug}/`, params);
  },

  delete(eventId, slug = "") {
    return ApiService.delete(`events/${eventId}/links/${slug}/`);
  },
};

export const EventVacancySubscriptionService = {
  post(eventId, vacancyId) {
    return ApiService.post(
      `events/${eventId}/vacancies/${vacancyId}/subscribe/`,
      {}
    );
  },
};

export const SubscriptionsService = {
  query(params) {
    return ApiService.query("subscriptions/", { params: params });
  },

  get(slug = "") {
    return ApiService.get(`subscriptions/${slug}/`);
  },

  delete(slug = "") {
    return ApiService.delete(`subscriptions/${slug}/`);
  },
};

export const SubscriptionEligibilityService = {
  check(params) {
    return ApiService.post(`subscription-eligibility/check`, params);
  },
};

export const EmailValidationService = {
  post() {
    return ApiService.query("email-validation/resend/", {});
  },

  get(userId = "", validationHash = "") {
    return ApiService.get(
      `email-validation/check/${userId}/${validationHash}/`
    );
  },
};

export const BilletService = {
  query(params) {
    return ApiService.query("billets/", { params: params });
  },

  get(slug = "") {
    return ApiService.get(`billets/${slug}/`);
  },
};

export const BilletGatewayService = {
  query(params) {
    return ApiService.query("billet-gateways/", { params: params });
  },

  get(slug = "") {
    return ApiService.get(`billet-gateways/${slug}/`);
  },
};
