/* eslint-disable no-process-env */
export const API_TOKEN = 'API_TOKEN';
export const API_BASE_URL = 'BASE_URL'
export const NODE_ENV = 'NODE_ENV';

export class ConfigClient {
  static config = {};

  /**
   * Initiate the configuration
   */
  static init() {
    ConfigClient.config[NODE_ENV] = process.env.NODE_ENV;
    ConfigClient.config[API_TOKEN] = process.env.REACT_APP_API_TOKEN;
    ConfigClient.config[API_BASE_URL] = process.env.REACT_APP_API_BASE_URL;
  }

  static get(configName) {
    return ConfigClient.config[configName];
  }
}
