<template>
  <div class="dashboard-panel">
    <h3 class="title">{{ title }}</h3>
    <div class="content">
      <slot />
    </div>
  </div>
</template>

<script setup>
defineProps({
  title: { type: String, default: 'Untitled Panel' },
})
</script>

<style scoped>
.dashboard-panel {
  background: linear-gradient(145deg, #101010, #1a1a1a);
  border: 1px solid rgba(0, 245, 255, 0.2);
  border-radius: 10px;
  padding: 20px;
  color: #e0e0e0;
  box-shadow:
    0 0 12px rgba(0, 245, 255, 0.15),
    inset 0 0 8px rgba(255, 255, 255, 0.05);
  transition: all 0.2s ease;
}
.dashboard-panel:hover {
  transform: translateY(-2px);
  box-shadow:
    0 0 18px rgba(0, 245, 255, 0.25),
    inset 0 0 10px rgba(0, 245, 255, 0.1);
}
.title {
  font-family: 'Orbitron', sans-serif;
  font-size: 18px;
  color: #00f5ff;
  margin-bottom: 12px;
  border-bottom: 1px solid rgba(0, 245, 255, 0.15);
  padding-bottom: 4px;
}
.content {
  margin-top: 10px;
}
</style>
