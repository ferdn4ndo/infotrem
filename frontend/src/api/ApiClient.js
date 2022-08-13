import axios from 'axios';
import {ConfigClient, API_BASE_URL, API_TOKEN} from '../config/ConfigClient';

class ApiClient {
  static client = null;
  static apiUrl = '';

  /**
   * Create axios client
   */
  static init() {
    ApiClient.apiUrl = ConfigClient.get(API_BASE_URL).replace(/\/$/, ''); // replace last char if it is '/'
    ApiClient.client = axios.create({
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
        Authorization: `Api-Token ${ConfigClient.get(API_TOKEN)}`
      }
    });
  }

  static getCancelToken() {
    return axios.CancelToken;
  }

  static addCommonHeader(name, value) {
    ApiClient.client.defaults.headers[name] = value;
  }
}

export default ApiClient
