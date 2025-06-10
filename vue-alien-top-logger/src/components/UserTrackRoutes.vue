<script>
import { BListGroup } from 'bootstrap-vue-next';
import ImageMarker from './ImageMarker.vue';
import { BListGroupItem } from 'bootstrap-vue-next';
export default {
    name: 'UserTrackRoutes',
    data: function () {
        return {
            allRoutes: undefined,
            RouteGradeRangeSelected: null,
            RouteHoldColourSelected: null,
            routesFound: true,

            filteredRoutes: [],
            newRoutesToSave: []
        }
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
                    console.log(this.allRoutes);
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
            this.newRoutesToSave.push(newRoute);
        },
        logSelectedRouteForUser(id) {
          
        }
    },
    watch : {
        RouteGradeRangeSelected() {
            this.FilterRoutes();
        },
        RouteHoldColourSelected(){
            this.FilterRoutes();
        },
        newRoutesToSave(){
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
                @newMarker="staffAddNewRoute"
                @logSelectedRouteForUser="logSelectedRouteForUser"
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
            <BListGroup>
                <BListGroupItem v-for="route in this.allRoutes">
                    {{ route }}
                </BListGroupItem>
            </BListGroup>
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
