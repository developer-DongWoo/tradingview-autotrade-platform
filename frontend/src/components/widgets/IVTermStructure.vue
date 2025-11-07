<template>
  <div class="chart-card">
    <h3>⏳ IV Term Structure</h3>
    <canvas ref="termChart"></canvas>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue"
import { Chart } from "chart.js/auto"

const termChart = ref(null)

onMounted(() => {
  new Chart(termChart.value, {
    type: "line",
    data: {
      labels: ["1주", "2주", "1개월", "2개월", "3개월"],
      datasets: [
        {
          label: "Implied Volatility",
          data: [18, 19, 20, 22, 25],
          borderColor: "#ffcc00",
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
