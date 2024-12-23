import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    authenticated: false
  }),
  actions: {
    setAuthenticated(value) {
      this.authenticated = value
    }
  }
})
