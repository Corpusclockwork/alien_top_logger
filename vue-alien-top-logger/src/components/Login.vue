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
    <div class="form-check">
  <input class="form-check-input" type="checkbox" value="" id="defaultCheck1">
  <label class="form-check-label" for="defaultCheck1">
    Default checkbox
  </label>
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