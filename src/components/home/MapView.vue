<template>
<div style="height: 100%; width: 100%;">
    <gmap-map
    :center="center"
    :zoom="7"
  >
  </gmap-map>
  </div>
</template>

<script>
import * as VueGoogleMaps from "vue2-google-maps";
import Vue from "vue";

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
      markers: [
        {
          position: { lat: 10.0, lng: 10.0 }
        },
        {
          position: { lat: 11.0, lng: 11.0 }
        }
      ]
    };
  },
  components: {
    Map
  }
};
</script>
<style>
.vue-map-container {
  width: 100%;
  height: 100%;
}
</style>