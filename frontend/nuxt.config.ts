import { defineNuxtConfig } from 'nuxt'

export default defineNuxtConfig({
  buildModules: [
    '@pinia/nuxt',
  ],
  router: {
    middleware: 'auth'
  }
})
