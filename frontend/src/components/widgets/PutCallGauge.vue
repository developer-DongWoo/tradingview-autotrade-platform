<template>
  <div class="chart-card">
    <h3>📊 Put / Call Ratio</h3>
    <canvas ref="gauge"></canvas>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue"
import { Chart } from "chart.js/auto"

const gauge = ref(null)

onMounted(() => {
  new Chart(gauge.value, {
    type: "doughnut",
    data: {
      labels: ["Call", "Put"],
      datasets: [
        {
          data: [65, 35],
          backgroundColor: ["rgba(0,245,255,0.6)", "rgba(255,0,60,0.6)"],
          borderWidth: 0,
        },
      ],
    },
    options: {
      cutout: "75%",
      plugins: {
        legend: { display: true, labels: { color: "#00f5ff" } },
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
  color: #00f5ff;
  text-align: center;
  width: 100%;
  max-width: 400px;
}
canvas {
  max-height: 240px;
}
</style>
