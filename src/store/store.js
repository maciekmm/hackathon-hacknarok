import {API_URL} from '@/constants.js'

import Vue from 'vue'

const jwtDecode = require('jwt-decode');


let store = {
  bus: new Vue(),
  user: {
    token: () => {
      return window.localStorage.getItem('token')
    },
    getUser: () => {
      if (window.localStorage.getItem('token')) {
        return jwtDecode(window.localStorage.getItem('token')).User
      }
      return null;
    },
    getAuthorizationHeader: () => {
      return {
        'Authorization': 'JWT ' + token()
      };
    }
  },
  data: {
    rooms: [],
    categories: []
  }

};

export default {
  store,
  install(Vue, options) {
    Vue.prototype.$store = store;
  }
}
