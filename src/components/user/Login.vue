<template>
  <div class="full-width">
    <v-toolbar class="no-bg" flat height="100">
      <v-container align-center grid-list-lg text-xs-center>
        <v-toolbar-title class="white--text display-1" style="font-weight: bold">WeLearn</v-toolbar-title>
      </v-container>
    </v-toolbar>
    <v-container grid-list-xl text-xs-center>
      <v-layout row wrap>
        <v-flex xs10 offset-xs1 md8 offset-md2 lg6 offset-lg3>
          <v-card>
            <v-card-text>
              <v-form ref="form" style="width: 100%">
                <v-container fill-height fluid>
                  <v-layout fill-height row wrap>
                    <v-flex offset-xs1 xs10 align-end flexbox>
                      <v-text-field label="Username" :rules="requiredRule" v-model="credentials.username" required></v-text-field>
                    </v-flex>
                    <v-flex offset-xs1 xs10 align-end flexbox>
                      <v-text-field label="Password" type="password" :rules="requiredRule" v-model="credentials.password" required></v-text-field>
                    </v-flex>
                    <v-flex offset-xs1 xs10 align-end flexbox>
                      <v-btn color="primary" block round depressed type="submit" v-on:click="login">Log in</v-btn>
                    </v-flex>
                    <v-flex offset-xs1 xs10>
                        Don't have an account? <router-link to="/register">Sign up</router-link>
                    </v-flex>
                  </v-layout>
                </v-container>
              </v-form>
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
          password: ""
        },
        requiredRule: [v => !!v || "This field is required"],
      };
    },
    methods: {
      login() {
        if(!this.$refs.form.validate()) return;
        this.$http
          .post(API_URL + "api-token-auth/", this.credentials)
          .then(response => {
            window.localStorage.setItem("token", response.data.token);
            this.$store.data.user = response.data;
            this.$router.push("/");
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

  .no-bg {
    background: transparent !important;
  }

</style>
