import Vue from 'vue'
import Router from 'vue-router'
import Hello from '@/components/Hello'
import 'vuetify/dist/vuetify.min.css' 
import Vuetify from 'vuetify'
 
Vue.use(Vuetify)

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Hello',
      component: Hello
    }
  ]
})
