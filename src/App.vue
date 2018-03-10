<template>
  <v-app>
    <v-toolbar fixed class="gradient-background" flat height="100">
      <v-container class="pointer-events" align-center grid-list-lg text-xs-center>
        <v-layout row wrap>
          <v-flex sm12 md4 lg2 text-xs-center>
            <v-toolbar-title class="white--text display-1" style="font-weight: bold">WeLearn</v-toolbar-title>
          </v-flex>
          <v-flex sm12 md8 lg8>
            <v-text-field class="mx-auto search-bar" prepend-icon="search" hide-details solo light single-line></v-text-field>
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
  import ListElement from "./components/home/eventListItem";

export default {
  components: {ListElement},
  name: 'app'
}
</script>

<style>
.gradient-background {
  background: linear-gradient(0deg, rgba(255, 255, 255, 0) 0%, rgba(0, 169, 157, 1) 100%);
  background-color:transparent !important;
  color: #ffffff;
  pointer-events: none;
}

.pointer-events {
  pointer-events: all;
}

.search-bar {
}

* {
  font-family: 'Montserrat';
}
</style>
