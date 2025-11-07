<template>
  <div class="base-card">
    <slot />
  </div>
</template>

<script setup></script>

<style scoped>
.base-card {
  background: linear-gradient(145deg, #0f0f0f, #1a1a1a);
  border: 1px solid rgba(0, 245, 255, 0.15);
  border-radius: 12px;
  box-shadow:
    0 0 25px rgba(0, 245, 255, 0.08),
    inset 0 0 12px rgba(255, 255, 255, 0.05);
  padding: 24px;
  color: #d4d4d4;
  font-family: 'Rajdhani', sans-serif;
  transition: all 0.3s ease;
}

.base-card:hover {
  border-color: rgba(0, 245, 255, 0.3);
  box-shadow:
    0 0 30px rgba(0, 245, 255, 0.2),
    inset 0 0 12px rgba(0, 245, 255, 0.1);
}
</style>
