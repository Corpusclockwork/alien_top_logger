import { createApp } from 'vue';
import './style.css';
import App from './App.vue';
import ImageMarker from './components/ImageMarker.vue';
import Marker from './components/Marker.vue';
import AddRouteModal from './components/AddRouteModal.vue';
import {createBootstrap} from 'bootstrap-vue-next'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue-next/dist/bootstrap-vue-next.css'

const app = createApp(App);
app.use(createBootstrap()) // Important

app
.component('ImageMarker', ImageMarker)
.component('Marker', Marker)
.component('AddRouteModal', AddRouteModal)

app.mount('#app');


  
