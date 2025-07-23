<script>
export default {
    name: 'NewUser',
    data: function () {
        return {
            username: '',
            password: '',
            repeatPassword: '',
            passwordsAreEqual: true,
            isClimbingStaffMember: false
        }
    },
    methods: {
        checkPasswordsAreEqual(){
            if (this.repeatPassword === this.password) {
                this.passwordsAreEqual = true;
            } else {
                this.passwordsAreEqual = false;
            }
        },
        displayLoginPage(){
            this.$emit("toggleLoginPages");
        }
    },
    watch: {
        repeatPassword(){
            this.checkPasswordsAreEqual()
        },
        password(){
            this.checkPasswordsAreEqual()
        }
    }
}
</script>
<template>
    <div class="newUserPage">
        <div class = "Header">
            <div>
                New User:
            </div>
            <div>
                <input v-model="isClimbingStaffMember" type="checkbox" class="newUserPageSectionText" id="isStaff" aria-describedby="isStaff">
                <label for="checkbox" class="isStaffText font-semibold w-24">Create a staff user ?</label>
                <div class="checkboxWarningText">(This checkbox should be removed before general customer use)</div>
            </div>
        </div>
        <div class="flex items-center gap-4 mb-2">
            <label for="username" class="newUserPageSectionHeader font-semibold w-24">Username</label>
            <input v-model="username" type="username" class="newUserPageSectionText form-control" id="usernameinput" aria-describedby="userHelp" placeholder="Enter username">
        </div>
        <div class="flex items-center gap-4 mb-2">
            <label for="password" class="newUserPageSectionHeader font-semibold w-24">Password</label>
            <input v-model="password" type="password" class="newUserPageSectionText form-control" id="passwordinput" aria-describedby="passwordHelp" placeholder="Enter password">
        </div>
        <div class="flex items-center gap-4 mb-2">
            <label for="password" class="newUserPageSectionHeader font-semibold w-24">Repeat password</label>
            <input v-model="repeatPassword" type="password" class="newUserPageSectionText form-control" id="repeatpasswordinput" aria-describedby="passwordHelp" placeholder="Enter password">
        </div>
        <div v-show="!passwordsAreEqual" class="passwordWarning"> Passwords don't match !</div>
        <div class="createUserPageButtonContainer">
            <button @click="$emit('createUser', {username: username, password: password, isClimbingStaffMember: isClimbingStaffMember})" type="button" class="createUserPageButton createUserButton" :disabled="!passwordsAreEqual || password === ''"> Create User</button>
            <button @click="displayLoginPage()" type="button" class="createUserPageButton">Go to Login Page</button>
        </div>
    </div>
</template>
<style>

.Header {
    display: flex;
    justify-content: space-between;
}

.newUserPage {
    padding: 10%;
    line-height: 1;
    border-radius: 5px;
    color: white;
    font-size: 4rem;
    display: grid;
}

.newUserPageSectionHeader {
    font-size: 2rem;
}

.newUserPageSectionText {
    font-family: "Montserrat", Sans-serif;
}

.checkboxWarningText {
    font-size: 1rem;
}

.passwordWarning {
    font-size: 1.5rem;
}

.isStaffText {
    padding: 10px;
    font-size: 2rem;
}

@media only screen and (max-width: 600px) {
    .isStaffText{
        font-size: 1rem;
    }
    .checkboxWarningText {
        font-size: 0.7rem;
    }
}

.createUserPageButtonContainer {
    display: flex;
    flex-direction: column;
    justify-self: center;
}

.createUserPageButton {
    font-size: 1.5rem;
    background-color: #E9704B;
    color: white;
    border-color: #E9704B;
    justify-self: center;
    border-radius: 15px;
    margin: 5px;
    padding: 10px;
}

.createUserPageButton:disabled {
    background-color: grey;
}

.createUserPageButton:hover:enabled {
    background-color: #994931;
}
</style>