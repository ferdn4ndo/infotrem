import Vue from "vue";
import Vuex from "vuex";

import auth from "./auth.module";
import billet from "./billet.module";
import contact from "./contact.module";
import email_validation from "./email_validation.module";
import event from "./event.module";
import filemgr from "./filemgr.module";
import home from "./home.module";
import loader from "./loader.module";
import location from "./location.module";
import profile from "./profile.module";
import subscription from "./subscription.module";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    auth,
    billet,
    contact,
    email_validation,
    event,
    filemgr,
    home,
    loader,
    location,
    profile,
    subscription,
  },
});
