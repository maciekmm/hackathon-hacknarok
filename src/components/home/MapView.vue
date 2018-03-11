<template>
  <div class="map-wrapper">
    <v-toolbar fixed class="gradient-background" flat height="100">
      <v-container class="pointer-events" align-center grid-list-xs text-xs-center>
        <v-layout row wrap>
          <v-flex sm12 md2 text-xs-center>
            <router-link class="link-disabled" to="/">
              <v-toolbar-title class="white--text display-1" style="font-weight: bold">WeLearn</v-toolbar-title>
            </router-link>
          </v-flex>
          <v-flex sm12 md8>
            <v-text-field class="mx-auto search-bar" prepend-icon="search" hide-details solo light single-line/>
          </v-flex>
          <v-flex sm12 md2>
            <v-select label="Category"
                      solo
                      clearable
                      :close-on-click="true"
                      :items="this.store.categories"
                      item-text="caption"
                      item-key="pk"
                      single-line
                      hide-details/>
          </v-flex>
        </v-layout>
      </v-container>
    </v-toolbar>

    <gmap-map :center="center" :position="center" :options="{disableDefaultUI: true}" :zoom="13"/>
    <v-btn bottom fab right fixed @click="this.getLocationAndCenter" class="center-button">
      <v-icon dark>{{ this.icon }}</v-icon>
    </v-btn>
    <offers-list/>
  </div>

</template>

<script>
  import * as VueGoogleMaps from 'vue2-google-maps';
  import Vue from 'vue';
  import OffersList from './OffersList.vue';
  import {
    API_URL
  } from '@/constants.js'

  Vue.use(VueGoogleMaps, {
    load: {
      key: 'AIzaSyBr8wwgdwKJadT6Tdwc2D5drd9KIElpZVw'
    }
  });

  export default {
    name: 'MapView',
    data: function data() {
      return {
        center: {
          lat: 10.0,
          lng: 10.0
        },
        icon: 'gps_not_fixed',
        error: '',
        store: this.$store.data
      };
    },
    mounted() {
      this.$http
        .get(API_URL + "rooms/")
        .then(
          data => {
            this.store.rooms = data.body;
            console.log(this.$store.data)
          },
          data => {
            this.error = data.err;
          }
        );
      this.getLocationAndCenter();
    },
    methods: {
      getLocationAndCenter() {
        this.icon = 'gps_not_fixed';
        if (navigator.geolocation) {
          navigator.geolocation.getCurrentPosition(this.centerMap, error => {
            this.icon = 'gps_off';
          });
        } else {
          this.icon = 'gps_off';
        }
      },
      centerMap(position) {
        this.center = {
          lat: position.coords.latitude + Math.random() / 1000,
          lng: position.coords.longitude + Math.random() / 1000
        };
        this.icon = 'gps_fixed';
      }
    },
    components: {
      OffersList
    }
  };

</script>
<style>

  .link-disabled {
    text-decoration: none;
  }

  .map-wrapper {
    height: 100%;
    width: 100%;
  }

  .vue-map-container {
    width: 100%;
    height: calc(100% - 60px);
  }

  .center-button {
    margin-bottom: 60px;
    z-index: 1;
  }

</style>
