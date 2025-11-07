<template>
  <div class="chart-box">
    <h3>Market Momentum</h3>
    <canvas id="momentum-chart"></canvas>
  </div>
</template>

<script setup>
import { onMounted } from "vue"
import Chart from "chart.js/auto"

onMounted(() => {
  const ctx = document.getElementById("momentum-chart")
  new Chart(ctx, {
    type: "line",
    data: {
      labels: Array.from({ length: 10 }, (_, i) => i + 1),
      datasets: [
        {
          label: "Momentum",
          data: Array.from({ length: 10 }, () => Math.random() * 100),
          borderColor: "#00f5ff",
          borderWidth: 2,
          fill: false,
          tension: 0.3,
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
