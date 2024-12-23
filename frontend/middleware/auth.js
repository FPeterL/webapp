import { useAuthStore } from '~/store/auth'

export default defineNuxtMiddleware((context) => {
  const authStore = useAuthStore(context.$pinia)
  if (!authStore.authenticated) {
    return context.redirect('/login')
  }
})
