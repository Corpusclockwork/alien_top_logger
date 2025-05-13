import { createApp } from 'vue';
import './style.css';
import App from './App.vue';
import ImageMarker from './components/ImageMarker.vue';
import Marker from './components/Marker.vue';
import AddRouteModal from './components/AddRouteModal.vue'

const app = createApp(App);

app
.component('ImageMarker', ImageMarker)
.component('Marker', Marker)
.component('AddRouteModal', AddRouteModal)

app.mount('#app');


  
