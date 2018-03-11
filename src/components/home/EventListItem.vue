<template>
  <v-flex xs12 sm6 md4 class="event-card">
    <v-card class="max-height">

      <v-card-title class="px-0 height-half" primary-title>
        <v-flex xs4>

          <p class="orange--text time">
            <!--{{(new Date(this.event.start)).toLocaleDateString()}}
            <br>-->
          {{(new Date(this.event.start)).toTimeString().substr(0,5)}}
        </p>
        </v-flex>

        <v-flex xs8>
          <div class="card-header">
            <div class="no-margin">
              <span class="black--text">{{this.event.caption}}</span>
              <br>
              <span class="secondaryText--text" v-if="this.event.description">{{this.event.description}}</span>
            </div>
          </div>
        </v-flex>
      </v-card-title>
      <v-card-text class="px-0 no-margin">
        <v-layout wrap fluid>
          <v-flex xs8>
            <v-layout class="align-center">
              <v-flex>
                <span class="primary--text distance">
                  {{
                  distanceInKmBetweenEarthCoordinates(this.event.lat,this.event.lon,50,20)
                  }} KM
                </span>
              </v-flex>
              <v-flex>
            <span>
            <v-icon>group</v-icon>
            {{this.event.members.length}}<span v-if="this.event.limit">/{{this.event.limit}}</span> osób
          </span>
              </v-flex>
            </v-layout>
          </v-flex>
          <v-flex>
            <v-btn depressed block color="primary">Dołącz</v-btn>
          </v-flex>
        </v-layout>
      </v-card-text>
    </v-card>
  </v-flex>
</template>

<script>
  module.exports = {
    name: 'EventListItem',
    props: ['event'],
    methods: {
      degreesToRadians(degrees) {
        return (degrees);
      },
      distanceInKmBetweenEarthCoordinates(lat1, lon1, lat2, lon2) {
        var earthRadiusKm = 6371;
        var dLat = (lat2 - lat1) * Math.PI / 180;
        var dLon = (lon2 - lon1) * Math.PI / 180;
        lat1 = lat1 * Math.PI / 180;
        lat2 = lat2 * Math.PI / 180;
        var a = Math.sin(dLat / 2) * Math.sin(dLat / 2) + Math.sin(dLon / 2) * Math.sin(dLon / 2) * Math.cos(lat1) * Math.cos(lat2);
        var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
        return parseInt(earthRadiusKm * c);
      }
    },
  }

</script>
subject: test.subject,
subjectDesc: test.subjectDesc,
distance: test.distance,
currentUsers: test.currentUsers,

<style scoped>

  .event-card {
    word-wrap: normal;
  }

  * {
    padding: 3px;
  }

  .max-height {
    height: 100%
  }

  .height-half {
    height: 50%
  }

  .distance {
    font-weight: bold;
  }

  .no-margin {
    margin: 0 auto;
  }

  .time {
    align-self: left;
    border-radius: 20px;
    padding: 10px;
    font-size: large;
    font-weight: bold;
    border: 2px solid orange;
  }
</style>
