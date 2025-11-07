<template>
  <button
    class="base-button"
    :class="[variant, { disabled }]"
    :disabled="disabled"
  >
    <slot />
  </button>
</template>

<script setup>
defineProps({
  variant: {
    type: String,
    default: 'primary', // 'primary', 'secondary', 'danger'
  },
  disabled: {
    type: Boolean,
    default: false,
  },
})
</script>

<style scoped>
.base-button {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 12px 24px;
  font-family: 'Orbitron', 'Rajdhani', sans-serif;
  font-size: 15px;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: #00f5ff;
  background: linear-gradient(145deg, #0d0d0d, #1a1a1a);
  border: 1px solid rgba(0, 245, 255, 0.2);
  border-radius: 8px;
  box-shadow:
    0 0 10px rgba(0, 245, 255, 0.3),
    inset 0 0 8px rgba(0, 245, 255, 0.1);
  transition: all 0.25s ease;
  overflow: hidden;
  cursor: pointer;
}

/* 네온 테두리 효과 */
.base-button::before {
  content: '';
  position: absolute;
  inset: 0;
  border: 1px solid rgba(0, 245, 255, 0.35);
  border-radius: inherit;
  filter: blur(3px);
  opacity: 0;
  transition: opacity 0.3s ease;
}

/* hover 시 네온 강화 */
.base-button:hover::before {
  opacity: 1;
}
.base-button:hover {
  color: #0ff;
  border-color: rgba(0, 245, 255, 0.6);
  box-shadow:
    0 0 18px rgba(0, 245, 255, 0.5),
    inset 0 0 8px rgba(0, 245, 255, 0.2);
  transform: translateY(-2px);
}

/* 클릭 시 반응 */
.base-button:active {
  transform: translateY(0);
  box-shadow:
    0 0 5px rgba(0, 245, 255, 0.5),
    inset 0 0 5px rgba(0, 245, 255, 0.3);
}

/* variant 색상 */
.primary {
  color: #00f5ff;
}
.secondary {
  color: #a0a0a0;
  border-color: rgba(160, 160, 160, 0.3);
  box-shadow: 0 0 8px rgba(160, 160, 160, 0.2);
}
.danger {
  color: #ff3c3c;
  border-color: rgba(255, 60, 60, 0.4);
  box-shadow: 0 0 8px rgba(255, 60, 60, 0.3);
}

/* 비활성화 */
.disabled,
.base-button:disabled {
  opacity: 0.4;
  cursor: not-allowed;
  box-shadow: none;
  border-color: rgba(255, 255, 255, 0.1);
}
</style>
