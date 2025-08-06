<script>

import SelectOption from '../SelectOption.vue';

export default {
    name: "AddRouteModal",
    data: function(){
        return {
            newRouteHoldColour: null,
            newRouteGradeRange: null,
            newRouteObject: new Object,
            okDisabled: true
        }
    },
    components:{
        SelectOption
    },
    props: {
        gradeRangeChoices: Array, 
        holdColourChoices: Array,
        markerX: Number,
        markerY: Number
    },
    watch: {
        newRouteHoldColour() {
            this.newRouteObject.hold_colour = this.newRouteHoldColour;
        },
        newRouteGradeRange() {
            this.newRouteObject.grade_range = this.newRouteGradeRange;
        }
    }
}
</script>
<template>
<div
    class="modal fade"
    tabindex="-1" 
    aria-labelledby="AddRouteModal"
    id="add-route"
    aria-hidden="true"
>
    <div class="modal-dialog modal-dialog-centered" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">Add Route</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close">
                </button>
            </div>
            <div class="modal-body">
                <form>
                    <div class="form-row" >
                        <div class="col">
                            <p> <span class="fw-bold">Route Location: </span>{{markerX}}, {{markerY}}</p>
                        </div>
                    </div>
                    <div class="form-row">
                         <div class="col">
                            <div class="modalFormSelectHeader"> Hold Colour:</div>
                               <SelectOption
                                    :optionChoices=holdColourChoices
                                    selectedOptionType="holdColourChoicesAddRouteModal"
                                    @selectedOptionEmitted="(option)=> newRouteHoldColour = option"
                                ></SelectOption>
                            <div v-if="newRouteHoldColour === null" class="invalid-feedback d-block">Please select a Hold Colour</div>
                        </div>
                        <div class="col">
                            <div class="modalFormSelectHeader"> Route Grade:</div>
                             <SelectOption
                                :optionChoices=gradeRangeChoices
                                selectedOptionType="gradeRangeChoicesAddRouteModal"
                                @selectedOptionEmitted="(option)=> newRouteGradeRange = option"
                            ></SelectOption>
                            <div v-if="newRouteGradeRange === null" class="invalid-feedback d-block">Please select a Grade</div>
                        </div>
                    </div>
                </form>
            </div>
            <div class="modal-footer">
                <button type="button" class="climbingAppButton" data-bs-dismiss="modal">Close</button>
                <button type="button" class="climbingAppButton" data-bs-dismiss="modal" @click="$emit('on-ok', newRouteObject);" :disabled="(newRouteHoldColour === null) || (newRouteGradeRange === null)" >Add Route</button>
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
.modalFormSelect:hover {
    cursor: pointer; 
}
</style>