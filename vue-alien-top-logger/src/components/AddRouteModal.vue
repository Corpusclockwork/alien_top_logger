<script>
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
    props: {
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
    role="dialog"
    id="add-route"
>
    <div class="modal-dialog modal-dialog-centered" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">Add Route</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="modal-body">
                <form>
                    <div class="form-row" >
                        <div class="col">
                            <p class="font-weight-bold"> Route Location: {{markerX}}, {{markerY}} </p>
                        </div>
                    </div>
                    <div class="form-row">
                        <div class="col">
                            <div> Route Grade : {{ newRouteGradeRange }}</div>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" id="V0-V2" value="V0-V2" v-model="newRouteGradeRange" required/>
                                <label class="form-check-label" for="V0-V2">V0-V2</label>
                            </div>

                            <div class="form-check">
                                <input class="form-check-input" type="radio" id="V1-V3" value="V1-V3" v-model="newRouteGradeRange" required/>
                                <label class="form-check-label" for="V1-V3">V1-V3</label>
                            </div>

                            <div class="form-check">
                                <input class="form-check-input" type="radio" id="V2-V4" value="V2-V4" v-model="newRouteGradeRange" required/>
                                <label class="form-check-label" for="V2-V4">V2-V4</label>
                            </div>
                            <div v-if="this.newRouteGradeRange === null" class="invalid-feedback d-block">Please select a Grade</div>
                            
                        </div>

                        <div class="col">
                            <div> Hold Colour : {{ newRouteHoldColour }}</div>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" id="RED" value="RED" v-model="newRouteHoldColour" required/>
                                <label class="form-check-label" for="RED">RED</label>
                            </div>

                            <div class="form-check">
                                <input class="form-check-input" type="radio" id="GREEN" value="GREEN" v-model="newRouteHoldColour" required/>
                                <label class="form-check-label" for="GREEN">GREEN</label>
                            </div>

                            <div class="form-check">
                                <input class="form-check-input" type="radio" id="BLUE" value="BLUE" v-model="newRouteHoldColour" required/>
                                <label class="form-check-label" for="BLUE">BLUE</label>
                            </div>
                            <div v-if="this.newRouteHoldColour === null" class="invalid-feedback d-block">Please select a Hold Colour</div>
                        </div>
                    </div>
                </form>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary" data-dismiss="modal" @click="$emit('on-ok', newRouteObject);" :disabled="(this.newRouteHoldColour === null) || (this.newRouteGradeRange === null)" >Save Route</button>
            </div>
        </div>
    </div>
</div>
</template>