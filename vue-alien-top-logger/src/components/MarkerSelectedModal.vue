<script>
import { BFormCheckbox } from 'bootstrap-vue-next';
import Marker from './Marker.vue';
export default {
    name: "MarkerSelectedModal",
    data: function(){
        return {
            DestroyRoute: false,
            HasBeenSaved: true,
            ClimbedByUser: null
        }
    },
    props: {
        marker: Marker,
    },
    watch: {
      
    },
    methods: {
     
    }
}
</script>
<template>
    <BModal
        id="selected-marker"
        :visible="true"
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
            <BFormGroup
                label="Sent By User?"
            >
                <BFormCheckbox
                    id="add-marker"
                    v-model="ClimbedByUser"
                ></BFormCheckbox>
            </BFormGroup>
            <BFormGroup
                label="Saved in the Database ?"
            >
                <BFormCheckbox
                    id="saved-route"
                    v-model="HasBeenSaved"
                ></BFormCheckbox>
            </BFormGroup>
            <BFormGroup
                label="DestroyRoute ?"
            >
                <BFormCheckbox
                    id="destror-route"
                    v-model="DestroyRoute"
                ></BFormCheckbox>
            </BFormGroup>
            <div>LOCATION
                <div> {{marker.RouteLocationX}} </div>
                <div> {{marker.RouteLocationX}} </div>
            </div>
        </form>
    </BModal>

</template>