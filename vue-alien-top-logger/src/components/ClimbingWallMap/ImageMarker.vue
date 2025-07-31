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

        gradeRangeChoices: Array, 
        holdColourChoices: Array,

        routesToAddToDatabase: Array,
        routesToDeleteFromDatabase: Array,

        routesClimbedByUserInSession: Array,
        routesClimbedByUserInDatabase: Array,
        isClimbingStaffMember: Boolean,

    },
    methods: {
        // --------------------------STAFF AND CUSTOMERS----------------------------
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
        markerSelected(marker){
            this.selectedRoute = marker;
        },
        editRoute(routeStats){
            // ------------------------------STAFF-------------------------------------------------------------
            if(this.isClimbingStaffMember) {
            this.$emit('staffEditRoute', {destroyRoute: routeStats.destroyRouteLocal, id: this.selectedRoute.id});
            } 
            // ---------------------------------------------------------------------------------------------------
            // ------------------------------------CUSTOMER-----------------------------------------------
            else {
                this.$emit('customerEditRoute', {climbedByUser: routeStats.climbedByUserLocal, id: this.selectedRoute.id});
            } 
            // ---------------------------------------------------------------------------------------------------
        },
        cancelEditRoute() {
            this.selectedRoute = null;
        },
        // ----------------------------------------------------------------------------
        // ----------------------------------------------STAFF-----------------------------------------------------
        setNewRouteLocation(event) {
            if(!this.isClimbingStaffMember) {
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

        // ---------------------------------------------------------------------------------------------------
        // ------------------------------------CUSTOMER----------------------------------------------------
        selectedRouteClimbedByUser(){
            const climbedByUserInDatabase = this.routesClimbedByUserInDatabase.map(route => route.RouteId).includes(this.selectedRoute?.id);
            const climbedByUserInSession = this.routesClimbedByUserInSession.map(route => route.RouteId).includes(this.selectedRoute?.id);
            return climbedByUserInDatabase || climbedByUserInSession;
        },
        // ---------------------------------------------------------------------------------------------------
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
                src="/alien_bloc_shape_final.jpg"
                alt= "Alien bloc"
                @click="setNewRouteLocation"
                :data-bs-toggle="this.isClimbingStaffMember ? 'modal' : ''"
                :data-bs-target="this.isClimbingStaffMember ? '#add-route' : ''"
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
    <!-- -------------------------STAFF AND CUSTOMERS--------------------------------- -->
     <EditRouteModal
        :isClimbingStaffMember="this.isClimbingStaffMember"
        :marker="this.selectedRoute? this.selectedRoute : undefined" 

        :gradeRangeChoices="this.gradeRangeChoices"
        :holdColourChoices="this.holdColourChoices"

        :selectedRouteDestroyedByUser="this.routesToDeleteFromDatabase?.includes(this.selectedRoute?.id)"
        :selectedRouteClimbedByUser="selectedRouteClimbedByUser()"

        @on-ok="editRoute"
        @on-cancel="cancelEditRoute"  
    />
    <!-- ---------------------------------------------------------- -->
    <!-- -------------------------STAFF--------------------------------- -->
    <div v-if="this.isClimbingStaffMember">
        <AddRouteModal
            :markerX= "this.newMarkerX"
            :markerY="this.newMarkerY"

            :gradeRangeChoices="this.gradeRangeChoices"
            :holdColourChoices="this.holdColourChoices"

            @on-ok="createNewRoute"
            @on-cancel="cancelNewRouteAdded"  
        />
    </div>
    <!-- ---------------------------------------------------------- -->
   
</div>
</template>
<style scoped>
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