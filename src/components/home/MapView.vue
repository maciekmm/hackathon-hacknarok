<template>
<div class="map-wrapper">
  <gmap-map
    :center="center"
    :position="center"
    :options="{disableDefaultUI: true}"
    :zoom="13">
  </gmap-map>
  <v-btn bottom fab right fixed @click="this.getLocationAndCenter" style="margin-bottom: 60px; z-index: 1">
    <v-icon dark>{{ this.icon }}</v-icon>
  </v-btn>
  <offers-list></offers-list>
  </div>
</template>

<script>
import { store, API_HOST } from "../../store/store.js";
import * as VueGoogleMaps from "vue2-google-maps";
import Vue from "vue";
import OffersList from "./OffersList.vue";

Vue.use(VueGoogleMaps, {
  load: {
    key: "AIzaSyBr8wwgdwKJadT6Tdwc2D5drd9KIElpZVw",
    v: "3"
    // libraries: 'places', //// If you need to use place input
  }
});

export default {
  name: "MapView",
  data: function data() {
    return {
      center: { lat: 10.0, lng: 10.0 },
      icon: "gps_not_fixed",
      rooms: [],
      error: ''
    };
  },
  mounted() {
    store.login(this, { username: "admin", password: "admin0000" }, data => {
      this.$http.get(API_HOST + "rooms/", {headers: store.getAuthHeader()}).then(
        data => {
          this.rooms = data.body
        },
        data => {
          this.error = data.err
        }
      );
    });
    this.getLocationAndCenter();
  },
  methods: {
    getLocationAndCenter() {
      this.icon = "gps_not_fixed";
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(this.centerMap, error => {
          this.icon = "gps_off";
        });
      } else {
        this.icon = "gps_off";
      }
    },
    centerMap(position) {
      this.center = {
        lat: position.coords.latitude + Math.random() / 1000,
        lng: position.coords.longitude + Math.random() / 1000
      };
      this.icon = "gps_fixed";
    }
  },
  components: {
    OffersList
  }
};
</script>
<style>
  .map-wrapper {
    height: 100%;
    width: 100%;
  }

.vue-map-container {
  width: 100%;
  height: calc(100% - 60px);
}
</style>
