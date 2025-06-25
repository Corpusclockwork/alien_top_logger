<script>
export default {
    name: 'Marker',
    props: {
        id: Number,
        x_percentage: Number,
        y_percentage: Number,
        hold_colour: String
    },
    methods: {
        getColour(){
            if(this.hold_colour =="RED") {
                return "red";
            } else if(this.hold_colour =="GREEN") {
                return "green";
            } else if (this.hold_colour =="BLUE") {
                return "blue";
            }
        },
        getXPercentage() {
            return this.x_percentage + '%'
        },
        getYPercentage() {
            return this.y_percentage + '%'
        }
    },
    computed: {
        cssProps() {
            return {
                'background-color': this.getColour(),
                'width': '25px',
                'height': '25px',
                'border-radius' : '50%',
                'top': this.getYPercentage(),
                'left': this.getXPercentage(),
                'position': 'absolute',
                'cursor': 'pointer'
            }
        }
    }
}
</script>
<template>
    <div 
        :style="cssProps" 
        @click="$emit('markerSelected')"
    >
    </div>
</template>