<template>
  <v-app>
    <v-toolbar fixed class="gradient-background" flat height="100">
      <v-toolbar-title class="white--text mx-auto display-2" style="font-weight: bold">WeLearn</v-toolbar-title>
    </v-toolbar>
    <v-content pa-0>
      <v-container fill-height fill-width pa-0 fluid>
        <router-view></router-view>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
export default {
  name: 'app',
  data() {
    return {
      title: 'WeLearn'
    }
  }
  
}
</script>

<style>
.gradient-background {
  background-image: linear-gradient(0deg, rgba(255, 255, 255, 0) 0%, rgba(0, 169, 157, 1) 100%);
  background-color:transparent !important;
  color: #ffffff;
  pointer-events: none;
}

* {
  font-family: 'Montserrat';
}
</style>
