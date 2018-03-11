export const API_HOST = 'https://welearn.math.party/'

export var store = {

	user: {
		authenticated: false,
    },

    store: {
		rooms: [],
		categories: []
    },

	login (context, creds, callback) {
		if(this.user.authenticated) {
			callback(data.body.token);
		}
		context.$http.post(API_HOST + 'api-token-auth/', creds).then((data) => {
			localStorage.setItem('jwt_token', data.body.token)
            this.user.authenticated = true

            if(callback) {
                callback(data.body.token)
            }
		},
		(data) => {
			context.error = data.err
		})
	},

	signup (context, creds, redirect) {
		context.$http.post(API_PATH + 'users/', creds).then((data) => {
			localStorage.setItem('jwt_token', data.body.token)
			this.user.authenticated = true

			if (redirect) {
				router.push({ name: redirect })
			}
		},
		(data) => {
			context.error = data.err
		})
	},

	logout () {
		localStorage.removeItem('jwt_token')
		this.user.authenticated = false
	},


	refreshToken (context) {
		context.$http.get(API_HOST+'api-token-refresh', { headers: auth.getAuthHeader() }).then((data) => {
			localStorage.setItem('jwt_token', data.body.token)
		},
		(data) => { console.log(data) })
	},

	checkAuth () {
		var jwt = localStorage.getItem('jwt_token')
		if (jwt) {
			this.user.authenticated = true
		} else {
			this.user.authenticated = false
		}
	},

	getAuthHeader () {
		return {
			'Authorization': 'JWT ' + localStorage.getItem('jwt_token')
		}
	}
}
