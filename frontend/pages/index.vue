<template>
  <div>
    <h1>Stock Price Checker</h1>
    <form @submit.prevent="fetchStock">
      <div>
        <label for="symbol">Stock Symbol:</label>
        <input id="symbol" v-model="symbol" type="text" placeholder="e.g., AAPL" />
      </div>
      <button type="submit">Check Price</button>
    </form>
    <div v-if="stockData">
      <h2>Stock Data</h2>
      <p>Symbol: {{ stockData.symbol }}</p>
      <p>Price: ${{ stockData.price }}</p>
      <p>Time: {{ stockData.time }}</p>
    </div>
    <div v-if="error">{{ error }}</div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';

const symbol = ref('');
const stockData = ref(null);
const error = ref('');

const fetchStock = async () => {
  try {
    const response = await axios.get('http://localhost:5000/stock', {
      params: { symbol: symbol.value },
    });
    stockData.value = response.data;
    error.value = '';
  } catch (err) {
    stockData.value = null;
    error.value = err.response?.data?.error || 'An error occurred';
  }
};
</script>

<style scoped>
form {
  margin-top: 1em;
}
</style>
