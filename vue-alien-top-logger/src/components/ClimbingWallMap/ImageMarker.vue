<script>
import AddRouteModal from '../Modals/AddRouteModal.vue';
import EditRouteModal from '../Modals/EditRouteModal.vue';
import Marker from './Marker.vue';
export default {
    name: 'ImageMarker',
    data: function () {
        return {
            markers: [],      
            newMarkerX: null,
            newMarkerY: null,
            selectedRoute: null,
        }
    },
    components: {
        AddRouteModal,
        EditRouteModal,
        Marker
    },
    props: {
        filteredRoutes: Array,
        newRoutes: Array,
        routesClimbedByUser: Array,
        routesToDeleteFromDatabase: Array,
        isStaffUser: Boolean
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
        setNewRouteLocation(event) {
            if(!this.isStaffUser) {
                return;
            }
            function roundNumber(x){
                return Math.round(x*100)/100;
            };
            this.newMarkerX = roundNumber((event.offsetX / document.getElementById('Alienbloc_shape_id').width) * 100);
            this.newMarkerY = roundNumber((event.offsetY / document.getElementById('Alienbloc_shape_id').height) * 100);
        },
        createNewRoute(newRouteObject){
            this.$emit('staffAddNewRoute', {   
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
            this.newMarkerX  = null;
            this.newMarkerY = null;
        },
        editRoute(routeStats){
            this.$emit('staffEditRoute', {destroyRoute: routeStats.destroyRouteLocal, id: this.selectedRoute.id});
            this.$emit('customerEditRoute', {climbedByUser: routeStats.climbedByUserLocal, id: this.selectedRoute.id});
        },
        cancelEditRoute() {
            this.selectedRoute = null;
        },
        markerSelected(marker){
            this.selectedRoute = marker;
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
                @click="setNewRouteLocation"
                :data-bs-toggle="this.isStaffUser ? 'modal' : ''"
                :data-bs-target="this.isStaffUser ? '#add-route' : ''"
            />
            <div v-for="marker in this.markers">
                <Marker
                    @click="markerSelected(marker)"
                    data-bs-toggle="modal"
                    data-bs-target="#edit-route"
                    :id = marker.id
                    :x_percentage = marker.x
                    :y_percentage = marker.y
                    :hold_colour = marker.colour
                />
            </div>
        </div>
    </div>
    <div v-if="this.isStaffUser">
        <AddRouteModal
            :markerX= "this.newMarkerX"
            :markerY="this.newMarkerY"
            @on-ok="createNewRoute"
            @on-cancel="cancelNewRouteAdded"  
        />
    </div>
    <EditRouteModal
        :isStaffUser="this.isStaffUser"
        :marker="this.selectedRoute? this.selectedRoute : undefined" 
        :climbedByUser="this.routesClimbedByUser.includes(this.selectedRoute?.id)"
        :destroyRoute="this.routesToDeleteFromDatabase.includes(this.selectedRoute?.id)"
        @on-ok="editRoute"
        @on-cancel="cancelEditRoute"  
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
    border-width: 1px;
    border-color: black;
    border-style: solid;

}
</style>