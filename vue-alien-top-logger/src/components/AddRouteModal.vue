<script>
export default {
    name: "AddRouteModal",
    data: function(){
        return {
            NewRouteHoldColour: null,
            NewRouteGradeRange: null,
            newRouteObject: {}
        }
    },
    props: {
        new_x: Number,
        new_Y: Number
    },
    watch: {
        NewRouteHoldColour() {
            newRouteObject.hold_colour = this.NewRouteHoldColour;
        },
        NewRouteGradeRange() {
            newRouteObject.grade_range = this.NewRouteGradeRange;
        }
    }
}
</script>
<template>
    <div> ADD NEW ROUTE</div>
    <div>
        <div> HOLD COLOUR</div>
        <select id="NewRouteHoldColour" v-model="NewRouteHoldColour">
                        <option value="RED">RED</option>
                        <option value="BLUE">BLUE</option>
                        <option value="GREEN">GREEN</option>
                    </select>
        <div> GRADE RANGE</div>
        <select id="NewRouteGradeRange" v-model="NewRouteGradeRange">
                        <option  value='V0-V2'>V0-V2</option>
                        <option value="V1-V3">V1-V3</option>
                        <option value="V2-V4">V2-V4</option>
                    </select>
        <div>LOCATION
            <div> X </div>
            <div> Y </div>
        </div>
    </div>
    <button 
        :disabled="false" 
        @click="$emit('NewRouteAdded', newRouteObject)"
    >
        CREATE ROUTE
    </button>
</template>