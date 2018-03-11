import Vue from 'vue'
import Router from 'vue-router'
import EventListItem from '@/components/home/EventListItem.vue'
import 'vuetify/dist/vuetify.min.css'
import MapView from '@/components/home/MapView'
import 'vuetify/dist/vuetify.min.css'
import Vuetify from 'vuetify'
var VueTouch = require('vue-touch')

Vue.use(VueTouch, {name: 'v-touch'})
Vue.use(Vuetify, {
  theme: {
    primary: '#00A99D',
    accent: '#FF6619',
    secondary: '#494949',
    secondaryText: '#8E8E8E'
  }
})
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Map',
      component: MapView
    },
    {
      path: '/event',
      name: 'EventListItem',
      component: EventListItem
    }
  ]
})
