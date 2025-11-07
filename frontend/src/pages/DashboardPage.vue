<template>
  <DashboardLayout>
    <div class="dashboard">
      <section class="status-section">
        <MetricCard title="GPU 온도" unit="°C" :data="gpuData" />
        <MetricCard title="CPU 사용률" unit="%" :data="cpuData" />
        <MetricCard title="트래픽" unit="Mbps" :data="netData" />
      </section>

      <section class="feed-section">
        <h3 class="section-title">시스템 로그</h3>
        <ActivityFeed />
      </section>
    </div>
  </DashboardLayout>
</template>

<script setup>
import DashboardLayout from '@/components/layout/DashboardLayout.vue'
import MetricCard from '@/components/widgets/MetricCard.vue'
import ActivityFeed from '@/components/widgets/ActivityFeed.vue'
import { ref, onMounted } from 'vue'

const gpuData = ref([])
const cpuData = ref([])
const netData = ref([])

// 임시 데이터 시뮬레이션
const generateData = () =>
  Array.from({ length: 20 }, (_, i) => ({
    time: i,
    value: Math.floor(Math.random() * 100),
  }))

onMounted(() => {
  gpuData.value = generateData()
  cpuData.value = generateData()
  netData.value = generateData()

  setInterval(() => {
    gpuData.value.push({ time: Date.now(), value: Math.random() * 100 })
    gpuData.value.shift()
    cpuData.value.push({ time: Date.now(), value: Math.random() * 100 })
    cpuData.value.shift()
    netData.value.push({ time: Date.now(), value: Math.random() * 300 })
    netData.value.shift()
  }, 2000)
})
</script>

<style scoped>
.dashboard {
  display: flex;
  flex-direction: column;
  gap: 40px;
}
.status-section {
  display: flex;
  gap: 20px;
  flex-wrap: wrap;
}
.section-title {
  color: #00f5ff;
  font-family: 'Orbitron', sans-serif;
  margin-bottom: 12px;
}
</style>
