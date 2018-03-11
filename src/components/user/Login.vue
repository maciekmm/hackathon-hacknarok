<template>
  <div @keyup.enter="login" class="full-width">
    <v-toolbar class="gradient-background" flat height="100">
      <v-container class="pointer-events" align-center grid-list-lg text-xs-center>
        <v-layout row wrap>
          <v-flex sm12 text-xs-center>
            <v-toolbar-title class="white--text display-1" style="font-weight: bold">WeLearn</v-toolbar-title>
          </v-flex>
        </v-layout>
      </v-container>
    </v-toolbar>
    <v-container grid-list-xl text-xs-center>
      <v-layout row wrap>
        <v-flex xs10 offset-xs1 md8 offset-md2 lg6 offset-lg3>
          <v-card>
            <v-card-text>
              <v-container fill-height fluid>
                <v-layout fill-height>
                  <v-flex offset-xs1 xs10 align-end flexbox>
                    <v-form>
                      <v-text-field label="Username" v-model="credentials.username" required></v-text-field>
                      <v-text-field label="Password" type="password" v-model="credentials.password" required></v-text-field>
                      <v-btn color="primary" block round depressed v-on:click="login">Log in</v-btn>
                    </v-form>
                  </v-flex>
                </v-layout>
              </v-container>
            </v-card-text>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
  import {
    API_URL
  } from "@/constants.js";
  export default {
    data() {
      return {
        credentials: {
          username: "",
          password: "",
        },
      };
    },
    methods: {
      login() {
        this.$http
          .post(API_URL + "api-token-auth/", this.credentials)
          .then(response => {
            window.localStorage.setItem("token", response.data.token);
            this.$router.push('/');
          })
          .catch(errors => {
            console.log(errors);
          });
      }
    }
  };
</script>

<style>
  #app {
    background: #00a99d;
  }
  .full-width {
    width: 100%;
  }
</style>
