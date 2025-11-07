<template>
  <div class="chart-card">
    <h3>🌡️ IV Smile Curve</h3>
    <canvas ref="ivChart"></canvas>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue"
import { Chart } from "chart.js/auto"

const ivChart = ref(null)

onMounted(() => {
  new Chart(ivChart.value, {
    type: "line",
    data: {
      labels: ["-10%", "-5%", "ATM", "+5%", "+10%"],
      datasets: [
        {
          label: "Implied Volatility",
          data: [22, 19, 16, 18, 21],
          borderColor: "#00f5ff",
          tension: 0.4,
          fill: false,
        },
      ],
    },
    options: {
      scales: {
        x: { ticks: { color: "#00f5ff" } },
        y: { ticks: { color: "#00f5ff" } },
      },
      plugins: { legend: { labels: { color: "#00f5ff" } } },
    },
  })
})
</script>

<style scoped>
.chart-card {
  background: rgba(0, 0, 0, 0.4);
  border: 1px solid rgba(0, 245, 255, 0.2);
  border-radius: 10px;
  padding: 20px;
  text-align: center;
  color: #00f5ff;
  width: 100%;
  max-width: 480px;
}
canvas {
  max-height: 260px;
}
</style>
