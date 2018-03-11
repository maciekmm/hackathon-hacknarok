<template>
  <div>
    <p>Room view</p>
    <p>{{ roomId }}</p>
    <p>{{ room.caption }}</p>
  </div>
</template>

<script>
  export default {
    name: 'Room',
    data() {
      return {
        roomId: this.$route.params.roomId,
        room: this.$store.data.rooms.filter(room => room.pk === this.roomId)
      };
    }
  };
</script>

<style scoped>

</style>
