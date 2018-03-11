<template>
  <v-flex xs6>
    <v-card>
      <v-card-title class="px-0" primary-title>
        <p class="orange--text time">
          {{(new Date(this.event.start)).toLocaleDateString()}}
          <br>
          {{(new Date(this.event.start)).toTimeString().substr(0,5)}}
        </p>

        <div class="card-header">
              <div style="margin: 0 auto">
                <span class="headline">{{this.event.caption}}</span>
                <br>
                <span class="secondaryText--text" v-if="this.event.description">{{this.event.description}}</span>
              </div>
            </div>
      </v-card-title>
      <v-card-text class="px-0">
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
            <v-btn block color="primary" round>Dołącz</v-btn>
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
  * {
    padding: 3px;
  }

  .distance {
    font-weight: bolder;
  }

  .time {
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
