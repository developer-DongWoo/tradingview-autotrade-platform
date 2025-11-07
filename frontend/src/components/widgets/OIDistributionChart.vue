<template>
  <div class="chart-card">
    <h3>💥 OI Distribution</h3>
    <canvas ref="oiChart"></canvas>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue"
import { Chart } from "chart.js/auto"

const oiChart = ref(null)

onMounted(() => {
  new Chart(oiChart.value, {
    type: "bar",
    data: {
      labels: ["4300", "4400", "4500", "4600", "4700", "4800"],
      datasets: [
        {
          label: "Call OI",
          data: [1200, 1500, 2200, 2500, 1800, 900],
          backgroundColor: "rgba(0,245,255,0.5)",
        },
        {
          label: "Put OI",
          data: [900, 1300, 1800, 2100, 2400, 2800],
          backgroundColor: "rgba(255,0,60,0.5)",
        },
      ],
    },
    options: {
      responsive: true,
      scales: {
        x: { ticks: { color: "#00f5ff" } },
        y: { ticks: { color: "#00f5ff" } },
      },
      plugins: {
        legend: { labels: { color: "#00f5ff" } },
      },
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
  max-height: 280px;
}
</style>
