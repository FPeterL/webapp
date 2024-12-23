<template>
  <div>
    <!-- Itt renderálódnak az oldalak -->
    <NuxtPage />
  </div>
</template>

<script setup>
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'

const store = useStore()
const router = useRouter()

// Ellenőrizzük a store és router helyes használatát
</script>

<style scoped>
/* Alapértelmezett stílusok, ha szükséges */
</style>
