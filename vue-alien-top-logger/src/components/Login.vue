<script>

import { BFormInput } from 'bootstrap-vue-next';
import { BForm } from 'bootstrap-vue-next';
export default {
    name: 'UserTrackRoutes',
    data: function () {
        return {
            username: null,
            password: null
        }
    }
}
</script>

<template>
    <div>
        Login Page
    </div>
    <BForm>
        <BFormInput>
            id="username"
            v-model="username"
            required
        </BFormInput>
        <BFormInput>
            id="password"
            v-model="password"
            required
        </BFormInput>
    </BForm>
    <div>
        LOGIN
    </div>
</template>