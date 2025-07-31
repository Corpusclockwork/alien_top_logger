<script>
export default {
    name: 'RouteList',
    props:{
        routeList: Array,
        holdColourChoices: Array, 
        gradeRangeChoices: Array
    },
    methods:{
        getLabel(value, choices){
            const pair = choices?.find((choice) => value === choice[0]);
            return pair ? pair[1]: "" ;
        },
        clickedRoute(route) {
            this.$emit("filterRoutes", route);
        }
    }
}
</script>
<template>
<div class="list-group overflow-scroll" v-for="route in routeList" :key="route.RouteId">
    <div @click="clickedRoute(route)" class="listGroupItem" :class="route.RouteColour"> 
        <div><span>{{ getLabel(route.RouteColour, holdColourChoices) }}</span></div>
        <div>{{ getLabel(route.RouteGradeRange, gradeRangeChoices) }}</div>
        <div><span class="fw-bold">Location: </span> {{ route.RouteLocationXAxis }}, {{ route.RouteLocationYAxis }}</div>
        <div><span class="fw-bold">Created On: </span> {{ route.RouteCreatedAt }}</div>
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
</style>