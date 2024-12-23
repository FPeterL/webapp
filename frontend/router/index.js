import { createRouter, createWebHistory } from 'vue-router'
import store from '../store'
import Login from '../pages/Login.vue'
import Index from '../pages/Index.vue'

const routes = [
  {
    path: '/',
    name: 'Index',
    component: Index,
    meta: {
      requiresAuth: true  // Bejelentkezést igénylő útvonal
    }
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth);
  const isAuthenticated = store.state.authenticated;

  if (requiresAuth && !isAuthenticated) {
    next({ name: 'Login' });  // Átirányítás a bejelentkezési oldalra
  } else {
    next();
  }
})

export default router
