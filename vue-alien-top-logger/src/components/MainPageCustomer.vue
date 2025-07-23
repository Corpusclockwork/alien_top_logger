<script>
import ImageMarker from './ClimbingWallMap/ImageMarker.vue';
export default {
    name: 'MainPageCustomer',
    data: function () {
        return {
            allRoutes: null,
            RouteGradeRangeSelected: "",
            RouteHoldColourSelected: "",
            routesClimbedByUserInSession: [], 
            routesClimbedByUserInDatabase: [],
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
        async getTrackedRoutesForUser() {
            const response = await fetch('http://localhost:8000/api/v1/routes/getuserroutes/', {
                credentials: "include",
                // look, we are getting sensitive data so I'm using a POST request, you can take it up with my manager who is also me :)))
                method: "POST",
                headers: {
                    'Content-Type': 'application/json',
                    "X-CSRFToken": this.csrfToken
                },
                body: JSON.stringify({'username': this.username})
            });
            const data = await response.json();
            this.routesClimbedByUserInDatabase = data.routesClimbedByUser;
        },
        async trackRoutesInDatabase() {
            const routeIdsAdd = this.routesClimbedByUserInSession.map(route => route.RouteId);
            const response = await fetch("http://localhost:8000/api/v1/routes/track", {
                credentials: "include",
                method: "POST",
                headers: {
                    'Content-Type': 'application/json',
                    "X-CSRFToken": this.csrfToken
                },
                body: JSON.stringify({'username': this.username, 'routesClimbedByUser': routeIdsAdd})
            });
        },
        async saveToDatabase(){
            if (this.routesClimbedByUserInSession.length > 0 ) {
                await this.trackRoutesInDatabase()
            }
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
            this.newRoutesToSave.forEach(route=> {
                if ((!this.RouteHoldColourSelected && this.RouteGradeRangeSelected) && (route.RouteGradeRange === this.RouteGradeRangeSelected)){
                    this.filteredRoutes.push(route);
                } else if ((!this.RouteGradeRangeSelected && this.RouteHoldColourSelected) && (route.RouteColour === this.RouteHoldColourSelected)){
                    this.filteredRoutes.push(route);
                } else if ((route.RouteColour === this.RouteHoldColourSelected) && (route.RouteGradeRange === this.RouteGradeRangeSelected)){
                    this.filteredRoutes.push(route);
                }
            });
        },
        customerEditRoute(customerEditRouteObject){
            const routeToTrack = this.allRoutes.find((route) => route.RouteId === customerEditRouteObject.id);
            if(customerEditRouteObject.climbedByUser){
                this.routesClimbedByUserInSession.push(routeToTrack);
            } else {
                const indexOfRouteToRemove = this.routesClimbedByUserInSession.indexOf((route) => route.id === customerEditRouteObject.id);
                this.routesClimbedByUserInSession.splice(indexOfRouteToRemove, 1);
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
                Track Routes
            </div>
            <button @click="saveToDatabase();"class="SaveChanges"> 
                <div>Save changes to the database</div>
            </button>
        </div>
        <div class="mainPageBodySection">
            <div>
                <ImageMarker
                    :isClimbingStaffMember = this.isClimbingStaffMember
                    :filteredRoutes = this.filteredRoutes
                    :routesClimbedByUserInDatabase = this.routesClimbedByUserInDatabase
                    :routesClimbedByUserInSession = this.routesClimbedByUserInSession
                    @customerEditRoute="customerEditRoute"
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
                        <div v-show="this.routesClimbedByUserInSession.length > 0">
                            <div>Routes climbed By You this session:</div>
                            <div class="editRoutesSectionList">
                                <div class="list-group overflow-scroll" v-for="route in this.routesClimbedByUserInSession.added">
                                    <div @click="FilterRoutes(route)" class="list-group-item"> 
                                        <div> {{ route.RouteColour }}</div>
                                        <div> {{ route.RouteGradeRange }}</div>
                                        <div> <span class="fw-bold">Location: </span> {{ route.RouteLocationXAxis }}, {{ route.RouteLocationYAxis }}</div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div v-show="this.routesClimbedByUserInSession.length === 0" class="mainPageFormMiddleSectionWarning fw-bold">
                            No routes tracked by you this session
                        </div>
                        <div>Routes climbed By You in Database:</div>
                        <div v-show="this.routesClimbedByUserInDatabase.length > 0" class="editRoutesSectionList">
                            <div class="list-group overflow-scroll" v-for="route in this.routesClimbedByUserInDatabase">
                                <div @click="FilterRoutes(route)" class="list-group-item"> 
                                    <div> {{ route.RouteColour }}</div>
                                    <div> {{ route.RouteGradeRange }}</div>
                                    <div> <span class="fw-bold">Location: </span> {{ route.RouteLocationXAxis }}, {{ route.RouteLocationYAxis }}</div>
                                </div>
                            </div>
                        </div>
                        <div v-show="this.routesClimbedByUserInDatabase.length === 0" class="mainPageFormMiddleSectionWarning fw-bold">
                            No routes tracked by you in the database
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
