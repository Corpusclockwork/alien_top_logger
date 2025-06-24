import { createApp } from 'vue';
import './style.css';
import App from './App.vue';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap';
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

app.use(router);
app.mount('#app');


  
