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
            isClimbingStaffMember: undefined,

            displayLoginPage: true,
            displayMainPage: false,
            
            mainPageMessageToDisplay: "",
            loginUserMessageToDisplay: "",
            newUserMessageToDisplay: ""
        }
    },
    created() {
        this.setCSRFToken();
        this.whoAmI();
    },
    methods: {
        getCSRFToken() {
            let cookieValue = null;
            const name = 'csrftoken'
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
        async loginUser(loginDetails) {
            const response = await fetch("http://localhost:8000/api/v1/login/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": this.getCSRFToken()
                },
                credentials: "include",
                body: JSON.stringify({
                    username: loginDetails.username, 
                    password: loginDetails.password
                })
            });
            if (response.ok == true){
                this.whoAmI();
            } else {
                this.loginUserMessageToDisplay= "You have entered an invalid username or password"
            }
        },
        async logoutUser() {
            try {
                const response = await fetch("http://localhost:8000/api/v1/logout/", {
                    method: 'POST',
                    headers: {
                        "Content-Type": "application/json",
                        'X-CSRFToken': this.getCSRFToken()
                    },
                    credentials: 'include',
                })
                if (response.ok) {
                    this.isAuthenticated = false;
                    this.username = "";
                    this.isClimbingStaffMember = undefined;
                }
            } catch(error) {
                this.mainPageMessageToDisplay= "Log out failed, honestly congrats, idk how you *did* that"
                throw error
            }
        },
        async setCSRFToken() {
            await fetch("http://localhost:8000/api/v1/session/",{
                credentials: "include"
            })        
        },
        async whoAmI() {
            const response = await fetch("http://localhost:8000/api/v1/whoami/",{
                method: 'GET',
                credentials: "include",
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': this.getCSRFToken()
                },
            });
            const data = await response.json();
            if (data.isAuthenticated){
                this.isAuthenticated = true;
                this.username = data.username;
                this.isClimbingStaffMember = data.isClimbingStaffMember;
            } else {
                this.isAuthenticated = false;
            }
        },
        async createUser(newUserDetails){
            const response = await fetch("http://localhost:8000/api/v1/newuser/", {
                method: "POST",
                headers: {
                    'Accept': 'application/json',
                    'X-CSRFToken': this.getCSRFToken()
                },
                credentials: "include",
                body: JSON.stringify({
                    username: newUserDetails.username, 
                    password: newUserDetails.password, 
                    isClimbingStaffMember: newUserDetails.isClimbingStaffMember
                })
            });
            const data = await response.json();
            if (data.status === 201) {
                this.loginUser({username: newUserDetails.username, password: newUserDetails.password});
            } else {
                 this.newUserMessageToDisplay= "Failed to create new user, username already in use"
            }
        }
    }
}
</script>
<template>
    <MainPage 
        v-if="isAuthenticated"
        :csrfToken="getCSRFToken()"
        :username="username"
        :isClimbingStaffMember="isClimbingStaffMember"
        :mainPageMessageToDisplay="mainPageMessageToDisplay"
        @logoutUser="logoutUser"
    ></MainPage>
    <Login
        v-else-if="displayLoginPage && !isAuthenticated"
        :loginUserMessageToDisplay="loginUserMessageToDisplay"
        @loginUser="loginUser"
        @toggleLoginPages="displayLoginPage = false; loginUserMessageToDisplay = '';"
    ></Login>
    <NewUser
        v-else-if="!displayLoginPage && !isAuthenticated"
        :newUserMessageToDisplay="newUserMessageToDisplay"
        @createUser="createUser"
        @toggleLoginPages="displayLoginPage = true; newUserMessageToDisplay = '';"
    ></NewUser>
</template>

