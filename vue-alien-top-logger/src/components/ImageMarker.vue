<script>
import AddRouteModal from './AddRouteModal.vue';
export default {
    name: 'ImageMarker',
    data: function () {
        return {
            markers: []
        }
    },
    props: {
        filteredRoutes: Array
    },
    methods: {
        generateMarkers() {
            // I should go back and make the markers generate while the filters are being changed 
            this.markers = [] ;
            this.filteredRoutes.forEach(route => {
                this.markers.push(
                    {
                        id: route.RouteId, 
                        colour: route.RouteColour, 
                        grade: route.RouteGradeRange, 
                        x: route.RouteLocationXAxis * 0.1,
                        y: route.RouteLocationYAxis * 0.1
                    }
                )
            });
        },
        AddMarker() {
            console.log("open popup")
        }
    },
    watch : {
        filteredRoutes() {
            this.generateMarkers();
        }
    }
}
</script>
<template>
<div> 
    <div class="ImageMarkerContainer">
        <!-- <AddRouteModal
            :new_X=""
            :new_Y=""
        /> -->
            <img
                src="/Alienbloc_shape.png"
                alt= "Alen bloc"
                @click="AddMarker()"
                class="ImageMarkerImageClass"
            />
            <div v-for="marker in this.markers">
                <Marker
                    @click="$emit('selectMarker', marker.id)"
                    :id = marker.id
                    :x_percentage = marker.x
                    :y_percentage = marker.y
                    :hold_colour = marker.colour
                />
            </div>
    </div>
</div>
</template>
<style>
.ImageMarkerContainer {
    width: 100%;
    position: relative;
}
.ImageMarkerImageClass {
    width: 100%;
}
</style>