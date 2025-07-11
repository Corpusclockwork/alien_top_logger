import { createApp } from 'vue';
import './style.css';
import App from './App.vue';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap';

// font-family: "Montserrat", Sans-serif;
// font-family: "Teko", Sans-serif;
//background-image: linear-gradient(82deg, var( --e-global-color-primary ) 0%, var( --e-global-color-649cea3 ) 100%);
// #E13B3B
// #E9704B
// I haven't implemented locking for staff users so they can't both edit the same route at once, maybe something to think about later
// If I wind up with staff being able to change the location of the route especially 

const app = createApp(App);
app.mount('#app');


  
