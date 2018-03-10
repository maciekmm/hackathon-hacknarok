<template>
  <v-flex xs6>
    <v-card color="white-grey lighten-2">
      <v-card-title primary-title color="blue-grey darken-2">
        <v-layout row align="end">
          <p id="time" class="orange--text">{{time}}</p>
          <v-flex>
            <div style="margin: 0 auto">
              <span class="headline">{{subject}}</span>
              <br>
              <span class="secondaryText--text">{{subjectDesc}}</span>
            </div>
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
          <v-flex>
            <v-btn block color="primary" round dark>Dołącz</v-btn>
          </v-flex>
        </v-layout>
      </v-card-text>
    </v-card>
  </v-flex>
</template>

<script>
  module.exports = {
    name: 'eventListItem',
    data: function (test) {
      return {
        subject: test.subject,
        subjectDesc: test.subjectDesc,
        distance: test.distance,
        currentUsers: test.currentUsers,
        totalUsers: test.totalUsers,
        time: test.time

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
