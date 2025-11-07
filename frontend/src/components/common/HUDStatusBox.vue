<template>
  <div class="hud-box">
    <h4 class="label">{{ label }}</h4>
    <p class="value">{{ value }}</p>
  </div>
</template>

<script setup>
defineProps({
  label: String,
  value: [String, Number],
})
</script>

<style scoped>
.hud-box {
  background: linear-gradient(145deg, #101010, #1a1a1a);
  border: 1px solid rgba(0, 245, 255, 0.2);
  border-radius: 8px;
  padding: 16px 20px;
  min-width: 160px;
  box-shadow:
    0 0 10px rgba(0, 245, 255, 0.15),
    inset 0 0 8px rgba(255, 255, 255, 0.05);
  transition: all 0.3s ease;
}
.hud-box:hover {
  box-shadow:
    0 0 20px rgba(0, 245, 255, 0.3),
    inset 0 0 10px rgba(0, 245, 255, 0.1);
  transform: translateY(-2px);
}
.label {
  font-size: 13px;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: rgba(255, 255, 255, 0.55);
  margin-bottom: 4px;
}
.value {
  font-family: 'Orbitron', sans-serif;
  font-size: 22px;
  color: #00f5ff;
}
</style>
