<template>
  <div class="modal-backdrop" @click.self="emit('close')">
    <div class="modal-content">
      <h2>{{ name }} 옵션 분석</h2>
      <p class="desc">AI 기반 심리 분석 결과 요약</p>

      <div class="chart-area">
        <p>📈 IV Term Structure</p>
        <div class="fake-chart"></div>
        <p>📊 OI Distribution</p>
        <div class="fake-chart"></div>
      </div>

      <button class="close-btn" @click="emit('close')">닫기 ✕</button>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  name: String,
})
const emit = defineEmits(["close"])
</script>

<style scoped>
.modal-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.85);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 999;
  animation: fadeIn 0.3s ease;
}

.modal-content {
  background: rgba(10, 10, 10, 0.95);
  border: 1px solid rgba(0, 245, 255, 0.3);
  border-radius: 12px;
  padding: 30px;
  color: #00f5ff;
  font-family: 'Orbitron', sans-serif;
  width: 90%;
  max-width: 600px;
  box-shadow: 0 0 20px rgba(0, 245, 255, 0.3);
}

.chart-area {
  margin-top: 20px;
  text-align: left;
}

.fake-chart {
  width: 100%;
  height: 120px;
  background: linear-gradient(90deg, rgba(0,245,255,0.15), rgba(255,255,255,0.05));
  border-radius: 8px;
  margin: 8px 0 20px;
}

.close-btn {
  margin-top: 20px;
  padding: 8px 20px;
  background: rgba(0,245,255,0.15);
  border: 1px solid rgba(0,245,255,0.4);
  color: #00f5ff;
  border-radius: 6px;
  cursor: pointer;
}
.close-btn:hover {
  background: rgba(0,245,255,0.25);
}
</style>
