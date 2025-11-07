<template>
  <div 
    class="option-tile" 
    :style="{ backgroundColor: boxColor, borderColor: borderColor }"
    @click="emit('openModal', name)"
  >
    <h3>{{ name }}</h3>
    <p class="ratio">📊 Put/Call Ratio: {{ putCallRatio }}</p>
    <p>IV: {{ iv }}%</p>
    <p>OI Δ: 
      <span :class="oiDelta >= 0 ? 'positive' : 'negative'">
        {{ oiDelta > 0 ? '+' : '' }}{{ oiDelta }}%
      </span>
    </p>
    <p>📈 추세: {{ trend }}</p>
  </div>
</template>

<script setup>
import { computed } from "vue"

const props = defineProps({
  name: String,
  putCallRatio: Number,
  iv: Number,
  oiDelta: Number,
  trend: String,
})

const emit = defineEmits(["openModal"])

const boxColor = computed(() => {
  const ratio = props.putCallRatio
  if (ratio > 1.0) return "rgba(255, 0, 60, 0.15)"
  if (ratio < 0.8) return "rgba(0, 245, 255, 0.15)"
  return "rgba(255, 200, 0, 0.08)"
})

const borderColor = computed(() => {
  const ratio = props.putCallRatio
  if (ratio > 1.0) return "rgba(255, 0, 60, 0.6)"
  if (ratio < 0.8) return "rgba(0, 245, 255, 0.6)"
  return "rgba(255, 200, 0, 0.4)"
})
</script>

<style scoped>
.option-tile {
  border: 1.5px solid rgba(0, 245, 255, 0.3);
  border-radius: 12px;
  padding: 20px;
  text-align: center;
  width: 250px;
  box-shadow: 0 0 12px rgba(0, 245, 255, 0.1);
  transition: all 0.3s ease;
  backdrop-filter: blur(3px);
  animation: fadeUp 0.8s ease forwards;
  cursor: pointer;
}
.option-tile:hover {
  transform: scale(1.04);
  box-shadow: 0 0 25px rgba(0, 245, 255, 0.3);
}
</style>
