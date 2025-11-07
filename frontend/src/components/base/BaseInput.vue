<template>
  <div class="input-wrapper">
    <label v-if="label" class="label">{{ label }}</label>
    <input
      v-bind="$attrs"
      class="base-input"
      :value="modelValue"
      @input="$emit('update:modelValue', $event.target.value)"
    />
  </div>
</template>

<script setup>
defineProps({
  label: String,
  modelValue: [String, Number],
})
defineEmits(['update:modelValue'])
</script>

<style scoped>
.input-wrapper {
  display: flex;
  flex-direction: column;
  gap: 6px;
  font-family: 'Rajdhani', sans-serif;
}

.label {
  font-size: 14px;
  color: rgba(255, 255, 255, 0.6);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.base-input {
  background: #111;
  border: 1px solid rgba(0, 245, 255, 0.2);
  border-radius: 6px;
  padding: 10px 12px;
  color: #00f5ff;
  outline: none;
  transition: all 0.25s ease;
}

.base-input:focus {
  border-color: rgba(0, 245, 255, 0.5);
  box-shadow: 0 0 10px rgba(0, 245, 255, 0.3);
  background: linear-gradient(145deg, #0f0f0f, #1b1b1b);
}
</style>
