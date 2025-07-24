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
                            <div class="modalFormSelectHeader"> Route Grade:</div>
                             <select class="modalFormSelect form-select" id="newRouteGradeRange" v-model="newRouteGradeRange" required>
                                <option  value='V0-V2'>V0-V2</option>
                                <option value="V1-V3">V1-V3</option>
                                <option value="V2-V4">V2-V4</option>
                            </select>
                            <div v-if="this.newRouteGradeRange === null" class="invalid-feedback d-block">Please select a Grade</div>
                        </div>
                        <div class="col">
                            <div class="modalFormSelectHeader"> Hold Colour:</div>
                            <select class="modalFormSelect form-select" id="newRouteHoldColour" v-model="newRouteHoldColour" required>
                                <option value="RED">RED</option>
                                <option value="BLUE">BLUE</option>
                                <option value="GREEN">GREEN</option>
                            </select>
                            <div v-if="this.newRouteHoldColour === null" class="invalid-feedback d-block">Please select a Hold Colour</div>
                        </div>
                    </div>
                </form>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="button" class="saveButton btn btn-primary" data-bs-dismiss="modal" @click="$emit('on-ok', newRouteObject);" :disabled="(this.newRouteHoldColour === null) || (this.newRouteGradeRange === null)" >Save Route</button>
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

.modalFormSelect:hover {
    cursor: pointer; 
}
</style>