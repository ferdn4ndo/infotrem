import {
  FileUploadService,
} from "@/common/filemgr.service";
import {
  POST_FILE,
} from "./actions.type";
import {
  SET_LOADING,
  RESET_LOADING,
  APPEND_UPLOADED_FILE,
  SET_UPLOADED_FILES,
} from "./mutations.type";

const initialState = {
  filesUploaded: [],
};

export const state = { ...initialState };

export const actions = {
  [POST_FILE](context, file, prevEvent) {
    return new Promise((resolve, reject) => {
      if (prevEvent !== undefined) {
        return prevEvent;
      }
      context.commit(SET_LOADING, "files_upload");

      FileUploadService
        .postFile(file)
        .then((response) => {
          context.commit(RESET_LOADING, "files_upload");
          resolve(response);
        })
        .catch((error) => {
          context.commit(RESET_LOADING, "files_upload");
          reject(error);
        });
    });
  },
};

/* eslint no-param-reassign: ["error", { "props": false }] */
export const mutations = {
  [APPEND_UPLOADED_FILE](state, uploadedFile) {
    let filteredFiles = state.events.filter((file) => {
      return file.name !== uploadedFile.name;
    });
    filteredFiles.push(uploadedFile);

    state.filesUploaded = filteredFiles;
  },

  [SET_UPLOADED_FILES](state, uploadedFiles) {
    state.filesUploaded = uploadedFiles;
  },
};

const getters = {
  filesUploaded(state) {
    return state.filesUploaded;
  },
};

export default {
  state,
  actions,
  mutations,
  getters,
};
