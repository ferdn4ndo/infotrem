import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import axios from "axios";
import "./registerServiceWorker";

import { CHECK_AUTH } from "./store/actions.type";
import ApiService from "./common/api.service";
import FileMgrService from "./common/filemgr.service";
import CurrencyFilter from "./filters/currency.filter";
import DateFilter from "./filters/date.filter";
import CpfFilter from "./filters/cpf.filter";
import BooleanFilter from "./filters/boolean.filter";
import CepFilter from "./filters/cep.filter";
import PhoneFilter from "./filters/phone.filter";
import BlankFilter from "./filters/blank.filter";
import VacancyFilter from "./filters/vacancy.filter";
import DatetimeFilter from "./filters/datetime.filter";

Vue.config.productionTip = false;
Vue.filter("currency", CurrencyFilter);
Vue.filter("date", DateFilter);
Vue.filter("datetime", DatetimeFilter);
Vue.filter("cpf", CpfFilter);
Vue.filter("boolean", BooleanFilter);
Vue.filter("cep", CepFilter);
Vue.filter("phone", PhoneFilter);
Vue.filter("blank", BlankFilter);
Vue.filter("vacancy", VacancyFilter);

ApiService.init();
FileMgrService.init();

// Ensure we checked auth before each page load.
router.beforeEach((to, from, next) =>
  Promise.all([store.dispatch(CHECK_AUTH)]).then(next)
);

Vue.prototype.$axios = axios;

import VueMask from "v-mask";
Vue.use(VueMask);

import money from "v-money";
Vue.use(money, { precision: 2 });

import OnLoad from "vue-onload";
Vue.use(OnLoad);

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
