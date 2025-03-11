<script setup>
import { RouterView } from 'vue-router'
</script>

<template>
  <div id="app">
    <RouterView />
    <div id="modal"></div>
  </div>
</template>

<style scoped>
#app {
  margin-top: 60px;
}
</style>
