import Vue from 'vue'
import Router from 'vue-router'
import Hello from '@/components/Hello'
import MapView from '@/components/home/MapView'
import 'vuetify/dist/vuetify.min.css' 
import Vuetify from 'vuetify'
 
Vue.use(Vuetify, {
  theme: {
    primary: '#00A99D',
    accent: '#FF6619',
    secondary: '#494949'
  }
})
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Map',
      component: MapView
    }
  ]
})
