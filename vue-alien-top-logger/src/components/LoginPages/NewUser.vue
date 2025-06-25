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
    <div>
        New User:
    </div>
    <div class="flex items-center gap-4 mb-4">
        <label for="username" class="font-semibold w-24">Username</label>
        <input type="username" class="form-control" id="usernameinput" aria-describedby="userHelp" placeholder="Enter username">
    </div>
    <div class="flex items-center gap-4 mb-2">
        <label for="password" class="font-semibold w-24">Password</label>
        <input type="password" class="form-control" id="passwordinput" aria-describedby="passwordHelp" placeholder="Enter password">
    </div>
    <div class="flex items-center gap-4 mb-2">
        <label for="password" class="font-semibold w-24">Repeat password</label>
        <input type="password" class="form-control" id="passwordinput" aria-describedby="passwordHelp" placeholder="Enter password">
    </div> 
    <div> Passwords don't match !</div>
</template>