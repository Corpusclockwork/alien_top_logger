<script>
import AddRouteModal from './AddRouteModal.vue';
import { ref, onMounted } from 'vue';
const root = ref(null);
export default {
    name: 'ImageMarker',
    data: function () {
        return {
            markers: [],
            newMarkers: [],
            newMarkerX: null,
            newMarkerY: null,
            showModal: false,
        }
    },
    props: {
        filteredRoutes: Array
    },
    methods: {
        generateMarkers() {
            // I should go back and make the markers generate while the filters are being changed 
            this.markers = [] ;
            this.filteredRoutes.forEach(route => {
                this.markers.push(
                    {
                        id: route.RouteId, 
                        colour: route.RouteColour, 
                        grade: route.RouteGradeRange, 
                        x: route.RouteLocationXAxis * 0.1, //update when backend fixed
                        y: route.RouteLocationYAxis * 0.1 //update when backend fixed
                    }
                )
            });
        },
        AddMarker(event) {
            function roundNumber(x){
                return Math.round(x*100)/100
            };
            this.newMarkerX = roundNumber((event.offsetX / document.getElementById('Alienbloc_shape_id').width) * 100);
            this.newMarkerY = roundNumber((event.offsetY / document.getElementById('Alienbloc_shape_id').height) * 100);
            this.showModal = true;
        },
        createNewRoute(newRouteObject){
            this.newMarkers.push(
                {       
                    colour: newRouteObject.hold_colour, 
                    grade: newRouteObject.grade_range, 
                    x: this.newMarkerX,
                    y: this.newMarkerY
                }
            );
            console.log(this.newMarkers);
            this.showModal=false;
            // I mean, kind of not needed but it feels like it makes things neater
            this.newMarkerX  = null;
            this.newMarkerY = null;
            
        },
        cancelNewRouteAdded(){
            // I mean, kind of not needed but it feels like it makes things neater
            this.showModal=false;
            this.newMarkerX  = null;
            this.newMarkerY = null;
        }
    },
    watch : {
        filteredRoutes() {
            this.generateMarkers();
        }
    }
}
</script>
<template>
<div ref="root"> 
    <div class="ImageMarkerContainer">
        <div class="ImageMarkerImageClass">
            <img
                id="Alienbloc_shape_id"
                src="/Alienbloc_shape.png"
                alt= "Alien bloc"
                @click="AddMarker"
            />
        </div>
    </div>
    <AddRouteModal
        v-if="showModal"
        :markerX= "newMarkerX"
        :markerY="newMarkerY"
        @on-ok="createNewRoute"
        @on-cancel="cancelNewRouteAdded"
        
    />
    <div v-for="marker in this.markers">
        <Marker
            @click="$emit('selectMarker', marker.id)"
            :id = marker.id
            :x_percentage = marker.x
            :y_percentage = marker.y
            :hold_colour = marker.colour
        />
    </div>
</div>
</template>
<style>
.ImageMarkerContainer {
    width: 100%;
    position: relative;
}
</style>