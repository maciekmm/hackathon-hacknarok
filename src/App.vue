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
            <v-select label="Category" solo :items="items" single-line hide-details item-value="text"></v-select>
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

export default {
  name: 'app',
  data() {
    return {
      items: ['a','b','c']
    }
  }
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

* {
  font-family: 'Montserrat';
}
</style>
