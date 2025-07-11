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
// I'm making a SPA bcasue it's nicer for users to interact with and means I can have a seeprate front and back end which
//  I would prefer than using DJAngo and 
// Its a small app so it thnk havong django just searve the vue files up is fine, if this evr gets real users I'll hav eto decouple them probably, but I don't think I'll need mulstiple server for a while
// I think I'm gonna go with cookie session authentictaion, if Django is gonna serve up my front end. 

const app = createApp(App);
app.mount('#app');


  
