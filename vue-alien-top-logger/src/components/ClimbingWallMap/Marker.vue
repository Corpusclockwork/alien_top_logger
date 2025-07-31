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
                'width': '3vw',
                'height': '3vw',
                'border-radius' : '50%',
                'top': this.getYPercentage(),
                'left': this.getXPercentage(),
                'position': 'absolute',
                'cursor': 'pointer',
                'border-color' :'black',
                'border-style' :'solid',
                'border-width' : '2px'
            }
        }
    }
}
</script>
<template>
    <div 
        :class="hold_colour"
        :style="cssProps" 
        @click="$emit('markerSelected')"
    >
    </div>
</template>
<style>
</style>