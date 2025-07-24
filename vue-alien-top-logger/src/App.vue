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
            displayMainPage: false,
            messageToDisplay: ""
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
            // const data = await response.json();
            if (response.ok == true){
                this.whoAmI();
            } else {
                // failed to log in
                this.messageToDisplay= "You have entered an invalid username or password"
                console.log(this.messageToDisplay);
            }
        },
        async logoutUser() {
            try {
                const response = await fetch("http://localhost:8000/api/v1/logout/", {
                    method: 'POST',
                    headers: {
                        "Content-Type": "application/json",
                        'X-CSRFToken': this.getCSRFToken(),
                    },
                    credentials: 'include',
                })
                if (response.ok) {
                    this.isAuthenticated = false;
                    this.username = "";
                    this.isClimbingStaffMember = undefined;
                }
            } catch(error) {
                console.error('Logout failed', error)
                this.messageToDisplay= "Log out failed"
                console.log(this.messageToDisplay);
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
                credentials: "include",
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': this.getCSRFToken(),
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
            const response = await fetch("http://127.0.0.1:8000/api/v1/newuser/", {
                method: "POST",
                headers: {
                    'Accept': 'application/json'
                },
                credentials: "include",
                body: JSON.stringify({
                    username: newUserDetails.username, 
                    password: newUserDetails.password, 
                    isClimbingStaffMember: newUserDetails.isClimbingStaffMember
                })
            });
            if (response.ok) {
                // created user
                this.messageToDisplay= "Created User" 
                console.log(this.messageToDisplay);
            } else {
                 // failed to create user 
                 this.messageToDisplay= "Failed to create user"
                 console.log(this.messageToDisplay);
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
        :messageToDisplay="messageToDisplay"
        @logoutUser="logoutUser()"
    ></MainPage>
    <Login
        v-else-if="displayLoginPage && !isAuthenticated"
        :messageToDisplay="messageToDisplay"
        @loginUser="loginUser"
        @toggleLoginPages="displayLoginPage = false"
    ></Login>
    <NewUser
        v-else-if="!displayLoginPage && !isAuthenticated"
        :messageToDisplay="messageToDisplay"
        @createUser="createUser"
        @toggleLoginPages="displayLoginPage = true"
    ></NewUser>
</template>

