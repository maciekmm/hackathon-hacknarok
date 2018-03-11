<template>
  <div>
    <p>Room view</p>
    <p>{{ roomId }}</p>
    <p>{{ room.caption }}</p>
  </div>
</template>

<script>
  import {
    store
  } from '../../store/store.js';

  export default {
    name: 'Room',
    data() {
      return {
        roomId: this.$route.params.roomId,
        room: store.store.rooms.filter(room => room.pk === this.roomId)
      };
    }
  };
</script>

<style scoped>

</style>
