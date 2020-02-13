import Vue from 'vue'
import VueRouter from 'vue-router'

import Dashboard from '../components/Dashboard.vue'
import Favorites from '../components/Favorites.vue'
import Login from '../components/Login.vue'
import Landing from '../components/Landing.vue'

import index from '../store'


Vue.use(VueRouter)
const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            //this is where we set our routes to each page
            //path, names,  components, 3 ways to reference one thing
            path: '/',
            name: 'landing',
            component: 'Landing',

        },
        {
            //this is where we set our routes to each page
            //path, names,  components, 3 ways to reference one thing
            path: '/login',
            name: 'login',
            component: 'Login',

        },
        {
            //this is where we set our routes to each page
            //path, names,  components, 3 ways to reference one thing
            path: '/dashboard',
            name: 'dashboard',
            component: 'Dashboard',

        },
        {
            //this is where we set our routes to each page
            //path, names,  components, 3 ways to reference one thing
            path: '/favorites',
            name: 'favorites',
            component: 'Favorites',

        },
        
    ]
})

export default router
