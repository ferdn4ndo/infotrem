import axios from "axios";
import JwtService from "@/common/jwt.service";
import LoggerService from "@/common/logger.service";

const DEFAULT_CONTENT_TYPE = "multipart/form-data";

const fileAxios = axios.create({
  baseURL: process.env.VUE_APP_USERVER_FILEMGR_BASE_URL,
  timeout: 60000,
  params: {},
});

const FileMgrService = {
  init() {
    fileAxios.defaults.baseURL = process.env.VUE_APP_USERVER_FILEMGR_BASE_URL;

    fileAxios.interceptors.request.use((config) => {
      config.headers.Authorization = `Bearer ${JwtService.getToken()}`;
      return config;
    });
  },

  query(resource, params) {
    return new Promise((resolve, reject) => {
      return fileAxios
        .get(resource, params)
        .then((data) => {
          resolve(data);
        })
        .catch((error) => {
          LoggerService.error(`FileMgr request failed with error ${error}`);
          reject(error);
        });
    });
  },

  get(resource, slug = "") {
    return new Promise((resolve, reject) => {
      let url = slug ? `${resource}/${slug}` : resource;
      return fileAxios.get(url)
        .then((data) => {
          resolve(data);
        })
        .catch((error) => {
          LoggerService.error(`FileMgr request failed with error ${error}`);
          reject(error);
        });
    });
  },

  post(resource, data) {
    return new Promise((resolve, reject) => {
      return fileAxios
        .post(`${resource}`, data)
        .then((data) => {
          resolve(data);
        })
        .catch((error) => {
          LoggerService.error(`FileMgr request failed with error ${error}`);
          reject(error);
        });
    });
  },

  patch(resource, params) {
    return new Promise((resolve, reject) => {
      return fileAxios
        .patch(`${resource}`, params)
        .then((data) => {
          resolve(data);
        })
        .catch((error) => {
          LoggerService.error(`FileMgr request failed with error ${error}`);
          reject(error);
        });
    });
  },

  put(resource, params) {
    return new Promise((resolve, reject) => {
      return fileAxios
        .put(`${resource}`, params)
        .then((data) => {
          resolve(data);
        })
        .catch((error) => {
          LoggerService.error(`FileMgr request failed with error ${error}`);
          reject(error);
        });
    });
  },

  delete(resource) {
    return new Promise((resolve, reject) => {
      return fileAxios
        .delete(resource)
        .then((data) => {
          resolve(data);
        })
        .catch((error) => {
          LoggerService.error(`FileMgr request failed with error ${error}`);
          reject(error);
        });
    });
  },
};

export default FileMgrService;

export const FileUploadService = {
  postFile(file) {
    const storageId = process.env.VUE_APP_USERVER_FILEMGR_STORAGE_ID || false;

    if (typeof storageId === "undefined" || !storageId) {
      throw new Error("FileUploadService - Unable to retrieve the StorageID");
    }

    const endpoint = `storages/${storageId}/upload-from-file/`;

    let formData = new FormData();
    formData.append('file', file);

    return FileMgrService.post(endpoint, formData);
  },
};

export const ALLOWED_MIME_TYPES = [
  'application/msword',
  'application/pdf',
  'application/rtf',
  'application/vnd.ms-excel',
  'application/vnd.ms-powerpoint',
  'application/vnd.oasis.opendocument.presentation',
  'application/vnd.oasis.opendocument.spreadsheet',
  'application/vnd.oasis.opendocument.text',
  'application/vnd.openxmlformats-officedocument.presentationml.presentation',
  'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
  'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
  'image/jpeg',
  'image/png',
  'text/plain',
];

export const getIconFromMimeType = (mime) => {
  switch (mime) {
    case 'application/msword':
    case 'application/ms-word':
    case 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
    case 'application/vnd.oasis.opendocument.text':
      return 'file_ms_word';

    case 'application/vnd.ms-powerpoint':
    case 'application/vnd.oasis.opendocument.presentation':
    case 'application/vnd.openxmlformats-officedocument.presentationml.presentation':
      return 'file_ms_powerpoint';

    case 'application/vnd.ms-excel':
    case 'application/vnd.oasis.opendocument.spreadsheet':
    case 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
      return 'file_ms_excel';
      case 'application/pdf':
      return 'file_pdf';

    case 'image/jpeg':
    case 'image/png':
      return 'file_image';

    case 'application/rtf':
    case 'text/plain':
      return 'file_text';

    default:
      return 'file';
  }
};

export const getTypeFromMimeType = (mime) => {
  switch (mime) {
    case 'application/msword':
    case 'application/ms-word':
    case 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
    case 'application/vnd.oasis.opendocument.text':
    case 'application/rtf':
    case 'text/plain':
    case 'application/vnd.ms-powerpoint':
    case 'application/vnd.oasis.opendocument.presentation':
    case 'application/vnd.openxmlformats-officedocument.presentationml.presentation':
    case 'application/vnd.ms-excel':
    case 'application/vnd.oasis.opendocument.spreadsheet':
    case 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
    case 'application/pdf':
      return 'DOCUMENT';

    case 'image/jpeg':
    case 'image/png':
      return 'IMAGE';

    default:
      return 'UNKNOWN';
  }
};
