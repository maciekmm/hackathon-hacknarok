<template>
    <div id="swipe-container" class="swipe mx-auto" fill-width grid-list-md text-xs-center>
        <v-btn class="trigger-button" block round depressed color="primary" @click="toggle">
          <span v-if="collapsed">Show</span>
          <span v-else>Hide</span>
        </v-btn>
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
        element.classList.remove('swipe-active')
        //element.style.top = window.innerHeight - 60 + "px";
      } else {
        element.classList.add('swipe-active')
        //element.style.top = "initial";
      }
    }
  }
};
</script>
<style>
.swipe {
  right: 0;
  left: 0;
  transition: all 0.5s;
  text-align: center;
  width: 100%;
  position: fixed;
  transform: translateY(-55px);
  background: #f7f7f7;
}
.swipe-active {
  transform: translateY(-100%);
}
.trigger-button {
  max-width: 70%;
  margin: 8pt auto;
}
</style>