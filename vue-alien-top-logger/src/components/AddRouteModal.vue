<script>
export default {
    name: "AddRouteModal",
    data: function(){
        return {
            NewRouteHoldColour: null,
            NewRouteGradeRange: null,
            gradeOptions: [
                { value: null, text: 'Please select an option' },
                { value: 'V0-V2', text: 'V0-V2' },
                { value: 'V1-V3', text: 'V1-V3' },
                { value: 'V2-V4', text: 'V2-V4' }
            ],
            holdColourOptions: [
                { value: null, text: 'Please select an option' },
                { value: 'RED', text: 'RED' },
                { value: 'GREEN', text: 'GREEN' },
                { value: 'BLUE', text: 'BLUE' }
            ],
            newRouteObject: new Object,
            okDisabled: true
        }
    },
    props: {
        markerX: Number,
        markerY: Number
    },
    watch: {
        NewRouteHoldColour() {
            this.newRouteObject.hold_colour = this.NewRouteHoldColour;
        },
        NewRouteGradeRange() {
            this.newRouteObject.grade_range = this.NewRouteGradeRange;
        }
    },
    methods: {
        checkGradeValidity(){
            this.okDisabled = (this.NewRouteHoldColour == null) || (this.NewRouteGradeRange == null);
            return this.NewRouteGradeRange != null;
        },
        holdColourValidity(){
            this.okDisabled = (this.NewRouteHoldColour == null) || (this.NewRouteGradeRange == null);
            return this.NewRouteHoldColour != null;
        }
    }
}
</script>
<template>
    <BModal 
        @ok="$emit('on-ok', newRouteObject)"
        @cancel="$emit('on-cancel')"
        id="add-marker"
        :visible="true"
        :ok-disabled="okDisabled"
    > 
        <form ref="form" @submit.stop.prevent="handleSubmit">
            <BFormGroup
                label="Grade"
                label-for="grade-input"
                invalid-feedback="Grade is required"
                :state="checkGradeValidity()"
            >
                <BFormSelect
                    id="grade-input"
                    v-model="NewRouteGradeRange"
                    :options="gradeOptions"
                    required
                ></BFormSelect>
            </BFormGroup>
            <BFormGroup
                label="Hold Colour"
                label-for="hold-colour-input"
                invalid-feedback="Hold Colour is required"
                :state="holdColourValidity()"
            >
                <BFormSelect
                    id="hold-colour-input"
                    v-model="NewRouteHoldColour"
                    :options="holdColourOptions"
                    required
                ></BFormSelect>
            </BFormGroup>
            <div>LOCATION
                <div> {{markerX}} </div>
                <div> {{markerY}} </div>
            </div>
        </form>
    </BModal>
</template>