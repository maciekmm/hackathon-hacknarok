<template>

  <v-flex xs12 sm5 md3 my-3 mx-1 class="event-card"
          style="overflow:hidden;padding-bottom: 60px;box-sizing: border-box;">
    <v-card class="max-height" height="100%">

      <v-card-title class="px-0 height-half" primary-title>
        <v-flex xs4>

          <p class="orange--text time">
            <!--{{(new Date(this.event.start)).toLocaleDateString()}}
            <br>-->
          {{(new Date(this.event.start)).toTimeString().substr(0,5)}}
        </p>
        </v-flex>

        <v-flex xs8>
          <div class="card-header rounded">
            <div class="no-margin">
              <span class="black--text">{{this.event.caption}}</span>
              <br>
              <span class="height-half secondaryText--text"
                    v-if="this.event.description">{{this.event.description}}</span>
            </div>
          </div>
        </v-flex>
      </v-card-title>
      <v-card-text class="px-0 no-margin" style="background-color:#f9f9f9;">
        <v-layout wrap fluid style="">
          <v-flex xs8>
            <v-layout>
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
            <v-btn
              @click.stop="joinRoom(event.pk)"
              block color="primary" round>
              Dołącz
            </v-btn>
          </v-flex>
        </v-layout>
      </v-card-text>
    </v-card>
  </v-flex>
</template>

<script>
  import { API_URL } from '../../constants';

  export default {
    name: 'EventListItem',
    props: ['event'],
    methods: {
      joinRoom(roomId) {
        console.log(this.$store.rooms);

        let room = this.$store.data.rooms.filter(room => room.pk === roomId)[0];
        console.log(room);
        room.members = room.members.concat(this.$store.user.pk);

        this.$http.put(API_URL + 'rooms/' + room.pk, room)
          .then(response => {
            console.log(response);
            // this.$store.data.rooms[response.bo]
          });
        console.log(room);

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
    cursor: pointer;
    word-wrap: normal;
  }

  .event-card:hover {
    background-color: #e6e6e6;
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
  }

  .rounded {
    border-radius: 20px;
  }
</style>
