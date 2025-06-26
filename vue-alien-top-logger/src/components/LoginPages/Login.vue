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
        <div class="flex items-center gap-4 mb-4">
            <label for="username" class="loginPageSectionHeader font-semibold w-24">Username</label>
            <input type="username" class="loginPageSectionText form-control" id="usernameinput" aria-describedby="userHelp" placeholder="Enter username">
        </div>
        <div class="flex items-center gap-4 mb-2">
            <label for="password" class="loginPageSectionHeader font-semibold w-24">Password</label>
            <input type="password" class="loginPageSectionText form-control" id="passwordinput" aria-describedby="passwordHelp" placeholder="Enter password">
        </div>
    </div>
</template>
<style>
.loginPage {
    margin: 10%;
    line-height: 1;
    border-radius: 5px;
    color: white;
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
</style>