<template>
  <div class="full-width">
    <v-toolbar flat height="100" class="no-bg">
      <v-container text-xs-center class="no-bg">
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
                  <v-layout grid-list-xs row wrap>
                    <v-flex offset-xs1 xs5>
                      <v-text-field label="First name" v-model="credentials.first_name"></v-text-field>
                    </v-flex>
                    <v-flex xs5>
                      <v-text-field label="Last name" v-model="credentials.last_name"></v-text-field>
                    </v-flex>
                    <v-flex offset-xs1 xs10>
                      <v-text-field label="E-mail" :rules="emailRules" v-model="credentials.email" required></v-text-field>
                    </v-flex>
                    <v-flex offset-xs1 xs10>
                      <v-text-field label="Username" :rules="requiredRule" v-model="credentials.username" required></v-text-field>
                    </v-flex>
                    <v-flex offset-xs1 xs10>
                      <v-text-field label="Password" type="password" v-model="credentials.password" :rules="requiredRule" required></v-text-field>
                    </v-flex>
                    <v-flex offset-xs1 xs10>
                      <v-btn color="primary" block round depressed type="submit" v-on:click="login">Sign up</v-btn>
                    </v-flex>
                    <v-flex offset-xs1 xs10>
                        Already have an account? <router-link to="/login">Sign in</router-link>
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
import { API_URL } from "@/constants.js";
export default {
  data() {
    return {
      credentials: {
        first_name: "",
        last_name: "",
        email: "",
        username: "",
        password: ""
      },
      requiredRule: [v => !!v || "This field is required"],
      emailRules: [
        v => !!v || "E-mail is required",
        v =>
          /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,5})+$/.test(v) ||
          "E-mail must be valid"
      ],
      errors: [],
    };
  },
  methods: {
    login() {
      if (!this.$refs.form.validate()) return;
      this.$http
        .post(API_URL + "register/", this.credentials)
        .then(response => {
          this.$router.push("/login");
        })
        .catch(errors => {
            console.log(errors)
            this.errors = errors
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
