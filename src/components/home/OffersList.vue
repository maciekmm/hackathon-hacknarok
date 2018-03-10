<template>
    <div id="swipe-container" class="swipe mx-auto" fill-width grid-list-md text-xs-center>
        <v-btn @click="toggle" v-if="this.collapsed">Show</v-btn>
        <v-btn @click="toggle" v-if="!this.collapsed">Hide</v-btn>
        <v-layout row wrap>
            <v-flex xs12>
                Test
            </v-flex>
            <v-flex xs12>
                Test
            </v-flex>
            <v-flex xs12>
                Test
            </v-flex>
            <v-flex xs12>
                Test
            </v-flex>
            <v-flex xs12>
                Test
            </v-flex>
            <v-flex xs12>
                Test
            </v-flex>
        </v-layout>
    </div>
</template>
<script>
export default {
  name: "OffersList",
  mounted() {
    this.toggle();
  },
  data() {
    return {
      collapsed: false
    };
  },
  methods: {
    toggle: function() {
      this.collapsed = !this.collapsed;
      let element = document.getElementById("swipe-container");
      if (this.collapsed) {
        element.style.top = window.innerHeight - 60 + "px";
      } else {
        element.style.top = "initial";
      }
    }
  }
};
</script>
<style>
.swipe {
  bottom: 0;
  right: 0;
  left: 0;
  transition: top 2s;
  text-align: center;
  width: 100%;
  position: fixed;
  background: #f7f7f7;
}
</style>