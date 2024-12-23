<!-- layouts/default.vue -->
<template>
  <div>
    <header>
      <!-- Itt elhelyezheted a fejlécedet, például navigációt -->
      <h1>Welcome to My Nuxt App</h1>
    </header>
    <main>
      <!-- Ez az, ami megjeleníti az oldalakat a NuxtPage komponens segítségével -->
      <NuxtPage />
    </main>
  </div>
</template>

<style scoped>
header {
  background-color: #f8f9fa;
  padding: 20px;
  text-align: center;
}
main {
  padding: 20px;
}
</style>
