<script>
export default {
    name: 'SelectOption',
    data: function () {
        return {
            selectedOption: "",
        }
    },
    props:{
        optionChoices: Array,
        variableToEdit: String,
        selectedOptionType: String,
        clearFilter: Boolean
    },
    watch:{
        selectedOption() {
            this.$emit("selectedOptionEmitted", this.selectedOption);
        },
        variableToEdit(){
            if(this.variableToEdit === ""){
                this.selectedOption = "";
            }
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
</style>