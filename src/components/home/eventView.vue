<template>
  <v-layout row justify-center>
    <v-dialog v-model="dialog" persistent max-width="290">
      <v-btn color="primary" slot="activator">Dołącz</v-btn>
      <v-card>
        <v-card-title class="headline">{{subject.subject}}</v-card-title>
        <v-card-text> {{subjectDesc.subjectDesc}} w odległości {{distance.distance}}</v-card-text>
        <v-card-text> {{currentUsers.currentUsers}}/{{totalUsers.totalUsers}} osób o {{time.time}}</v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="green darken-1" flat @click.native="dialog = false">Anuluj</v-btn>
          <v-btn color="green darken-1" flat @click.native="dialog = false">Wchodze w to</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-layout>
</template>
l
<script>
   export default {
    name: 'eventView',
    props: ['subject', 'subjectDesc', 'distance', 'currentUsers', 'totalUsers', 'time'],
    data: function () {
      return {

      }
    }

  }
</script>

<style scoped>
  div {
    border-radius: 20px;
  }
</style>
