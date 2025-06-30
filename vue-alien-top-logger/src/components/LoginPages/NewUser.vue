<script>
export default {
    name: 'NewUser',
    data: function () {
        return {
            username: null,
            email: null,
            password: null
        }
    },
    methods: {
        async Login(){
            console.log("hi");
            const response = await fetch("http://127.0.0.1:8000/api/v1/newuser", {
                method: "POST",
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify([{username: this.username, email: this.email, password: this.password}])
            });
            console.log(response);
        }
    }
}
</script>
<template>
    <div class="newUserPage">
        <div class="newUserPageHeader">
            New User:
        </div>
        <div class="flex items-center gap-4 mb-4">
            <label for="username" class="newUserPageSectionHeader font-semibold w-24">Username</label>
            <input type="username" class="newUserPageSectionText form-control" id="usernameinput" aria-describedby="userHelp" placeholder="Enter username">
        </div>
         <div class="flex items-center gap-4 mb-2">
            <label for="email" class="newUserPageSectionHeader font-semibold w-24">Email</label>
            <input type="email" class="newUserPageSectionText form-control" id="emailinput" aria-describedby="emailHelp" placeholder="Enter email address">
        </div>
        <div class="flex items-center gap-4 mb-2">
            <label for="password" class="newUserPageSectionHeader font-semibold w-24">Password</label>
            <input type="password" class="newUserPageSectionText form-control" id="passwordinput" aria-describedby="passwordHelp" placeholder="Enter password">
        </div>
        <div class="flex items-center gap-4 mb-2">
            <label for="password" class="newUserPageSectionHeader font-semibold w-24">Repeat password</label>
            <input type="password" class="newUserPageSectionText form-control" id="repeatpasswordinput" aria-describedby="passwordHelp" placeholder="Enter password">
        </div>
        <div> Passwords don't match !</div>
        <div class="flex items-center gap-4 mb-2">
            <label for="checkbox" class="newUserPageSectionHeader font-semibold w-24">Is Staff User</label>
            <input type="checkbox" class="newUserPageSectionText form-control" id="isStaff" aria-describedby="isStaff">
        </div>
        <div>(This checkbox will be removed before customer use)</div>
        <button @click="Login()"> Login</button>
    </div>
</template>
<style>
.newUserPage {
    margin: 10%;
    line-height: 1;
    border-radius: 5px;
    color: white;
}

.newUserPage{
    font-size: 4rem;
}

.newUserPageSectionHeader {
    font-size: 2rem;
}

.newUserPageSectionText {
    font-family: "Montserrat", Sans-serif;
}
</style>