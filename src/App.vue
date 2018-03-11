<template>
  <v-app>
    <v-content pa-0>
      <v-container fill-height fill-width pa-0 fluid>
        <router-view></router-view>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
  import {
    API_URL
  } from '@/constants.js'
  
  export default {
    name: 'app',
    data() {
      return {
        store: this.$store.data
      }
    },
    mounted() {
      this.$http.get(API_URL + "categories/")
        .then(
          data => {
            this.store.categories = data.body;
          },
          data => {
            this.error = data.err;
          }
        );
    }
  }
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
