<script>
export default {
    name: 'NewUser',
    data: function () {
        return {
            username: null,
            email: null,
            password: null,
            repeatPassword: null,
            passwordsAreEqual: true,
            isClimbingStaffMemberInFrontEnd: false
        }
    },
    methods: {
        async createUser(){
            console.log("hi");
            const response = await fetch("http://127.0.0.1:8000/api/v1/newuser/", {
                method: "POST",
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    username: this.username, 
                    email: this.email, 
                    password: this.password, 
                    isClimbingStaffMemberInFrontEnd: this.isClimbingStaffMemberInFrontEnd
                })
            });
            console.log(response);
        },
        checkPasswordsAreEqual(){
            if (this.repeatPassword === this.password) {
                this.passwordsAreEqual = true;
            } else {
                this.passwordsAreEqual = false;
            }
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
                <input v-model="isClimbingStaffMemberInFrontEnd" type="checkbox" class="newUserPageSectionText" id="isStaff" aria-describedby="isStaff">
                <label for="checkbox" class="isStaffText font-semibold w-24">Create a staff user ?</label>
                <div class="checkboxWarningText">(This checkbox should be removed before general customer use)</div>
            </div>
        </div>
        <div class="flex items-center gap-4 mb-2">
            <label for="username" class="newUserPageSectionHeader font-semibold w-24">Username</label>
            <input v-model="username" type="username" class="newUserPageSectionText form-control" id="usernameinput" aria-describedby="userHelp" placeholder="Enter username">
        </div>
         <div class="flex items-center gap-4 mb-2">
            <label for="email" class="newUserPageSectionHeader font-semibold w-24">Email</label>
            <input v-model="email" type="email" class="newUserPageSectionText form-control" id="emailinput" aria-describedby="emailHelp" placeholder="Enter email address">
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
        <button @click="createUser()" type="button" class="createUserButton btn btn-primary"> Create User</button>
    </div>
</template>
<style>

.Header {
    display: flex;
    justify-content: space-between;
}

.newUserPage {
    margin: 10%;
    line-height: 1;
    border-radius: 5px;
    color: white;
    margin-bottom: 0%;
    padding-bottom: 10%;
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
    font-size: 0.5rem;
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
.createUserButton {
    font-size: 2rem;
    background-color: #E9704B;
    color: white;
    border-color: #E9704B;
    justify-self: center;
}

.createUserButton:disabled {
    background-color: grey;
}

.createUserButton:hover {
    background-color: #994931;
}
</style>