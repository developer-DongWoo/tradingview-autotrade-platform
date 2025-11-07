<template>
  <div class="chart-box">
    <h3>Bubble Index</h3>
    <canvas id="bubble-chart"></canvas>
  </div>
</template>

<script setup>
import { onMounted } from "vue"
import Chart from "chart.js/auto"

onMounted(() => {
  const ctx = document.getElementById("bubble-chart")
  new Chart(ctx, {
    type: "bar",
    data: {
      labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
      datasets: [
        {
          label: "Bubble Score",
          data: [30, 50, 80, 60, 40, 90],
          backgroundColor: "#00f5ff55",
          borderColor: "#00f5ff",
          borderWidth: 1,
        },
      ],
    },
    options: {
      plugins: { legend: { display: false } },
      scales: { x: { display: false }, y: { display: false } },
    },
  })
})
</script>

<style scoped>
.chart-box {
  background: #0a0a0a;
  border: 1px solid rgba(0, 245, 255, 0.2);
  border-radius: 10px;
  padding: 10px 20px;
  width: 280px;
  height: 180px;
}
h3 {
  color: #00f5ff;
  font-size: 14px;
  margin-bottom: 6px;
  text-align: left;
}
</style>
