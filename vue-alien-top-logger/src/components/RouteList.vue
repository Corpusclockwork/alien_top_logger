<script>
export default {
    name: 'RouteList',
    props:{
        routeList: Array,
        holdColourChoices: Array, 
        gradeRangeChoices: Array,

        deletedRoutes: Array,

        climbedByUserInDatabase: Array,
        climbedByUserInSession: Array
    },
    methods:{
        getLabel(value, choices){
            const pair = choices?.find((choice) => value === choice[0]);
            return pair ? pair[1]: "" ;
        },
        clickedRoute(route) {
            this.$emit("filterRoutes", route);
        },
        deletedRoutesClass(route){
            if (this.deletedRoutes?.find(deletedRoute => deletedRoute?.RouteId === route.RouteId)) {
                return "routeDeleted"
            } 
            return "";
        },
        routeClimbedByUserInDatabase(route){
            if (this.climbedByUserInDatabase?.find(climbedRoute => climbedRoute?.RouteId === route.RouteId)) {
                return true
            } 
            return "";
        },
        routeClimbedByUserInSession(route){
            if (this.climbedByUserInSession?.find(climbedRoute => climbedRoute?.RouteId === route.RouteId)) {
                return true
            } 
            return "";
        }
    }
}
</script>
<template>
<div class="list-group overflow-scroll" v-for="route in routeList" :key="route.RouteId">
    <div @click="clickedRoute(route)" class="listGroupItem" :class="route.RouteColour, deletedRoutesClass(route)"> 
        <div v-if="routeClimbedByUserInDatabase(route)" class="routeClimbed"> &#10004 </div>
        <div v-if="routeClimbedByUserInSession(route)" class="routeClimbed">&#9745</div>
        <div><span>{{ getLabel(route.RouteColour, holdColourChoices) }}</span></div>
        <div>{{ getLabel(route.RouteGradeRange, gradeRangeChoices) }}</div>
        <div v-if="route.RouteCreatedAt"><span class="fw-bold">Created: </span> {{ new Date(route.RouteCreatedAt).toLocaleDateString("en-UK") }}</div>
    </div>
</div>
</template>
<style scoped>
.listGroupItem {
    border-radius: 0;
    border-width: 1px;
    border-color: black;
    border-style: solid;
    position: relative;
    display: block;
    padding: 10px;
}
.listGroupItem:hover {
     cursor: pointer; 
}
.routeDeleted {
    opacity: 0.6;
    text-decoration: line-through;
}
.routeClimbed {
    position: absolute;
    right: 10%;
    font-weight: bold;
}
</style>