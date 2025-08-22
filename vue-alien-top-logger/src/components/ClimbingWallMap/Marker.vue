<script>
export default {
    name: 'Marker',
    props: {
        id: Number,
        x_percentage: Number,
        y_percentage: Number,
        hold_colour: String,
        climbedByUserInSession: Boolean,
        climbedByUserInDatabase: Boolean
    },
    methods: {
        getXPercentage() {
            return (this.x_percentage-2) + '%';
        },
        getYPercentage() {
            return (this.y_percentage-2) + '%';
        },
        getOpacity(){
            return (this.climbedByUserInSession || this.climbedByUserInDatabase) ? '0.6' : '1';
        }
    },
    computed: {
        cssProps() {
            return {
                'top': this.getYPercentage(),
                'left': this.getXPercentage(),
                'opacity': this.getOpacity(),
            }
        }
    }
}
</script>
<template>
    <div 
        :class="hold_colour"
        class="markerCircle"
        :style="cssProps" 
        @click="$emit('markerSelected')"
        :title="'Location: ' + x_percentage +' , ' + y_percentage"
    >
    <div v-if="climbedByUserInSession || climbedByUserInDatabase" class="tickCharacter">
        &#x2713
    </div>
    </div>
</template>
<style>
.markerCircle{
    width: 3.5vw;
    height: 3.5vw;
    border-width: 0.3vw;
    border-radius: 50%;
    position: absolute;
    cursor: pointer;
    border-color: black;
    border-style: solid;
    justify-content: center;
    align-items: center;
}
.tickCharacter{
    font-size: 2.5vw;
    font-weight: bold;
}

@media only screen and (max-width: 600px) {
    .markerCircle {
        width: 6vw;
        height: 6vw;
        border-width: 0.5vw;
    }
    .tickCharacter{
        font-size: 5vw;
        font-weight: bold;
    }
}
</style>