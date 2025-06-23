import { createApp } from 'vue';
import './style.css';
import App from './App.vue';
// import {createBootstrap} from 'bootstrap-vue-next'

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap';
// import 'bootstrap-vue-next/dist/bootstrap-vue-next.css';

import { createWebHistory, createRouter } from 'vue-router';
import Login from './components/Login.vue';
import UserTrackRoutes from './components/UserTrackRoutes.vue';

const routes = [
    { path: '/', component: Login },
    { path: '/login', component: Login },
    { path: '/usertrackroutes', component: UserTrackRoutes }
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

const app = createApp(App);
// app.use(createBootstrap()); // Need this to be about to use vue bootstrap

app.use(router); // need this so our CSR works
app.mount('#app');


  
