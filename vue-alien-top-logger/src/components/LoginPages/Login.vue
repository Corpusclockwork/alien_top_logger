<script>
import MainPage from "../MainPage.vue"
export default {
    name: 'Login',
    data: function () {
        return {
            username: null,
            password: null,
            email: null,
         
            isClimbingStaffMember: false, 
            csrfToken: null,
            isAuthenticated: false
        }
    },
    components: {
        MainPage
    },
    created() {
        this.isUserAuthenticated();
    },
    methods:{
        async getCSRF() {
            // this.csrfToken = null;
            console.log("hi")
            const response = await fetch("http://localhost:8000/api/v1/csrf/", {
                credentials: "include"
            });
            if (response.ok == true){
                this.csrfToken = response.headers.get("X-CSRFToken");
                console.log(this.csrfToken);
                console.log(response);
            } 
        },
        async isUserAuthenticated() {
            const response = await fetch("http://localhost:8000/api/v1/session/", {
                credentials: "include"
            });
            const data = await response.json()
            console.log(data);
            if (data.isAuthenticated){
                this.isAuthenticated = true;
                this.getCSRF();
            } else {
                this.isAuthenticated = false;
                this.getCSRF();
            }
        },
        async loginUser() {
            console.log(this.csrfToken)
            const response = await fetch("http://localhost:8000/api/v1/login/", {
                method: "POST",
                headers: {
                    'Content-Type': 'application/json',
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
                this.isAuthenticated = true;
                // this.isClimbingStaffMember = response.body.isClimbingStaffMember
            }
        },
        async logoutUser() {
            const response = await fetch("http://localhost:8000/api/v1/logout/", {
                credentials: "include",
            })
            if (response.ok) {
                this.isAuthenticated = false
                this.getCSRF();
            }
        },
    }
}
</script>

<template>
    <div v-if="!isAuthenticated" class="loginPage">
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
        <button @click="loginUser()" type="button" class="loginButton btn btn-primary"> Login</button>
        
    </div>
    <div v-if="isAuthenticated">
        <button @click="logoutUser()" class="loginButton">Logout</button>
        <MainPage
            :isClimbingStaffMember="isClimbingStaffMember"
        >
        </MainPage>
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