<script>
export default {
    name: 'Login',
    data: function () {
        return {
            username: null,
            password: null,
            email: null,
            isClimbingStaffMember: false,
        }
    },
    props:{
        csrfToken: String,
        isAuthenticated: Boolean
    },
    methods:{
        async loginUser() {
            console.log(this.csrfToken);
            const response = await fetch("http://localhost:8000/api/v1/login/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": this.csrfToken
                },
                credentials: "include",
                body: JSON.stringify({
                    username: this.username, 
                    email: this.email, 
                    password: this.password
                })
            });
            if (response.ok == true){
                // this.isAuthenticated = true;
                this.$emit("userAuthenticated", {isAuthenticated: this.isAuthenticated});
                // this.isClimbingStaffMember = response.body.isClimbingStaffMember
            }
        },
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
            <label for="email" class="newUserPageSectionHeader font-semibold w-24">Email</label>
            <input v-model="email" type="email" class="newUserPageSectionText form-control" id="emailinput" aria-describedby="emailHelp" placeholder="Enter email address">
        </div>
        <div class="flex items-center gap-4 mb-2">
            <label for="password" class="loginPageSectionHeader font-semibold w-24">Password</label>
            <input v-model="password" type="password" class="loginPageSectionText form-control" id="passwordinput" aria-describedby="passwordHelp" placeholder="Enter password">
        </div>
        <button @click="loginUser()" type="button" class="loginButton btn btn-primary">Login</button>
        <button @click="displayNewUserPage()" type="button" class="loginButton btn btn-primary">Create a New User</button>
    </div>
</template>
<style>
.loginPage {
    line-height: 1;
    border-radius: 5px;
    color: white;
    font-size: 4rem;
    display: grid;
    font-size: 4rem;
}

.loginPageSectionHeader {
    font-size: 2rem;
}

.loginPageSectionText {
    font-family: "Montserrat", Sans-serif;
}

.loginButton {
    font-size: 2rem;
    background-color: #E9704B;
    color: white;
    border-color: #E9704B;
    justify-self: center;
}

.loginButton:disabled {
    background-color: grey;
}

.loginButton:hover {
    background-color: #994931;
}
</style>