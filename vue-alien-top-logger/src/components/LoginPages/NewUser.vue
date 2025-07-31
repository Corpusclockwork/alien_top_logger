<script>
export default {
    name: 'NewUser',
    data: function () {
        return {
            username: '',
            password: '',
            repeatPassword: '',
            passwordsAreEqual: true,
            usernameIsValid: false,
            isClimbingStaffMember: false
        }
    },
    props:{
        newUserMessageToDisplay: String
    },
    methods: {
        checkPasswordsAreEqual(){
            if (this.repeatPassword === this.password) {
                this.passwordsAreEqual = true;
            } else {
                this.passwordsAreEqual = false;
            }
        },
        checkSafeUsername(){
            // Usernames in Django have to have 150 characters or fewer. 
            // Usernames may contain alphanumeric, _, @, +, . and - characters.
            // I guess I should check these things are true in the front end to not waste user time
            const pattern = /^[a-zA-Z0-9_@+.-]{1,150}$/;
            this.usernameIsValid = pattern.test(this.username);
        },
        // 'Django's authentication framework will now automatically fail authentication for any password exceeding 4096 bytes.''
        // As of 2013, so I don't need to validate on the front end to prevent DoS attacks, any password too long will be dismissed anyway
        // (Django uses PBKDF2 by default to store passwords)
        displayLoginPage(){
            this.$emit("toggleLoginPages");
        }
    },
    watch: {
        username(){
            this.checkSafeUsername();
        },
        repeatPassword(){
            this.checkPasswordsAreEqual();
        },
        password(){
            this.checkPasswordsAreEqual();
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
                <div class="checkboxWarningText">(This checkbox should be removed before real customer use)</div>
            </div>
        </div>
        <div class="flex items-center gap-4 mb-2">
            <label for="username" class="newUserPageSectionHeader font-semibold w-24">Username</label>
            <input v-model="username" type="username" class="newUserPageSectionText form-control" id="usernameinput" aria-describedby="userHelp" placeholder="Enter username">
        </div>
        <div v-show="!usernameIsValid" class="usernameWarning">Username can contain only alphanumeric, _, @, +, . and - characters, and must be between 1 and 150 characters.</div>
        <div class="flex items-center gap-4 mb-2">
            <label for="password" class="newUserPageSectionHeader font-semibold w-24">Password</label>
            <input v-model="password" type="password" class="newUserPageSectionText form-control" id="passwordinput" aria-describedby="passwordHelp" placeholder="Enter password">
        </div>
        <div class="flex items-center gap-4 mb-2">
            <label for="password" class="newUserPageSectionHeader font-semibold w-24">Repeat password</label>
            <input v-model="repeatPassword" type="password" class="newUserPageSectionText form-control" id="repeatpasswordinput" aria-describedby="passwordHelp" placeholder="Enter password">
        </div>
        <div v-show="!passwordsAreEqual" class="passwordWarning"> Passwords don't match !</div>
        <div class="userCreatedMessage">{{newUserMessageToDisplay}}</div>
        <div class="createUserPageButtonContainer">
            <button @click="$emit('createUser', {username, password, isClimbingStaffMember})" type="button" class="climbingAppButton" :disabled="!passwordsAreEqual || password === '' || !usernameIsValid"> Create User</button>
            <button @click="displayLoginPage()" type="button" class="climbingAppButton">Go to Login Page</button>
        </div>
    </div>
</template>
<style scoped>
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
    font-size: 1.2rem;
}
.passwordWarning {
    font-size: 1.2rem;
}
.usernameWarning {
    font-size: 1.2rem;
}
.isStaffText {
    padding: 10px;
    font-size: 2rem;
}
@media only screen and (max-width: 600px) {
    .isStaffText{
        font-size: 1.5rem;
    }
    .checkboxWarningText {
        font-size: 1rem;
    }
}
.userCreatedMessage{
    font-size: 1.2rem;
    color: black;
}
.createUserPageButtonContainer {
    display: flex;
    flex-direction: column;
    justify-self: center;
    width: 50%;
    padding-top: 10px;
}
</style>