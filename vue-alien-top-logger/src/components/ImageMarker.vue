<script>
import AddRouteModal from './AddRouteModal.vue';
import MarkerSelectedModal from './MarkerSelectedModal.vue';
export default {
    name: 'ImageMarker',
    data: function () {
        return {
            markers: [],      
            newMarkerX: null,
            newMarkerY: null,

            showAddRouteModal: false,
            showMarkerSelectedModal: false
        }
    },
    props: {
        filteredRoutes: Array,
        newRoutes: Array
    },
    methods: {
        generateMarkers() {
            this.markers = [] ;
            this.filteredRoutes.forEach(route => {
                this.markers.push(
                    {
                        id: route.RouteId, 
                        colour: route.RouteColour, 
                        grade: route.RouteGradeRange, 
                        x: Number(route.RouteLocationXAxis),
                        y: Number(route.RouteLocationYAxis)
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
            this.showAddRouteModal = true;
        },
        createNewRoute(newRouteObject){
            this.showAddRouteModal=false;
            this.$emit('newMarker', {       
                    RouteColour: newRouteObject.hold_colour, 
                    RouteGradeRange: newRouteObject.grade_range, 
                    RouteLocationXAxis: this.newMarkerX,
                    RouteLocationYAxis: this.newMarkerY
                });
            // I mean, kind of not needed but it feels like it makes things neater
            this.newMarkerX  = null;
            this.newMarkerY = null;
            
        },
        cancelNewRouteAdded(){
            // I mean, kind of not needed but it feels like it makes things neater
            this.showAddRouteModal=false;
            this.newMarkerX  = null;
            this.newMarkerY = null;
        },
        markerSelected(){
            this.showMarkerSelectedModal=true;
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
<div> 
    <div class="ImageMarkerContainer">
        <div>
            <img
                class="ImageMarkerImageClass"
                id="Alienbloc_shape_id"
                src="/Alienbloc_shape.png"
                alt= "Alien bloc"
                @click="AddMarker"
            />
            <div v-for="marker in this.markers">
                <Marker
                    @click="markerSelected"
                    :id = marker.id
                    :x_percentage = marker.x
                    :y_percentage = marker.y
                    :hold_colour = marker.colour
                />
            </div>
        </div>
    </div>
    <AddRouteModal
        v-if="showAddRouteModal"
        :markerX= "newMarkerX"
        :markerY="newMarkerY"
        @on-ok="createNewRoute"
        @on-cancel="cancelNewRouteAdded"  
    />
    <MarkerSelectedModal
        v-if="showMarkerSelectedModal"
        :marker="this.markers[0]" 
    />
</div>
</template>
<style>
.ImageMarkerContainer {
    width: 100%;
    position: relative;
}
.ImageMarkerImageClass {
    width: 100%;
}
</style>