<template>
  <v-card color="white-grey lighten-2">
    <v-card-title primary-title color="blue-grey darken-2">
      <v-layout row align="end">
        <p id="time" class="orange--text">{{time}}</p>
        <v-flex>
          <span class="headline">{{subject}}</span>
          <br>
          <span class="secondaryText--text">{{subjectDesc}}</span>
        </v-flex>
      </v-layout>
    </v-card-title>
    <v-card-text>
      <v-layout wrap fluid>
        <v-flex xs8>
          <v-layout style="text-align: center">
            <v-flex>
              <span id="distance" class="primary--text">{{distance}}</span>
            </v-flex>
            <v-flex>
            <span>
            <v-icon>group</v-icon>
            {{currentUsers}}/{{totalUsers}} osób
          </span>
            </v-flex>
          </v-layout>
        </v-flex>
        <v-flex :align="right">
          <v-btn block color="primary" round dark>Dołącz</v-btn>
        </v-flex>
      </v-layout>
    </v-card-text>
  </v-card>
</template>

<script>
  export default {
    name: 'listElement',
    data() {
      return {
        subject: "Analiza Matematyczna",
        subjectDesc: "Rachunek różniczkowy",
        distance: "5 KM",
        currentUsers: 3,
        totalUsers: 5,
        time: "14:30",
        msg: 'Welcome to Your Vue.js'
      }
    }
  }
</script>

<style scoped>

  #distance {
    font-weight: bolder;
  }

  #time {
    align-self: left;
    border-radius: 20px;
    padding: 10px;
    font-size: large;
    font-weight: bold;
    border: 2px solid orange;
  }

  div {
    border-radius: 20px;
  }
</style>
