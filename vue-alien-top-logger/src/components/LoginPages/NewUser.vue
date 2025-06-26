<script>
export default {
    name: 'NewUser',
    data: function () {
        return {
            username: null,
            password: null
        }
    },
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
            <label for="password" class="newUserPageSectionHeader font-semibold w-24">Password</label>
            <input type="password" class="newUserPageSectionText form-control" id="passwordinput" aria-describedby="passwordHelp" placeholder="Enter password">
        </div>

        <div class="flex items-center gap-4 mb-2">
            <label for="password" class="newUserPageSectionHeader font-semibold w-24">Repeat password</label>
            <input type="password" class="newUserPageSectionText form-control" id="passwordinput" aria-describedby="passwordHelp" placeholder="Enter password">
        </div>
        <div> Passwords don't match !</div>
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