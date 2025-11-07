<template>
  <div class="auth-layout">
    <div class="auth-box">
      <slot />
    </div>
  </div>
</template>

<script setup></script>

<style scoped>
.auth-layout {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background: radial-gradient(circle at center, #0d0d0d 0%, #000 100%);
}

.auth-box {
  background: linear-gradient(145deg, #101010, #1b1b1b);
  border: 1px solid rgba(0, 245, 255, 0.3);
  border-radius: 12px;
  padding: 40px;
  box-shadow:
    0 0 20px rgba(0, 245, 255, 0.1),
    inset 0 0 10px rgba(255, 255, 255, 0.05);
}
</style>
