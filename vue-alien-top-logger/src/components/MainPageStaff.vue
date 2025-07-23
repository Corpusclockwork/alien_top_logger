<script>
import ImageMarker from './ClimbingWallMap/ImageMarker.vue';
export default {
    name: 'MainPageStaff',
    data: function () {
        return {
            allRoutes: null,
            RouteGradeRangeSelected: "",
            RouteHoldColourSelected: "",
            routesToDeleteFromDatabase: [],
            routesToAddToDatabase: [],
            filteredRoutes: []
        }
    },
    props: {
        isClimbingStaffMember: Boolean,
        csrfToken: String,
        username: String
    },
    components: {
        ImageMarker
    },
    created() {
        this.getRoutes();
        this.getTrackedRoutesForUser(); 
    },
    methods: {
        async getRoutes() {
            const response = await fetch('http://localhost:8000/api/v1/routes/');
            const data = await response.json()
             this.allRoutes = data.routes;
             this.allRoutes.sort(function(a,b){
                return new Date(b.RouteCreatedAt) - new Date(a.RouteCreatedAt);
            });
            console.log(this.allRoutes);
        },
        async saveNewRoutesInDatabase() {
            //clear the negative ids we have been using for the routes
            this.routesToAddToDatabase.forEach((route) => {delete route.RouteId});
            const response = await fetch("http://localhost:8000/api/v1/routes/create/", {
                method: "POST",
                headers: {
                    'Content-Type': 'application/json',
                    "X-CSRFToken": this.csrfToken
                },
                credentials: "include",
                body: JSON.stringify(this.routesToAddToDatabase)
            });
        },
        async deleteRoutesFromDatabase() {
            const ids = this.routesToDeleteFromDatabase.map(route => route.RouteId);
            const response = await fetch("http://localhost:8000/api/v1/routes/delete/", {
                credentials: "include",
                method: "DELETE",
                headers: {
                    'Content-Type': 'application/json',
                    "X-CSRFToken": this.csrfToken
                },
                body: JSON.stringify(ids)
            });
        },
        async saveToDatabase(){
            if(this.routesToAddToDatabase.length > 0){
                await this.saveNewRoutesInDatabase() ;
            }
            if(this.routesToDeleteFromDatabase.length > 0){
                await this.deleteRoutesFromDatabase();
            }
            this.routesToAddToDatabase = [];
            this.routesToDeleteFromDatabase = [];
            this.RouteGradeRangeSelected = "";
            this.RouteHoldColourSelected = "";
            this.getRoutes();
        },
        FilterRoutes(routeSelected){
            this.filteredRoutes = [];
            if(routeSelected){
                this.filteredRoutes.push(routeSelected);
                this.RouteGradeRangeSelected = "";
                this.RouteHoldColourSelected = "";
                return;
            }
            this.allRoutes.forEach(route => {
                //ugly but functional
                //("" is false in javascript)
                if ((!this.RouteHoldColourSelected && this.RouteGradeRangeSelected) && (route.RouteGradeRange === this.RouteGradeRangeSelected)){
                    this.filteredRoutes.push(route);
                } else if ((!this.RouteGradeRangeSelected && this.RouteHoldColourSelected) && (route.RouteColour === this.RouteHoldColourSelected)){
                    this.filteredRoutes.push(route);
                } else if ((route.RouteColour === this.RouteHoldColourSelected) && (route.RouteGradeRange === this.RouteGradeRangeSelected)){
                    this.filteredRoutes.push(route);
                }
            });
            this.routesToAddToDatabase.forEach(route=> {
                if ((!this.RouteHoldColourSelected && this.RouteGradeRangeSelected) && (route.RouteGradeRange === this.RouteGradeRangeSelected)){
                    this.filteredRoutes.push(route);
                } else if ((!this.RouteGradeRangeSelected && this.RouteHoldColourSelected) && (route.RouteColour === this.RouteHoldColourSelected)){
                    this.filteredRoutes.push(route);
                } else if ((route.RouteColour === this.RouteHoldColourSelected) && (route.RouteGradeRange === this.RouteGradeRangeSelected)){
                    this.filteredRoutes.push(route);
                }
            });
        },
        staffAddNewRoute(newRoute){
            // generate a new id for the route (negative)
            newRoute.RouteId = -(this.routesToAddToDatabase.length + 1);
            this.routesToAddToDatabase.push(newRoute);
            this.FilterRoutes();
        }, 
        staffEditRoute(destroyRouteObject){
            if (destroyRouteObject.id < 0) {
                const indexOfRouteToRemove = this.routesToAddToDatabase.indexOf((route) => route.RouteId === destroyRouteObject.id);
                // delete fr fr rn as the route doesn't exist in the backend yet
                this.routesToAddToDatabase.splice(indexOfRouteToRemove, 1);   
                // since something has changed that the user can see on the climbing wall map, we should filter again 
                this.FilterRoutes(); 
            } else {
                if(destroyRouteObject.destroyRoute) {
                    const routeToDestroy = this.allRoutes.find((route) => route.RouteId === destroyRouteObject.id);
                    this.routesToDeleteFromDatabase.push(routeToDestroy)
                } else {
                    const indexOfRouteToRemove = this.routesToDeleteFromDatabase.indexOf((route) => route.RouteId === destroyRouteObject.id);
                    this.routesToDeleteFromDatabase.splice(indexOfRouteToRemove, 1); 
                }  
            }
        },
        logOutUser() {
            this.$emit("logoutUser");
        }
    },
    watch : {
        RouteGradeRangeSelected() {
            if(this.RouteGradeRangeSelected !== ""){
                this.FilterRoutes();
            }
        },
        RouteHoldColourSelected(){
            if(this.RouteHoldColourSelected !== ""){
                this.FilterRoutes();
            } 
        }
    }
}
</script>
<template>
    <div class="mainPage">
        <div class="mainPageHeaderSection">
            <button @click="logOutUser()" type="button" class="loginButton btn btn-primary">Logout User</button>
            <div>{{username}}</div>
            <div class="MainPageHeader">
                Edit Routes
            </div>
            <button @click="saveToDatabase();"class="SaveChanges"> 
                <div>Save changes to the database</div>
            </button>
        </div>
        <div class="mainPageBodySection">
            <div class="addRoute"> 
                <div>Click on map to add a route</div>
            </div>
            <div>
                <ImageMarker
                    :isClimbingStaffMember = this.isClimbingStaffMember
                    :filteredRoutes = this.filteredRoutes
                    :routesToAddToDatabase = this.routesToAddToDatabase
                    :routesToDeleteFromDatabase = this.routesToDeleteFromDatabase
                    @staffAddNewRoute="staffAddNewRoute"
                    @staffEditRoute="staffEditRoute"
                />
            </div>
            <form class="mainPageForm"> 
                <div class="mainPageFormSection">
                    <div class="applyFilters"> Apply filters to see routes on the map</div>
                    <div class="filterSubsection">
                        <div class="filterSubsectionHeader">Grade:</div>
                        <select class="form-select mainPageSelectForm" id="RouteGradeRange" v-model="RouteGradeRangeSelected">
                            <option value="" selected>Not specified</option>
                            <option value='V0-V2'>V0-V2</option>
                            <option value="V1-V3">V1-V3</option>
                            <option value="V2-V4">V2-V4</option>
                        </select>
                    </div>
                    <div class="filterSubsection">
                        <div class="filterSubsectionHeader">Hold Colour:</div>
                        <select class="form-select mainPageSelectForm" id="RouteHoldColour" v-model="RouteHoldColourSelected">
                            <option value="" selected>Not specified</option>
                            <option value="RED">RED</option>
                            <option value="BLUE">BLUE</option>
                            <option value="GREEN">GREEN</option>
                        </select>
                    </div>
                </div>
                <div class="mainPageFormSection">
                    <div class="mainPageFormMiddleSection">
                        <div>
                            Routes <span class="fw-bold">added</span> by you just now:
                            <div v-show="this.routesToAddToDatabase.length > 0" class="editRoutesSectionList">
                                <div class="list-group overflow-scroll" v-for="route in this.routesToAddToDatabase">
                                    <div @click="FilterRoutes(route)" class="list-group-item"> 
                                        <div> {{ route.RouteColour }}</div>
                                        <div> {{ route.RouteGradeRange }}</div>
                                        <div> <span class="fw-bold">Location: </span> {{ route.RouteLocationXAxis }}, {{ route.RouteLocationYAxis }}</div>
                                    </div>
                                </div>
                            </div>

                            <div v-show="this.routesToAddToDatabase.length === 0" class="mainPageFormMiddleSectionWarning fw-bold">
                                No routes added by you
                            </div>
                        </div>
                        <div>
                            Routes <span class="fw-bold">deleted</span> by you just now:  
                            <div v-show="this.routesToDeleteFromDatabase.length > 0" class="editRoutesSectionList">
                                <div class="list-group overflow-scroll" v-for="route in this.routesToDeleteFromDatabase">
                                    <div @click="FilterRoutes(route)" class="list-group-item"> 
                                        <div> {{ route.RouteColour }}</div>
                                        <div> {{ route.RouteGradeRange }}</div>
                                        <div> <span class="fw-bold">Location: </span> {{ route.RouteLocationXAxis }}, {{ route.RouteLocationYAxis }}</div>
                                    </div>
                                </div>
                            </div>
                            <div v-show="this.routesToDeleteFromDatabase.length === 0" class="mainPageFormMiddleSectionWarning fw-bold">
                                No routes deleted by you 
                            </div>
                        </div>
                    </div>
                </div>
                <div class="mainPageFormSection listOfRoutesSection" >
                    <div class="listOfRoutesHeader">List of Routes in the Database: </div>
                    <div class="listOfRoutes">
                        <div class="list-group overflow-scroll" v-for="route in this.allRoutes">
                            <div @click="FilterRoutes(route)" class="list-group-item"> 
                                <div> {{ route.RouteColour }}</div>
                                <div> {{ route.RouteGradeRange }}</div>
                                <div> <span class="fw-bold">Created On: </span> {{ route.RouteCreatedAt }}</div>
                                <div> <span class="fw-bold">Location: </span> {{ route.RouteLocationXAxis }}, {{ route.RouteLocationYAxis }}</div>
                            </div>
                        </div>
                    </div>
                </div>
            </form>
        </div>
    </div>
</template>
<style>
/* .mainPage {
    margin: 5%;
    line-height: 1;
    margin-bottom: 0%;
    background: rgba(255, 255, 255, 0.85);
    font-size: 1em;
    border-radius: 5px;
} */

.mainPage {
    padding: 2% 10% 10% 10%;
    line-height: 1;
    border-radius: 5px;
    color: white;
    font-size: 1rem;
    display: grid;
}

#select:focus {
    border-color: #66afe9;
    outline: 0;
    -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075),0 0 8px rgba(255,175,233,.6);
    box-shadow: inset 0 1px 1px rgba(0,0,0,.075),0 0 8px rgba(255,175,233,.6);
}
.addRoute {
    font-family: "Montserrat", Sans-serif;
    font-weight: bold;
    background-color: #E13B3B;
    color: white;
    padding: 5px;
    max-width: fit-content;
}

.mainPageForm {
    padding: 2px;
    display: flex;
    font-family: "Montserrat", Sans-serif;
}
.mainPageFormSection {
    flex: 1;
}
@media only screen and (max-width: 500px) {
    .mainPageForm{
        display: inline;
    }
}

.mainPageHeaderSection {
    display: flex;
    background: rgba(0, 0, 0, 1);
    padding: 30px;
}

.MainPageHeader {
    flex: 1 1;
    padding: 2px;
    color: white;
    font-size: 4em;
}

.SaveChanges{
    font-size: 2em;
    flex: 1 1;
    text-align: center;
    background-color: #E13B3B;
    color: white;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 5px;
    margin: 2px;
} 

.SaveChanges:hover {
    background-color: #882323;
    cursor: pointer; 
}

.mainPageBodySection {
    color: black;
    text-align: center;
    background: rgba(255, 255, 255, 0.85);
}

.applyFilters {
    font-size: 0.8em;
    font-weight: bold;
    color: #E13B3B;
    margin-top: 2%;
    margin-bottom: 2%;
}


.filterSubsection {
    display: flex;
    padding: 2%;
    justify-content: center;
    align-items: center;
}
.filterSubsectionHeader {
    flex: 1 1;
}
.mainPageSelectForm {
    flex: 1 1;
    padding: 2%;
}

.mainPageSelectForm:hover {
     cursor: pointer; 
}

.mainPageFormMiddleSection {
    padding: 5%;
}
.form-select {
    border-width: 3px;
    border-radius: 5px;
    border-color: #E9704B;
}

.mainPageFormMiddleSectionWarning {
    background-color: #E9704B;
    color: white;
    border-radius: 5px;
    padding: 3%;
    margin: 2%;
}

.listOfRoutes {
    height: 300px;
    overflow:scroll;
    border-width: 3px;
    border-radius: 5px;
    border-color: #E9704B;
    border-style: solid;
    background-color: white;
    color: white;
    scrollbar-color: #E13B3B white;
    scrollbar-width: medium;
    
}
.listOfRoutesHeader {
    padding: 3%;
    margin: 2%;
}

.editRoutesSectionList {
    height: 100px;
    overflow:scroll;
    border-width: 3px;
    border-radius: 5px;
    border-color: #E9704B;
    background-color: white;
    border-style: solid;
    scrollbar-color: #E13B3B white;
    scrollbar-width: medium;
    margin: 3px;
}

.list-group-item {
    background: rgba(255, 255, 255, 0.5);
    border-radius: 0;
    border-width: 1px;
    border-color: black;
    border-style: solid;
}

.list-group-item:hover {
     cursor: pointer; 
}



</style>
