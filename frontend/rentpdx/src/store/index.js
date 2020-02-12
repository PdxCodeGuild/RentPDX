import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import Vuex from 'vuex'
import router from '../router'


Vue.use(VueAxios, axios)
Vue.use(Vuex)

export default new Vuex.Store({

    state: {
        //store state information ie: user, username, userid, email
    },

    getters: {
        /*
        get information from actions

        examples: userId(state){ 
            return state.authUser.user_id
        }

        */
    },

    mutations: {
        //mutations set the state, use for authorization
    },
    actions: {
        //actions are methods, ie: axios calls, data manipulation etc...
    }
})