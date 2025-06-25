<script>
import ImageMarker from './ClimbingWallMap/ImageMarker.vue';
export default {
    name: 'MainPage',
    data: function () {
        return {
            isStaffUser: true, // TWEAK THIS FOR QUICK TESTING
            allRoutes: undefined,
            RouteGradeRangeSelected: null,
            RouteHoldColourSelected: null,
            routesFound: true,
            // Users
            routesClimbedByUser: [], // will need to populate this from the backend at some point 
            // Staff
            routesToDeleteFromDatabase: [],
            newRoutesToSave: [],

            filteredRoutes: []
            
        }
    },
    components: {
        ImageMarker
    },
    beforeMount() {
        // get user details (from props maybe) and check if the current user is a staff user
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
                // since something has changed that the user can see on the climbing wall map, we should filter again 
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
    <div class="MainPage">
        <div v-if="!isStaffUser" class="MainPageHeader">
            TRACK ROUTES
        </div>
        <div v-if="isStaffUser" class="MainPageHeader">
            EDIT ROUTES
        </div>
        <div v-if="isStaffUser"class="AddRoute"> 
            <div>Click on map to add a route</div>
        </div>
        <div class="SaveChanges"> 
            <div>Save changes to the database</div>
        </div>
        <div>
            <ImageMarker
                :filteredRoutes = this.filteredRoutes
                :newRoutes = this.newRoutesToSave
                :routesToDeleteFromDatabase = this.routesToDeleteFromDatabase
                :routesClimbedByUser = this.routesClimbedByUser
                @staffAddNewRoute="staffAddNewRoute"
                @staffEditRoute="staffEditRoute"
                @customerEditRoute="customerEditRoute"
                :isStaffUser="this.isStaffUser"
            />
        </div>
        <form> 
            <div class="row">
                <div class="col">
                    <div class="Filters"> 
                        <div> Apply filters to see routes on the map</div>
                        <div>Route Grade:</div>
                        <select class="form-select" id="RouteGradeRange" v-model="RouteGradeRangeSelected">
                            <option  value='V0-V2'>V0-V2</option>
                            <option value="V1-V3">V1-V3</option>
                            <option value="V2-V4">V2-V4</option>
                        </select>
                        <div>Route Hold Colour:</div>
                        <select class="form-select" id="RouteHoldColour" v-model="RouteHoldColourSelected">
                            <option value="RED">RED</option>
                            <option value="BLUE">BLUE</option>
                            <option value="GREEN">GREEN</option>
                        </select>
                    </div>
                </div>
                <div class="col">
                    <div v-if=" !isStaffUser">
                        Routes climbed By You:
                        <div>
                            {{ this.routesClimbedByUser }}
                        </div>
                    </div>
                    <div v-if="isStaffUser">
                        <div>
                            Routes <span class="font-weight-bold">added</span> by you just now:
                            <div>
                                {{ this.newRoutesToSave }}
                            </div>
                        </div>
                        <div>
                            Routes <span class="font-weight-bold">deleted</span> by you just now:  
                            <div>
                                {{ this.routesToDeleteFromDatabase }}
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col listOfRoutes" data-bs-spy="scroll">
                    List of Routes:
                    <div class="list-group overflow-scroll" v-for="route in this.allRoutes">
                        <div class="list-group-item"> {{ route }}</div>
                    </div>
                </div>
            </div>
        </form>
    </div>
</template>
<style>
.MainPage {
    margin: 5%;
    margin-bottom: 0%;
    border-style: solid;
    border-width: 2px;
    border-color: #E13B3B;
    background-color: white;
}
.listOfRoutes {
    font-family: "Montserrat", Sans-serif;
}
</style>
