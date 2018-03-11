<template>
  <v-app>
    <v-toolbar fixed class="gradient-background" flat height="100">
      <v-container class="pointer-events" align-center grid-list-xs text-xs-center>
        <v-layout row wrap>
          <v-flex sm12 md2 text-xs-center>
            <v-toolbar-title class="white--text display-1" style="font-weight: bold">WeLearn</v-toolbar-title>
          </v-flex>
          <v-flex sm12 md8>
            <v-text-field class="mx-auto search-bar" prepend-icon="search" hide-details solo light single-line></v-text-field>
          </v-flex>
          <v-flex sm12 md2>
            <v-select label="Category" solo :items="this.store.categories" item-text="caption" item-key="pk" single-line hide-details></v-select>
          </v-flex>
        </v-layout>
      </v-container>
    </v-toolbar>
    <v-content pa-0>
      <v-container fill-height fill-width pa-0 fluid>
        <router-view></router-view>
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
      }
    },
    computed: {
      flatCategories: function() {
        console.log(this.store.categories)
        return Array.from(Object.keys(this.store.categories), k=>this.store.categories[k].caption);
      }
    },
    mounted() {
      store.login(this, {
        username: "admin",
        password: "admin0000"
      }, data => {
        this.$http
          .get(API_HOST + "categories/", {
            headers: store.getAuthHeader()
          })
          .then(
            data => {
              store.store.categories = data.body;
              console.log(store.store.categories)
            },
            data => {
              this.error = data.err;
            }
          );
      });
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
