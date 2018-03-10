<template>
  <v-app>
    <v-toolbar fixed class="gradient-background" flat height="100">
      <v-toolbar-title class="white--text mx-auto display-2">WeLearn</v-toolbar-title>
    </v-toolbar>
    <v-content pa-0>
      <v-container fill-height fill-width pa-0 fluid>
        <router-view></router-view>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
  import ListElement from "./components/eventListItem";

export default {
  components: {ListElement},
  name: 'app'
}
</script>

<style>
.gradient-background {
  background-image: linear-gradient(0deg, rgba(255, 255, 255, 0) 0%, rgba(0, 169, 157, 1) 100%);
  background-color:transparent !important;
  color: #ffffff;
  text-shadow: 0px 1px 2px rgba(150, 150, 150, 1);
  pointer-events: none;
}

* {
  font-family: 'Montserrat';
}
</style>
