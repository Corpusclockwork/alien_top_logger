import { createApp } from 'vue';
import './style.css';
import App from './App.vue';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap';
import { createWebHistory, createRouter } from 'vue-router';
import Login from './components/LoginPages/Login.vue';
import MainPage from './components/MainPage.vue';
import NewUser from './components/LoginPages/NewUser.vue';
// font-family: "Montserrat", Sans-serif;
// font-family: "Teko", Sans-serif;
//background-image: linear-gradient(82deg, var( --e-global-color-primary ) 0%, var( --e-global-color-649cea3 ) 100%);
// #E13B3B
// #E9704B
// I haven't implemented locking for staff users so they can't both edit the same route at once, maybe something to think about later
// If I wind up with staff being able to change the location of the route especially 
// will have something in the backend to make sure that the same route can't be deleted twice tho 
// I also haven't made it so that you can add users to tha databse, so you have to use the pre built set of users that I made

const routes = [
    { path: '/', component: Login },
    { path: '/login', component: Login },
    { path: '/createnewuser', component: NewUser },
    { path: '/usertrackroutes', component: MainPage }
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

const app = createApp(App);

app.use(router);
app.mount('#app');


  
