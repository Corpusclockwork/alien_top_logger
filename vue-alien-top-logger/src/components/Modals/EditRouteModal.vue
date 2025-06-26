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
        climbedByUser: Boolean,
        destroyRoute: Boolean,
        isStaffUser: Boolean
    },
    watch: {
        marker(){
            this.climbedByUserLocal = this.climbedByUser;
            this.destroyRouteLocal = this.destroyRoute;
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
                <h5 v-if="isStaffUser" class="modalFormSelectHeader modal-title">Destroy Route</h5>
                <h5 v-if="!isStaffUser" class="modalFormSelectHeader modal-title">Track Route</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close">
                </button>
            </div>
            <div class="modal-body col">
                <form>
                    <div class="form-row" >
                        <p> <span class="fw-bold">Route Grade Range: </span> {{marker?.grade}} </p>
                    </div>
                    <div class="form-row" >
                        <p> <span class="fw-bold">Route Grade Hold Colour: </span> {{marker?.colour}} </p>
                    </div>
                    <div class="form-row" >
                        <p> <span class="fw-bold">Route Location: </span> {{marker?.x}}, {{marker?.y}} </p>
                    </div>
                    <div class="form-row" >
                        <p> <span class="fw-bold"> Route Id: </span> {{marker?.id}} </p>
                    </div>
                    <div v-if="isStaffUser">
                        <div class="custom-control custom-switch">
                            <input class=" editCheckbox custom-control-input" type="checkbox" role="switch" id="destroyRoute" v-model="destroyRouteLocal" />
                            <label class="custom-control-label" for="destroyRoute">Destroy selected Route ?</label>
                        </div>
                        <div class="negativeIdWarning" v-if="marker?.id < 0">A negative route id means that the route hasn't been saved in the database yet</div>
                    </div>
                    <div v-if="!isStaffUser">
                        <div class="custom-control custom-switch">
                            <input class="editCheckbox custom-control-input" type="checkbox" role="switch" id="climbedByUserLocal" v-model="climbedByUserLocal" />
                            <label class="custom-control-label" for="climbedByUserLocal">Climbed by you ?</label>
                        </div>
                    </div>
                </form>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="button" class="saveButton btn btn-primary" data-bs-dismiss="modal" @click="$emit('on-ok', {climbedByUserLocal, destroyRouteLocal});" >Save Route</button>
            </div>
        </div>
    </div>
</div>
</template>
<style>
.modal-body {
    font-family: "Montserrat", Sans-serif;
}

.modal-title {
    font-size: 1.5em;
}

.saveButton {
    background-color: #E9704B;
    border-color: #E9704B;
}

.saveButton:disabled {
    background-color: grey;
}

.saveButton:hover {
    background-color: #994931;
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
 
</style>