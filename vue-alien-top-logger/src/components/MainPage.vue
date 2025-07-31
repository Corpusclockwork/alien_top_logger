<script>
import ImageMarker from './ClimbingWallMap/ImageMarker.vue';
import SelectOption from './SelectOption.vue';
export default {
    name: 'MainPage',
    data: function () {
        return {
            allRoutes: null,
            RouteGradeRangeSelected: "",
            RouteHoldColourSelected: "",
            gradeRangeChoices: undefined,
            holdColourChoices: undefined,


            // ------------------STAFF -------------------------
            routesToDeleteFromDatabase: [],
            routesToAddToDatabase: [],
            // -------------------------------------------------
            // -----------------CUSTOMER-------------------------
            routesClimbedByUserInSession: [], 
            routesClimbedByUserInDatabase: [],
            // -------------------------------------------------
            filteredRoutes: []
        }
    },
    props: {
        isClimbingStaffMember: Boolean,
        csrfToken: String,
        username: String
    },
    components: {
        ImageMarker,
        SelectOption
    },
    created() {
        this.getRoutes();
        this.getGradeRanges();
        this.getHoldColours();
        // --------------------------CUSTOMER-------------------
        if (!this.isClimbingStaffMember) {
            this.getTrackedRoutesForUser(); 
        }
        // -----------------------------------------------------
    },
    methods: {
        // ------------------------------------------ STAFF AND CUSTOMER ------------------------------------------------------
         async getRoutes() {
            const response = await fetch('http://localhost:8000/api/v1/routes/');
            const data = await response.json()
             this.allRoutes = data.routes;
             this.allRoutes.sort(function(a,b){
                return new Date(b.RouteCreatedAt) - new Date(a.RouteCreatedAt);
            });
            console.log(this.allRoutes);
        },
        async getGradeRanges() {
            const response = await fetch('http://localhost:8000/api/v1/routes/graderanges/');
            const data = await response.json()
            this.gradeRangeChoices = data.gradeRangeChoices;
        },
        async getHoldColours() {
            const response = await fetch('http://localhost:8000/api/v1/routes/holdcolours/');
            const data = await response.json()
            this.holdColourChoices = data.holdColourChoices;
        },
        async saveToDatabase(){
            // ------------------------STAFF ------------------------------
            if (this.isClimbingStaffMember){
                if(this.routesToAddToDatabase.length > 0){
                    await this.saveNewRoutesInDatabase() ;
                }
                if(this.routesToDeleteFromDatabase.length > 0){
                    await this.deleteRoutesFromDatabase();
                }
                this.routesToAddToDatabase = [];
                this.routesToDeleteFromDatabase = [];
                await this.getRoutes();
            // ----------------------------- ------------------------------
            // ------------------------CUSTOMER ------------------------------
            } else if (!this.isClimbingStaffMember){
                if(this.routesClimbedByUserInSession.length > 0){
                    await this.trackRoutesInDatabase() ;
                }
                await this.getTrackedRoutesForUser();
                this.routesClimbedByUserInSession = [];
            }
            // -----------------------------------------------------------
            this.RouteGradeRangeSelected = "";
            this.RouteHoldColourSelected = "";
        },
        FilterRoutes(routeSelected){
            this.filteredRoutes = [];
            if(routeSelected){
                this.filteredRoutes.push(routeSelected);
                this.RouteGradeRangeSelected = "";
                this.RouteHoldColourSelected = "";
                return;
            }
            if (!this.RouteHoldColourSelected && !this.RouteGradeRangeSelected){
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
        // --------------------------------------------------------------------------------
        // -------------------------STAFF --------------------------------------------------
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
        // ------------------------------------------------------------------------------------------
        // ----------------------------------------------CUSTOMER-------------------------------------
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
            const response = await fetch("http://localhost:8000/api/v1/routes/track/", {
                credentials: "include",
                method: "POST",
                headers: {
                    'Content-Type': 'application/json',
                    "X-CSRFToken": this.csrfToken
                },
                body: JSON.stringify({'username': this.username, 'routesClimbedByUser': routeIdsAdd})
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
        // ------------------------------------------------------------------------------------------------------
        // --------------------------LOGOUT USER-------------------------------------------
        logOutUser() {
            this.$emit("logoutUser");
        }
        // --------------------------------------------------------------------------------
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
    <button @click="logOutUser()" type="button" class="logoutButton">Logout User</button>
    <div class="mainPage">
        <!-- -----------------------HEADER------------------------------------------------- -->
        <div class="mainPageHeaderSection">
            <div class="mainPageUsernameHeaderSection">
                <div class="mainPageUsername">
                    {{username}}
                </div>
                <!-- ----------STAFF------- -->
                <div v-if="isClimbingStaffMember" class="mainPageHeader">
                    Staff Account: Edit Routes
                </div>
                <!-- ----------------------- -->
                <!-- ----------CUSTOMER------- -->
                <div v-if="!isClimbingStaffMember" class="mainPageHeader">
                    Track Your Routes
                </div>
                <!-- ------------------------- -->
            </div>
            <button @click="saveToDatabase();"class="saveChanges"> 
                Save changes to the database
            </button>
        </div>
        <!-- ------------------------------------------------------------------------ -->
         <!-- -----------------------BODY------------------------------------------------- -->
        <div class="mainPageBodySection">
            <!-- ---------------STAFF------------ -->
            <div v-if="isClimbingStaffMember" class="addRoute"> 
                <div>Click on map to add a route</div>
            </div>
            <!-- --------------------------------- -->
            <div>
                <ImageMarker
                    :isClimbingStaffMember = this.isClimbingStaffMember

                    :filteredRoutes = this.filteredRoutes

                    :gradeRangeChoices = this.gradeRangeChoices
                    :holdColourChoices = this.holdColourChoices

                    :routesToAddToDatabase = this.routesToAddToDatabase
                    :routesToDeleteFromDatabase = this.routesToDeleteFromDatabase
                    @staffAddNewRoute="staffAddNewRoute"
                    @staffEditRoute="staffEditRoute"

                    :routesClimbedByUserInDatabase = this.routesClimbedByUserInDatabase
                    :routesClimbedByUserInSession = this.routesClimbedByUserInSession
                    @customerEditRoute="customerEditRoute"
                />
            </div>
            <form class="mainPageForm"> 
                <!-- -----------------------FILTERS------------------------------------------------- -->
                <div class="mainPageFormSection">
                    <div v-if="!RouteGradeRangeSelected && !RouteHoldColourSelected"class="applyFilters"> Apply filters to see routes on the map</div>
                    <div class="filterSubsection">
                        <div class="filterSubsectionHeader">Grade:</div>
                        <SelectOption
                            :optionChoices=gradeRangeChoices
                            selectedOptionType="gradeRangeChoicesMainPage"
                            @selectedOptionEmitted="(option)=> RouteGradeRangeSelected = option"
                        ></SelectOption>
                    </div>
                    <div class="filterSubsection">
                        <div class="filterSubsectionHeader">Hold Colour:</div>
                        <SelectOption
                            :optionChoices=holdColourChoices
                            selectedOptionType="holdColourChoicesMainPage"
                            @selectedOptionEmitted="(option)=> RouteHoldColourSelected = option"
                        ></SelectOption>
                    </div>
                </div>
                <!-- -------------------------------------------------------------------------- -->
                 <!-- -----------------------------------------STAFF-------------------------- -->
                <div v-if="isClimbingStaffMember" class="mainPageFormSection">
                    <div class="mainPageFormMiddleSection">
                        <div>
                            Routes <span class="fw-bold">added</span> by you just now:
                            <div v-show="this.routesToAddToDatabase.length > 0" class="editRoutesSectionList">
                                <div class="list-group overflow-scroll" v-for="route in this.routesToAddToDatabase" :key="route.RouteId">
                                    <div @click="FilterRoutes(route)" class="list-group-item" :class="route.RouteColour"> 
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
                                <div class="list-group overflow-scroll" v-for="route in this.routesToDeleteFromDatabase" :key="route.RouteId">
                                    <div @click="FilterRoutes(route)" class="list-group-item" :class="route.RouteColour"> 
                                        <div><span class="fw-bold">{{ route.RouteColour }}</span></div>
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
                <!-- -------------------------------------------------------------------------- -->
                 <!-- -------------------------------CUSTOMER--------------------------------- -->
                  <div v-if="!isClimbingStaffMember" class="mainPageFormSection">
                    <div class="mainPageFormMiddleSection">
                        <div v-show="this.routesClimbedByUserInSession.length > 0">
                            <div>Routes climbed By You this session:</div>
                            <div class="editRoutesSectionList">
                                <div class="list-group overflow-scroll" v-for="route in this.routesClimbedByUserInSession" :key="route.RouteId">
                                    <div @click="FilterRoutes(route)" class="list-group-item" :class="route.RouteColour"> 
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
                            <div class="list-group overflow-scroll" v-for="route in this.routesClimbedByUserInDatabase" :key="route.RouteId">
                                <div @click="FilterRoutes(route)" class="list-group-item" :class="route.RouteColour"> 
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
                  <!-- -------------------------------------------------------------------------- -->
                   <!-- -----------------------------LIST OF ROUTES---------------------------------- -->
                <div class="mainPageFormSection listOfRoutesSection" >
                    <div class="listOfRoutesHeader">List of Routes in the Database: </div>
                    <div class="listOfRoutes">
                        <div class="list-group overflow-scroll" v-for="route in this.allRoutes" :key="route.RouteId">
                            <div @click="FilterRoutes(route)" class="list-group-item" :class="route.RouteColour"> 
                                <div> {{ route.RouteColour }}</div>
                                <div> {{ route.RouteGradeRange }}</div>
                                <div> <span class="fw-bold">Created On: </span> {{ route.RouteCreatedAt }}</div>
                                <div> <span class="fw-bold">Location: </span> {{ route.RouteLocationXAxis }}, {{ route.RouteLocationYAxis }}</div>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- -------------------------------------------------------------------------- -->
            </form>
        </div>
        <!-- ----------------------------------------------------------------------- -->
    </div>
</template>
<style scoped>
.logoutButton {
    font-size: 3.5vw;
    background-color: white;
    color: black;
    border: 1px solid black;
    position: absolute;
    right: 0;
}
.logoutButton:hover:enabled {
    background-color: #802f2f;
}
/* ---------------------- Main Page------------------ */
.mainPage {
    padding: 10% 10% 10% 10%;
    line-height: 1;
    border-radius: 5px;
    color: white;
    font-size: 1rem;
    display: grid;
}
.mainPageForm {
    padding: 2%;
    display: flex;
    font-family: "Montserrat", Sans-serif;
    max-width: 100%;
}
.mainPageFormSection {
    flex: 1;
}
@media only screen and (max-width: 600px) {
    .mainPageForm {
        display: flex;
        flex-direction: column;
        padding: 5%;
    }
}
.mainPageHeaderSection {
    display: flex;
    justify-content: space-between;
    background: rgba(0, 0, 0, 1);
    padding: 5%;
}
.mainPageUsernameHeaderSection{
    display: flex;
    flex-direction: column;
    max-width: 70%;
}
.mainPageUsername {
    font-size: 7vw;
    word-wrap: anywhere;
}
.mainPageHeader {
    font-size: 3.5vw;
}
/* ---------------------- Save Button------------------ */
.saveChanges{
    font-size: 3.5vw;
    background-color: #E9704B;
    color: black;
    border: 1px solid black;
    border-radius: 5px;
    justify-self: center;
    margin: 5px;
    padding: 10px;
} 
.saveChanges:hover {
    background-color: #994931;
    cursor: pointer; 
}
/* ---------------------------------------- */
/* ---------------------------------------- */
.addRoute {
    font-family: "Montserrat", Sans-serif;
    font-weight: bold;
    background-color: #E13B3B;
    color: white;
    padding: 5px;
    max-width: fit-content;
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
.selectForm {
    flex: 1 1;
    padding: 2%;
    border-width: 3px;
    border-radius: 5px;
    border-color: #E9704B;
    margin: 5px;
    font-weight: bold;
}
.selectForm:hover {
     cursor: pointer; 
}
.mainPageFormMiddleSection {
    padding: 5%;
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
    border-radius: 0;
    border-width: 1px;
    border-color: black;
    border-style: solid;
}

/* --------------------------------------------- */
.list-group-item.IrnBru {
    background: linear-gradient(
        to bottom left, 
        rgb(231, 142, 9) 0%,
        rgb(231, 142, 9) 50%,
        rgb(22, 39, 169) 50%, 
        rgb(22, 39, 169) 100%);
    background-color:rgb(113, 77, 22);
    color: white
}
.list-group-item.Flamingo {
    background-color: rgb(169, 51, 149);
}
.list-group-item.Wasp {
    background: linear-gradient(
        to bottom left, 
        rgb(164, 170, 1) 0%,
        rgb(164, 170, 1) 50%,
        rgb(0, 0, 0) 50%, 
        rgb(0, 0, 0) 100%);
    background-color: rgb(150, 145, 46);
    color: white
}
.list-group-item.Mint {
    background-color: rgb(39, 160, 204);
}
.list-group-item.Green {
    background-color: rgb(68, 153, 76);
}
.list-group-item.Orange {
    background-color: rgb(193, 118, 14);
}
.list-group-item.Purple {
    background-color: rgb(98, 68, 153);
}
.list-group-item.Red{
    background-color: rgb(171, 58, 58);
}
.list-group-item.Gryffindor {
    background: linear-gradient(
        to bottom left, 
        rgb(231, 142, 9) 0%,
        rgb(231, 142, 9) 50%,
        rgb(218, 63, 76) 50%, 
        rgb(218, 63, 76) 100%);
    background-color: rgb(231, 142, 9);
}
.list-group-item.Pink{
    background-color: rgb(212, 99, 178);
}
.list-group-item.White{
    background-color: rgb(255, 255, 255);
    color: black;
}
.list-group-item.Black {
    background-color: rgb(20, 20, 20);
    color: white;
}
.list-group-item.Blue {
    background-color: rgb(77, 115, 174);
}
.list-group-item.Yellow {
    background-color: rgb(222, 210, 76);
}
.list-group-item.Grey {
    background-color: rgb(83, 83, 83);
}
.list-group-item.Dalmatians {
    background-color: rgb(173, 173, 173);
}
.list-group-item.Blobs {
    background-color: rgb(117, 121, 117);
}
/* ------------------------------------------- */
.list-group-item.list-group-item:hover {
     cursor: pointer; 
}
</style>
