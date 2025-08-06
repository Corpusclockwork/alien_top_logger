<script>
import Marker from '../ClimbingWallMap/Marker.vue';
export default {
    name: "EditRouteModal",
    data: function(){
        return {
            destroyRouteLocal: false,
            climbedByUserLocal: undefined,
        }
    },
    components: {
        Marker
    },
    props: {
        marker: Marker,

        gradeRangeChoices: Array, 
        holdColourChoices: Array,

        selectedRouteClimbedByUserInSession: Boolean,
        selectedRouteClimbedByUserInDatabase: Boolean,

        selectedRouteDestroyedByUser: Boolean,

        isClimbingStaffMember: Boolean
    },
    methods: {
        getLabel(value, choices){
            const pair = choices?.find((choice) => value === choice[0]);
            return pair ? pair[1]: "" ;
        }
    },
    watch: {
        marker(){
            this.climbedByUserLocal = this.selectedRouteClimbedByUserInSession;
            this.destroyRouteLocal = this.selectedRouteDestroyedByUser;
        }
    }
}
</script>
<template>
<div
    class="modal fade"
    tabindex="-1" 
    aria-labelledby="EditRouteModal"
    id="edit-route"
    aria-hidden="true"
>
    <div class="modal-dialog modal-dialog-centered" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <!-- ------------------------------------STAFF ----------------------------------------->
                <h5 v-if="isClimbingStaffMember" class="modalFormSelectHeader modal-title">Destroy Route</h5>
                <!-- ----------------------------------------------------------------------------->
                 <!-- ------------------------------------CUSTOMER ----------------------------------------->
                <h5 v-if="!isClimbingStaffMember" class="modalFormSelectHeader modal-title">Track Route</h5>
                <!-- ----------------------------------- ----------------------------------------->
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close">
                </button>
            </div>
            <div class="modal-body col">
                <form>
                    <div class="form-row" >
                        <p>
                            <span class="fw-bold">Route Grade Hold Colour: </span>
                            <span class="EditRouteTextContainer" :class="marker?.colour">{{getLabel(marker?.colour, holdColourChoices)}}</span>
                        </p>
                    </div>
                    <div class="form-row" >
                        <p> 
                            <span class="fw-bold" >Route Grade Range: </span>
                            <span class="EditRouteTextContainer" :class="marker?.grade" >{{getLabel(marker?.grade, gradeRangeChoices)}}</span> 
                        </p>
                    </div>
                    <div class="form-row" >
                        <p> <span class="fw-bold">Route Location: </span> {{marker?.x}}, {{marker?.y}} </p>
                    </div>
                    <div class="form-row" >
                        <p> <span class="fw-bold"> Route Id: </span> {{marker?.id}} </p>
                    </div>
                    <!-- ------------------------------------STAFF ----------------------------------------->
                    <div v-if="isClimbingStaffMember">
                        <div class="custom-control custom-switch">
                            <input class=" editCheckbox custom-control-input" type="checkbox" role="switch" id="destroyRoute" v-model="destroyRouteLocal" />
                            <label class="custom-control-label" for="destroyRoute">Delete this Route ?</label>
                        </div>
                        <div class="negativeIdWarning" v-if="marker?.id < 0">A negative route id means that the route hasn't been saved in the database yet</div>
                    </div>
                    <!-- ------------------------------------------------------------------------------------->
                     <!-- ------------------------------------CUSTOMER ----------------------------------------->
                    <div v-if="!isClimbingStaffMember">
                        <div v-if="!selectedRouteClimbedByUserInDatabase" class="custom-control custom-switch">
                            <input class="editCheckbox custom-control-input" type="checkbox" role="switch" id="climbedByUserLocal" v-model="climbedByUserLocal" />
                            <label class="custom-control-label" for="climbedByUserLocal">Has this route been climbed by you ?</label>
                        </div>
                        <div v-if="selectedRouteClimbedByUserInDatabase" class="custom-control custom-switch">
                            Route has already been climbed by you
                        </div>
                    </div>
                    <!-- ------------------------------------------------------------------------------------>
                </form>
            </div>
            <div v-if="!selectedRouteClimbedByUserInDatabase" class="modal-footer">
                <button type="button" class="climbingAppButton" data-bs-dismiss="modal">Close</button>
                <button v-if="isClimbingStaffMember" type="button" class="climbingAppButton" data-bs-dismiss="modal" @click="$emit('on-ok', {destroyRouteLocal});" >Delete Route</button>
                <button v-if="!isClimbingStaffMember" type="button" class="climbingAppButton" data-bs-dismiss="modal" @click="$emit('on-ok', {climbedByUserLocal});" >Save</button>
            </div>
        </div>
    </div>
</div>
</template>
<style scoped>
.modal-body {
    font-family: "Montserrat", Sans-serif;
}
.modal-title {
    font-size: 1.5em;
}
.modalFormSelectHeader {
   margin: 5px;
}
.negativeIdWarning {
    color: #E13B3B;
    font-size: 0.7em;
    margin: 5px;
}
.editCheckbox {
    accent-color: #E13B3B;
    margin: 5px;
}
.editCheckbox:hover{
    cursor: pointer; 
}
.EditRouteTextContainer {
    padding: 4px;
    padding: 4px;
    border-radius: 4px;
    border-style: solid;
    border-color: black;
    border-width: 1px;
}
</style>