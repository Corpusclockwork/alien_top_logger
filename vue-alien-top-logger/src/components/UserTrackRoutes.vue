<script>
import ImageMarker from './ImageMarker.vue';
export default {
    name: 'UserTrackRoutes',
    data: function () {
        return {
            allRoutes: undefined,
            RouteGradeRangeSelected: null,
            RouteHoldColourSelected: null,
            routesFound: true,

            routesClimbedByUser: [], // will need to populate this from the backend at some point 
            routesToDeleteFromDatabase: [],

            filteredRoutes: [],
            newRoutesToSave: []
        }
    },
    components: {
        ImageMarker
    },
    beforeMount() {
        this.getRoutes()
    },
    methods: {
        async getRoutes() {
            const response = await fetch('http://127.0.0.1:8000/api/v1/routes/');
            const reader = response.body.getReader();
            let data = [];
            while (true) {
                const { done, value } = await reader.read();
                if (done) {
                    const str = new TextDecoder().decode(data[0]);
                    this.allRoutes = JSON.parse(str);
                    // if we sort the routes now, getting the newest and oldest routes will be nicer
                    // newest routes at the top
                    this.allRoutes.sort(function(a,b){
                        return new Date(b.RouteCreatedAt) - new Date(a.RouteCreatedAt);
                    });
                    console.log(this.allRoutes);
                    // this.allRoutes is a proxy array
                    return;
                }
                data.push(value);
            }
        },
        FilterRoutes(){
            this.filteredRoutes = [];
            this.allRoutes.forEach(route => {
                //ugly but functional
                if ((!this.RouteHoldColourSelected && this.RouteGradeRangeSelected) && (route.RouteGradeRange === this.RouteGradeRangeSelected)){
                    this.filteredRoutes.push(route);
                } else if ((!this.RouteGradeRangeSelected && this.RouteHoldColourSelected) && (route.RouteColour === this.RouteHoldColourSelected)){
                    this.filteredRoutes.push(route);
                } else if ((route.RouteColour === this.RouteHoldColourSelected) && (route.RouteGradeRange === this.RouteGradeRangeSelected)){
                    this.filteredRoutes.push(route);
                }
            });
            this.newRoutesToSave.forEach(route=> {
                if ((!this.RouteHoldColourSelected && this.RouteGradeRangeSelected) && (route.RouteGradeRange === this.RouteGradeRangeSelected)){
                    this.filteredRoutes.push(route);
                } else if ((!this.RouteGradeRangeSelected && this.RouteHoldColourSelected) && (route.RouteColour === this.RouteHoldColourSelected)){
                    this.filteredRoutes.push(route);
                } else if ((route.RouteColour === this.RouteHoldColourSelected) && (route.RouteGradeRange === this.RouteGradeRangeSelected)){
                    this.filteredRoutes.push(route);
                }
            });
            if(this.filteredRoutes.length > 0) {
                this.routesFound = true;
            } else {
                this.routesFound = false;
            }
        },
        staffAddNewRoute(newRoute){
            // generate a new id for the route (negative)
            newRoute.RouteId = -(this.newRoutesToSave.length + 1);
            this.newRoutesToSave.push(newRoute);
            this.FilterRoutes();
        }, 
        staffEditRoute(destroyRouteObject){
            if (destroyRouteObject.id < 0) {
                const indexOfRouteToRemove = this.newRoutesToSave.indexOf((route) => route.RouteId === destroyRouteObject.id);
                // delete fr fr rn as the route doesn't exist in the backend yet
                this.newRoutesToSave.splice(indexOfRouteToRemove, 1);   
                // since something has changed that the user can see on the image, we should filter again 
                this.FilterRoutes(); 
            } else {
                if(destroyRouteObject.destroyRoute) {
                    this.routesToDeleteFromDatabase.push(destroyRouteObject.id)
                } else {
                    const indexOfRouteToRemove = this.routesToDeleteFromDatabase.indexOf((routeId) => routeId === destroyRouteObject.id);
                    this.routesToDeleteFromDatabase.splice(indexOfRouteToRemove, 1); 
                }  
            }
        },
        customerEditRoute(customerEditRouteObject){
            if(customerEditRouteObject.climbedByUser){
                this.routesClimbedByUser.push(customerEditRouteObject.id);
            } else {
                const indexOfRouteToRemove = this.routesClimbedByUser.indexOf((route) => route.id === customerEditRouteObject.id);
                this.routesClimbedByUser.splice(indexOfRouteToRemove, 1);
            }
        }
    },
    watch : {
        RouteGradeRangeSelected() {
            this.FilterRoutes();
        },
        RouteHoldColourSelected(){
            this.FilterRoutes();
        }
    }
}
</script>

<template>
    <div class="UserTrackRoutes">
        <div class="TrackRoutesHeader">
            TRACK ROUTES
        </div>
        <div class="TrackRoutesMapContainer">
            <ImageMarker
                :filteredRoutes = this.filteredRoutes
                :newRoutes = this.newRoutesToSave
                :routesClimbedByUser = this.routesClimbedByUser
                :routesToDeleteFromDatabase = this.routesToDeleteFromDatabase
                @staffAddNewRoute="staffAddNewRoute"
                @staffEditRoute="staffEditRoute"
                @customerEditRoute="customerEditRoute"
            />
        </div>
        
        <div class="ChangeRoutesData">
            <div class="RoutesTrackedContainer">
                <div class="RoutesTrackedList">
                </div>
            </div>
            <div class="Filters"> 
                <div> APPLY FILTERS</div>
                <div v-if="!routesFound"> NO ROUTES FOUND</div>
                <div class="SearchRouteGradeContainer"> 
                    <div>Grade</div>
                    <select id="RouteGradeRange" v-model="RouteGradeRangeSelected">
                        <option  value='V0-V2'>V0-V2</option>
                        <option value="V1-V3">V1-V3</option>
                        <option value="V2-V4">V2-V4</option>
                    </select>
                </div>
                <div class="SearchRouteHoldColourContainer">
                    <div>Hold Colour</div>
                    <select id="RouteHoldColour" v-model="RouteHoldColourSelected">
                        <option value="RED">RED</option>
                        <option value="BLUE">BLUE</option>
                        <option value="GREEN">GREEN</option>
                    </select>
                </div>
            </div>
        </div>
        <div>
            CURRENT ROUTES (newest first):
            <div>
                <div v-for="route in this.allRoutes">
                    {{ route }}
                </div>
            </div>
        </div>
        <!-- FOR STAFF ONLY -->
        <div class="AddRouteData"> 
            <div>TO ADD NEW ROUTE, SELECT LOCATION ON MAP</div>
        </div>
        <div>
            New Routes add that have yet to be saved:
            <div>
                {{ this.newRoutesToSave }}
            </div>
        </div>
        <!-- ------------- -->

        <!-- FOR CUSTOMERS ONLY -->
        <div>
            ROUTES TRACKED
        </div>
        <div> Existing climbs that have been sent by user</div>
        {{ routesClimbedByUser }}
        <!-- ------------- -->
    </div>
</template>
<style>
.UserTrackRoutes {
    width: 100%;
}
.TrackRoutesMapImage {
    width: 100%;
}
.TrackRoutesHeader {
    font-family: Arial, Helvetica, sans-serif;
    color: red;
}
.TrackRoutesMap{
    width: 90%;
}
.ImageMarkerClass {
    width: 100%;
}
</style>
