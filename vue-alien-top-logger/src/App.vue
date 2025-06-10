<script setup>
    import { RouterView } from 'vue-router';
</script>

<template>
  <nav>
    <RouterLink to="/">Go to Home</RouterLink>
    <RouterLink to="/usertrackroutes">Go to Track Routes</RouterLink>
  </nav>

  <RouterView/>
</template>

