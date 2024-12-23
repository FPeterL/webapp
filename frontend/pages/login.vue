<template>
  <div>
    <h1>Login</h1>
    <form @submit.prevent="handleLogin">
      <div>
        <label for="username">Username:</label>
        <input id="username" v-model="username" type="text" placeholder="Enter your username" />
      </div>
      <div>
        <label for="password">Password:</label>
        <input id="password" v-model="password" type="password" placeholder="Enter your password" />
      </div>
      <button type="submit">Login</button>
    </form>
    <div v-if="error" class="error-message">{{ error }}</div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'
import { useAuthStore } from '~/store/auth'
import { useAuthStore } from '~/store/auth'

const username = ref('')
const password = ref('')
const error = ref('')
const router = useRouter()
const authStore = useAuthStore()

const handleLogin = async () => {
  try {
    const response = await axios.post('http://localhost:5000/login', {
      username: username.value,
      password: password.value,
    })

    if (response.status === 200) {
      authStore.setAuthenticated(true)
      router.push({ path: '/' })
    } else {
      error.value = 'Login failed'
    }
  } catch (err) {
    error.value = err.response?.data?.message || 'Login failed'
  }
}
</script>

<style scoped>
form {
  margin-top: 1em;
}
.error-message {
  color: red;
}
</style>
