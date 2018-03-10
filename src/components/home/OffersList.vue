<template>
<div>
    <div id="swipe-container" v-on:swipeup="toggle" class="swipe mx-auto" fill-width grid-list-md text-xs-center>
      <v-touch @swipeup="toggle" @swipedown="toggle">
        <div class="button-wrapper">
        <v-btn class="trigger-button" color="primary" depressed @click="toggle">
          <v-icon v-if="collapsed">keyboard_arrow_up</v-icon>
          <v-icon v-else>keyboard_arrow_down</v-icon>
        </v-btn>
        </div>
        <v-spacer></v-spacer>
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
        </v-touch>
    </div>
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
  z-index: 10;
  background: #f7f7f7;
}
.swipe-active {
  transform: translateY(-100%);
}
.trigger-button {
  max-width: 70%;
  margin: 8pt auto;
}
.button-wrapper {
  width: 100%;
  height: 60px;
  background: #00a99d;
}
</style>