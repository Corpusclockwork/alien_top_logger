<script>
import ImageMarker from './ImageMarker.vue';
export default {
    name: 'UserTrackRoutes',
    data: function () {
        return {
            allRoutes: undefined,
            RouteGradeRangeSelected: null,
            RouteHoldColourSelected: null,
            filteredRoutes: [],
            routesFound: true,
            addedMarkerIds: new Set()
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
            if(this.filteredRoutes.length > 0) {
                this.routesFound = true;
            } else {
                this.routesFound = false;
            }
        },
        addSelectedMarker(id) {
            this.addedMarkerIds.add(id);
            console.log("send marker ids to the backend");
            console.log(this.addedMarkerIds);
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
                @selectMarker="addSelectedMarker"
            />
        </div>
        <!-- ONLY STAFF USERS SHOULD HAVE THIS SECTION -->
        <div class="AddRouteData"> 
            <div>TO ADD NEW ROUTE, SELECT LOCATION ON MAP</div>
        </div>
        <!--  -->
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
