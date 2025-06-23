<script>
import Marker from './Marker.vue';
export default {
    name: "EditRouteModal",
    data: function(){
        return {
            destroyRoute: false,
            climbedByUserLocal: undefined,
            hasBeenSavedLocal: undefined
        }
    },
    props: {
        marker: Marker,
        hasBeenSaved: Boolean,
        climbedByUser: Boolean
    },
    mounted() {
        this.climbedByUserLocal = this.climbedByUser;
        this.hasBeenSavedLocal = this.hasBeenSaved;
    },
    watch: {
      
    },
    methods: {
     
    }
}
</script>
<template>
    <BModal
        id="edit-route"
        :visible="true"
        title="Edit Route"
        @ok="$emit('on-ok', {DestroyRoute, HasBeenSaved, ClimbedByUser})"
        @cancel="$emit('on-cancel')"
        @close="$emit('on-cancel')"
    >
        <!-- BOTH 
            location x
            location y
            created at 
        -->

         <!-- CUSTOMER
            add to list of climbed by user routes ? 
        -->

         <!-- STAFF
            sent to db yes/no
            destroy route ?
        -->

        <form>
            <BFormGroup>
                <BFormCheckbox
                    id="add-marker"
                    v-model="climbedByUserLocal" 
                    switch
                >
                    Sent By User?
                </BFormCheckbox>
                <BFormCheckbox
                    id="saved-route"
                    v-model="hasBeenSavedLocal" 
                    :switch=true
                >
                    Saved in the Database ?
                </BFormCheckbox>
                <BFormCheckbox switch
                    id="destroy-route"
                    v-model="destroyRoute" 
                    
                >
                    Destroy selected Route ?
                </BFormCheckbox>
            </BFormGroup>
            <div>LOCATION
                <div> {{marker.RouteLocationX}} </div>
                <div> {{marker.RouteLocationX}} </div>
            </div>
        </form>
    </BModal>

</template>
<style>

</style>