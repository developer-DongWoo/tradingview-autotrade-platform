<template>
  <div class="chart-card">
    <h3>⚡ Volume Flow</h3>
    <canvas ref="volChart"></canvas>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue"
import { Chart } from "chart.js/auto"

const volChart = ref(null)

onMounted(() => {
  new Chart(volChart.value, {
    type: "line",
    data: {
      labels: ["09:30", "10:30", "11:30", "12:30", "13:30", "14:30", "15:30"],
      datasets: [
        {
          label: "Call Volume",
          data: [300, 500, 800, 600, 1000, 1500, 1200],
          borderColor: "rgba(0,245,255,0.7)",
          fill: false,
          tension: 0.4,
        },
        {
          label: "Put Volume",
          data: [200, 400, 700, 900, 800, 1000, 1300],
          borderColor: "rgba(255,0,60,0.7)",
          fill: false,
          tension: 0.4,
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
