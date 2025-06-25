<script setup>
    import { RouterView } from 'vue-router';
</script>

<template>
  <nav>
    <RouterLink to="/">Go to Login page</RouterLink>
    <RouterLink to="/usertrackroutes">Go to Main page</RouterLink>
  </nav>

  <RouterView/>
</template>

