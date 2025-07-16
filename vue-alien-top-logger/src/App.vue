<script>
import Login from './components/LoginPages/Login.vue';
import MainPage from './components/MainPage.vue';
import NewUser from './components/LoginPages/NewUser.vue';
export default {
    name: "App",
    components: {
        Login,
        MainPage,
        NewUser
    },
    data: function () {
        return {
            isAuthenticated: null,
            csrfToken: "",
            displayLoginPage: true,
            isClimbingStaffMember: undefined,
            displayMainPage: false
        }
    },
    created() {
        this.isUserAuthenticated();
    },
    methods: {
        async getCSRF() {
            const response = await fetch("http://localhost:8000/api/v1/csrf/", {
                credentials: "include"
            });
            if (response.ok == true){
                this.csrfToken = response.headers.get("X-CSRFToken");
                console.log(this.csrfToken);
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
                this.isClimbingStaffMember = data.isClimbingStaffMember
                this.getCSRF();
            } else {
                this.isAuthenticated = false;
                this.getCSRF();
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
        }
    }
}
</script>
<template>
    <MainPage 
        v-if="isAuthenticated"
        :isClimbingStaffMember="isClimbingStaffMember"
        @logoutUser="logoutUser()"
    ></MainPage>
    <Login
        v-else-if="displayLoginPage && !isAuthenticated"
        @userAuthenticated="isAuthenticated = true"
        @isClimbingStaffMember="(value)=> {isClimbingStaffMember = value}"
        @toggleLoginPages="displayLoginPage = false"
        :csrfToken="csrfToken"
    ></Login>
    <NewUser
        v-else-if="!displayLoginPage && !isAuthenticated"
        @toggleLoginPages="displayLoginPage = true"
    ></NewUser>
</template>

