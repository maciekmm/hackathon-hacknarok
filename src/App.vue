<template>
  <v-app dark>
    <v-toolbar app><h1>Welearn</h1></v-toolbar>
    <v-content>
      <v-container fluid>
        <router-view></router-view>
      </v-container>
    </v-content>
    <v-footer app></v-footer>
  </v-app>
</template>

<script>
export default {
  name: 'app'
}
</script>

<style>
</style>
