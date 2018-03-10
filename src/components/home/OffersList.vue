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
          <eventListItem
            v-for="item in items" :key="item.id"
            v-bind:subject=item.subject
            v-bind:subjectDesc=item.subjectDesc
            v-bind:distance=item.distance
            v-bind:currentUsers=item.currentUsers
            v-bind:totalUsers=item.totalUsers
            v-bind:time=item.time
          >
          </eventListItem>
        </v-layout>
        </v-touch>
    </div>
    </div>
</template>
<script>
  import eventListItem from './eventListItem.vue';

  export default {
  name: "OffersList",
  mounted() {
    this.toggle();
  },
  data() {
    return {
      items: [
        {
          subject: "Analiza Matematyczna",
          subjectDesc: "Rachunek różniczkowy",
          distance: "5 KM",
          currentUsers: 3,
          totalUsers: 5,
          time: "14:30"
        },
        {
          subject: "test",
          subjectDesc: "test2",
          distance: "100 M",
          currentUsers: 7,
          totalUsers: 10,
          time: "20:30"
        },
        {
          subject: "re",
          subjectDesc: "tererest2",
          distance: "100 KM",
          currentUsers: 89,
          totalUsers: 10000000000,
          time: "21:30"
        }
      ],
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
  },
    components: {
      eventListItem
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

.swipe * {
  text-align: initial;
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

