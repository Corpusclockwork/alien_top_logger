<script>
export default {
    name: 'Login',
    data: function () {
        return {
            username: null,
            password: null
        }
    },
}
</script>

<template>
    <div class="loginPage">
        <div class="loginPageHeader">
            Login:
        </div>
        <div class="flex items-center gap-4 mb-2">
            <label for="username" class="loginPageSectionHeader font-semibold w-24">Username</label>
            <input type="username" class="loginPageSectionText form-control" id="usernameinput" aria-describedby="userHelp" placeholder="Enter username">
        </div>
         <div class="flex items-center gap-4 mb-2">
            <label for="email" class="newUserPageSectionHeader font-semibold w-24">Email</label>
            <input type="email" class="newUserPageSectionText form-control" id="emailinput" aria-describedby="emailHelp" placeholder="Enter email address">
        </div>
        <div class="flex items-center gap-4 mb-2">
            <label for="password" class="loginPageSectionHeader font-semibold w-24">Password</label>
            <input type="password" class="loginPageSectionText form-control" id="passwordinput" aria-describedby="passwordHelp" placeholder="Enter password">
        </div>
        <button @click="login()" type="button" class="loginButton btn btn-primary"> Login</button>
    </div>
</template>
<style>
.loginPage {
    margin: 10%;
    line-height: 1;
    border-radius: 5px;
    margin-bottom: 0;
    padding-bottom: 10%;
    color: white;
    font-size: 4rem;
    display: grid;
}

.loginPage{
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