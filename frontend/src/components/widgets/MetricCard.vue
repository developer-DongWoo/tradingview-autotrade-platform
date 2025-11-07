<template>
  <div class="metric-card">
    <div class="metric-header">
      <h4>{{ title }}</h4>
      <span class="value">{{ latestValue }} {{ unit }}</span>
    </div>

    <ResponsiveContainer width="100%" height="100%">
      <LineChart :data="data">
        <defs>
          <linearGradient id="neonLine" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#00f5ff" stop-opacity="0.9" />
            <stop offset="100%" stop-color="#00f5ff" stop-opacity="0.1" />
          </linearGradient>
        </defs>

        <Line
          type="monotone"
          dataKey="value"
          stroke="url(#neonLine)"
          stroke-width="2.5"
          dot="false"
          isAnimationActive="true"
        />
      </LineChart>
    </ResponsiveContainer>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { LineChart, Line, ResponsiveContainer } from 'recharts'

const props = defineProps({
  title: String,
  unit: { type: String, default: '' },
  data: { type: Array, default: () => [] },
})

const latestValue = computed(() => {
  if (!props.data.length) return 0
  return props.data[props.data.length - 1].value
})
</script>
