<template>
  <div v-if="isOpen" class="modal-overlay" @click.self="$emit('close')">
    <div class="modal-content">
      <header class="modal-header">
        <h2>{{ title }}</h2>
        <button class="close-btn" @click="$emit('close')">✕</button>
      </header>
      <div class="modal-body">
        <slot />
      </div>
      <footer class="modal-footer">
        <slot name="footer" />
      </footer>
    </div>
  </div>
</template>

<script setup>
defineProps({
  isOpen: Boolean,
  title: String,
})
defineEmits(['close'])
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(10, 10, 10, 0.85);
  backdrop-filter: blur(4px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal-content {
  width: 420px;
  background: linear-gradient(145deg, #0e0e0e, #181818);
  border: 1px solid rgba(0, 245, 255, 0.25);
  border-radius: 10px;
  box-shadow:
    0 0 40px rgba(0, 245, 255, 0.25),
    inset 0 0 20px rgba(0, 245, 255, 0.08);
  color: #e0e0e0;
  padding: 20px;
  font-family: 'Orbitron', 'Rajdhani', sans-serif;
  position: relative;
  animation: fadeIn 0.3s ease;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid rgba(0, 245, 255, 0.15);
  margin-bottom: 12px;
  padding-bottom: 8px;
}

.modal-header h2 {
  font-size: 18px;
  color: #00f5ff;
}

.modal-body {
  margin: 16px 0;
  line-height: 1.6;
}

.close-btn {
  background: transparent;
  border: none;
  color: rgba(255, 255, 255, 0.5);
  font-size: 18px;
  cursor: pointer;
  transition: color 0.2s ease;
}
.close-btn:hover {
  color: #00f5ff;
}

.modal-footer {
  display: flex;
  justify-content: flex-end;
  gap: 8px;
  border-top: 1px solid rgba(0, 245, 255, 0.1);
  padding-top: 8px;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: scale(0.97);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}
</style>
