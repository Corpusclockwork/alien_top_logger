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
    mounted() {
        console.log("hello");
        this.climbedByUserLocal = this.climbedByUser;
        this.destroyRouteLocal = this.destroyRoute;
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
    role="dialog"
    id="edit-route"
>
    <div class="modal-dialog modal-dialog-centered" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <h5 v-if="isStaffUser" class="modal-title">Destroy Route</h5>
                <h5 v-if="!isStaffUser" class="modal-title">Track Route</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="modal-body">
                <form>
                    <div class="form-row" >
                        <p class="font-weight-bold"> Route Grade Range: {{marker.grade}} </p>
                    </div>
                    <div class="form-row" >
                        <p class="font-weight-bold"> Route Grade Hold Colour: {{marker.colour}} </p>
                    </div>
                    <div class="form-row" >
                        <p class="font-weight-bold"> Route Location: {{marker.x}}, {{marker.y}} </p>
                    </div>
                    <div class="form-row" >
                        <p class="font-weight-bold"> Route Id: {{marker.id}} </p>
                    </div>
                    <div v-if="isStaffUser">
                        <div class="custom-control custom-switch">
                            <input class="custom-control-input" type="checkbox" role="switch" id="destroyRoute" v-model="destroyRouteLocal" />
                            <label class="custom-control-label" for="destroyRoute">Destroy selected Route ?</label>
                        </div>
                        <div v-if="marker.id < 0">A negative route id means that the route hasn't been saved in the database yet</div>
                    </div>
                    <div v-if="!isStaffUser">
                        <div class="custom-control custom-switch">
                            <input class="custom-control-input" type="checkbox" role="switch" id="climbedByUserLocal" v-model="climbedByUserLocal" />
                            <label class="custom-control-label" for="climbedByUserLocal">Climbed by you ?</label>
                        </div>
                    </div>
                </form>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary" data-dismiss="modal" @click="$emit('on-ok', {climbedByUserLocal, destroyRouteLocal});" >Save Route</button>
            </div>
        </div>
    </div>
</div>
</template>
<style>

</style>