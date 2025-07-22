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
            username: "",
            displayLoginPage: true,
            isClimbingStaffMember: undefined,
            displayMainPage: false
        }
    },
    created() {
        this.session();
    },
    methods: {
        getCookie(name) {
            let cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        },
        async session() {
            const response = await fetch("http://localhost:8000/api/v1/session/", {
                credentials: "include"
            });
            const data = await response.json()
            console.log(data);
            if (data.isAuthenticated){
                this.isAuthenticated = true;
                this.isClimbingStaffMember = data.isClimbingStaffMember
                this.username = data.username
            } else {
                this.isAuthenticated = false;
            }
            this.csrfToken = this.getCookie("csrftoken");
        },
        async logoutUser() {
            const response = await fetch("http://localhost:8000/api/v1/logout/", {
                credentials: "include",
            })
            if (response.ok) {
                this.isAuthenticated = false
            }
        }
    }
}
</script>
<template>
    <MainPage 
        v-if="isAuthenticated"
        :isClimbingStaffMember="isClimbingStaffMember"
        :csrfToken="csrfToken"
        :username="username"
        :updateCSRFToken="csrfToken = getCookie('csrftoken')"
        @logoutUser="logoutUser()"
    ></MainPage>
    <Login
        v-else-if="displayLoginPage && !isAuthenticated"
        @userAuthenticated="isAuthenticated = true"
        @username="(value) => {username = value}"
        @isClimbingStaffMember="(value)=> {isClimbingStaffMember = value}"
        @toggleLoginPages="displayLoginPage = false"
        :csrfToken="csrfToken"
    ></Login>
    <NewUser
        v-else-if="!displayLoginPage && !isAuthenticated"
        @toggleLoginPages="displayLoginPage = true"
    ></NewUser>
</template>

