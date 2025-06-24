<script>
export default {
    name: 'UserTrackRoutes',
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
        Login Page
    </div>
    <div class="flex items-center gap-4 mb-4">
        <label for="username" class="font-semibold w-24">Username</label>
        <input type="username" class="form-control" id="usernameinput" aria-describedby="userHelp" placeholder="Enter username">
    </div>
    <div class="flex items-center gap-4 mb-2">
        <label for="email" class="font-semibold w-24">Email</label>
        <input type="email" class="form-control" id="emailinput" aria-describedby="emailHelp" placeholder="Enter email">
    </div>
</template>