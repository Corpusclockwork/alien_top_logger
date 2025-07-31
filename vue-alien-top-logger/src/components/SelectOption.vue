<script>
export default {
    name: 'SelectOption',
    data: function () {
        return {
            selectedOption: '',
            
        }
    },
    props:{
        optionChoices: Array,
        selectedOptionType: String
    },
    methods:{
        displayNewUserPage(){
            this.$emit("toggleLoginPages");
        }
    },
    watch:{
        selectedOption() {
            this.$emit("selectedOptionEmitted", this.selectedOption);
        }
    }
}
</script>
<template>
<select class="selectOption" :class="selectedOption" :id="selectedOptionType" v-model="selectedOption">
    <option value="" selected>Not specified</option>
    <option :class=choice[0] v-for="choice in optionChoices" :value=choice[0] :key="choice[0]">
        {{choice[1]}}
    </option>
</select>
</template>
<style scoped>
.selectOption {
    flex: 1 1;
    padding: 2%;
    border-width: 3px;
    border-radius: 5px;
    border-color: #E9704B;
    margin: 5px;
    font-weight: bold;
}
.selectOption:hover {
     cursor: pointer; 
}
/* ---------------------------------------------- */
.IrnBru {
    background: linear-gradient(
        to bottom left, 
        rgb(231, 142, 9) 0%,
        rgb(231, 142, 9) 50%,
        rgb(22, 39, 169) 50%, 
        rgb(22, 39, 169) 100%);
    background-color:rgb(113, 77, 22);
    color: white
}
.Flamingo {
    background-color: rgb(169, 51, 149);
}
.Wasp {
    background: linear-gradient(
        to bottom left, 
        rgb(164, 170, 1) 0%,
        rgb(164, 170, 1) 50%,
        rgb(0, 0, 0) 50%, 
        rgb(0, 0, 0) 100%);
    background-color: rgb(150, 145, 46);
    color: white
}
.Mint {
    background-color: rgb(39, 160, 204);
}
.Green {
    background-color: rgb(68, 153, 76);
}
.Orange {
    background-color: rgb(193, 118, 14);
}
.Purple {
    background-color: rgb(98, 68, 153);
}
.Red{
    background-color: rgb(171, 58, 58);
}
.Gryffindor {
    background: linear-gradient(
        to bottom left, 
        rgb(231, 142, 9) 0%,
        rgb(231, 142, 9) 50%,
        rgb(218, 63, 76) 50%, 
        rgb(218, 63, 76) 100%);
    background-color: rgb(231, 142, 9);
}
.Pink{
    background-color: rgb(212, 99, 178);
}
.White{
    background-color: rgb(255, 255, 255);
    color: black;
}
.Black {
    background-color: rgb(20, 20, 20);
    color: white;
}
.Blue {
    background-color: rgb(77, 115, 174);
}
.Yellow {
    background-color: rgb(222, 210, 76);
}
.Grey {
    background-color: rgb(83, 83, 83);
}
.Dalmatians {
    background-color: rgb(173, 173, 173);
}
.Blobs {
    background-color: rgb(117, 121, 117);
}
/* ------------------------------------------ */
.VB {
    background-color: rgb(240, 144, 0);
}
.V0_V2 {
    background-color: rgb(243, 239, 17);
    color: black;
}
.V1_V3 {
    background-color: rgb(120, 236, 110);
    color: black;
}
.V2_V4 {
    background-color: rgb(14, 158, 201);
    color: black;
}
.V3_V5 {
    background-color: rgb(173, 62, 201);
}
.V4_V6 {
    background-color: rgb(205, 22, 31);
}
.V5_V7 {
    background-color: rgb(0, 0, 0);
    color: white;
}
.V7plus {
    background-color: rgb(255, 255, 255);
    color: black;
}
.OffCircuit {
    background-color: rgb(138, 138, 138);
}
.Comp {
    background-color: rgb(243, 145, 235);
    color: black;
}
</style>