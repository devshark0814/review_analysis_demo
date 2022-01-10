// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import vuetify from '@/plugins/vuetify' // path to vuetify export
import Toasted from 'vue-toasted';
import axios from "axios"; //追記
import VueAxios from "vue-axios"; //追記
import apiClient from "./common/apiClient";
import VueApexCharts from 'vue-apexcharts';
import VueWordCloud from 'vuewordcloud';

Vue.config.productionTip = false

Vue.use(Toasted);
Vue.use(VueAxios, axios); //追記
Vue.use(VueApexCharts);

Vue.component('apexchart', VueApexCharts);
Vue.component(VueWordCloud.name, VueWordCloud);

Vue.prototype.$apiClient = apiClient;

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  vuetify,
  components: { App },
  template: '<App/>'
})
