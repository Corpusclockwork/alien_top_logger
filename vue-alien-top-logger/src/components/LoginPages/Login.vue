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
    props:{
        messageToDisplay: String
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
        <div class="incorrectUsernameOrPasswordWarning">{{ messageToDisplay }}</div>
        <div class="flex items-center gap-4 mb-2">
            <label for="username" class="loginPageSectionHeader font-semibold w-24">Username</label>
            <input v-model="username" type="username" class="loginPageSectionText form-control" id="usernameinput" aria-describedby="userHelp" placeholder="Enter username">
        </div>
        <div class="flex items-center gap-4 mb-2">
            <label for="password" class="loginPageSectionHeader font-semibold w-24">Password</label>
            <input v-model="password" type="password" class="loginPageSectionText form-control" id="passwordinput" aria-describedby="passwordHelp" placeholder="Enter password">
        </div>
        <div class="loginPageButtonContainer">
            <button @click="displayNewUserPage()" type="button" class="climbingAppButton">Create a New User</button>
            <button @click="$emit('loginUser', {username, password})" type="button" class="climbingAppButton" :disabled="username === '' || password === ''">Login</button>
        </div>
    </div>
</template>
<style scoped>
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

.incorrectUsernameOrPasswordWarning {
    font-size: 1.2rem;
    padding-top: 10px;
}

.loginPageButtonContainer {
    display: flex;
    flex-direction: column;
    justify-self: center;
    width: 50%;
    padding-top: 10px;
}
</style>