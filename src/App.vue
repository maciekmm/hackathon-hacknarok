<template>
  <v-app>
    <v-content pa-0>
      <v-container fill-height fill-width pa-0 fluid>
        <router-view :key="$route.fullPath"/>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
  import {store, API_HOST} from './store/store.js'

  export default {
    name: 'app',
    data() {
      return {
        store: store.store
      };
    },
    mounted() {
      store.login(this, {
        username: 'admin',
        password: 'admin0000'
      }, data => {
        this.$http
          .get(API_HOST + 'categories/', {
            headers: store.getAuthHeader()
          })
          .then(
            data => {
              store.store.categories = data.body;
              console.log(store.store.categories);
            },
            data => {
              this.error = data.err;
            }
          );
      });
    }
  };
</script>

<style>
  html {
    overflow: hidden;
  }



  .gradient-background {
    background: linear-gradient(0deg, rgba(255, 255, 255, 0) 0%, rgba(0, 169, 157, 1) 100%);
    background-color: transparent !important;
    color: #ffffff;
    pointer-events: none;
  }

  .pointer-events {
    pointer-events: all;
  }

  * {
    font-family: 'Montserrat';
  }
</style>
