<script>
export default {
    name: 'Login',
    data: function () {
        return {
            username: '',
            password: '',
            isClimbingStaffMember: false,
        }
    },
    methods:{
        displayNewUserPage(){
            this.$emit("toggleLoginPages");
        }
    }
}
</script>
<template>
    <div class="loginPage">
        <div class="loginPageHeader">
            Login:
        </div>
        <div class="flex items-center gap-4 mb-2">
            <label for="username" class="loginPageSectionHeader font-semibold w-24">Username</label>
            <input v-model="username" type="username" class="loginPageSectionText form-control" id="usernameinput" aria-describedby="userHelp" placeholder="Enter username">
        </div>
        <div class="flex items-center gap-4 mb-2">
            <label for="password" class="loginPageSectionHeader font-semibold w-24">Password</label>
            <input v-model="password" type="password" class="loginPageSectionText form-control" id="passwordinput" aria-describedby="passwordHelp" placeholder="Enter password">
        </div>
        <div class="loginPageButtonContainer">
            <button @click="$emit('loginUser', {username, password})" type="button" class="loginPageButton" :disabled="username === '' || password === ''">Login</button>
            <button @click="displayNewUserPage()" type="button" class="loginPageButton">Create a New User</button>
        </div>
    </div>
</template>
<style>
.loginPage {
    padding: 10%;
    line-height: 1;
    border-radius: 5px;
    color: white;
    font-size: 4rem;
    display: grid;
}

.loginPageSectionHeader {
    font-size: 2rem;
}

.loginPageSectionText {
    font-family: "Montserrat", Sans-serif;
}

.loginPageButtonContainer {
    display: flex;
    flex-direction: column;
    justify-self: center;
}

.loginPageButton {
    font-size: 1.5rem;
    background-color: #E9704B;
    color: white;
    border-color: #E9704B;
    justify-self: center;
    border-radius: 15px;
    margin: 5px;
    padding: 10px;
}

.loginPageButton:disabled {
    background-color: grey;
}

.loginPageButton:hover:enabled {
    background-color: #994931;
}
</style>