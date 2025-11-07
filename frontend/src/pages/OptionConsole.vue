<template>
  <div class="option-console">
    <h1>🧠 Predator Option Console</h1>
    <p class="subtitle">시장의 심리를 데이터로 읽다</p>

    <div class="summary">
      <OptionSentimentPanel />
    </div>

    <div class="charts">
      <PutCallGauge />
      <OIDistributionChart />
      <IVSmileChart />
      <IVTermStructure />
      <VolumeFlowChart />
    </div>
  </div>
</template>

<script setup>
import OptionSentimentPanel from "@/components/widgets/OptionSentimentPanel.vue"
import PutCallGauge from "@/components/widgets/PutCallGauge.vue"
import OIDistributionChart from "@/components/widgets/OIDistributionChart.vue"
import IVSmileChart from "@/components/widgets/IVSmileChart.vue"
import IVTermStructure from "@/components/widgets/IVTermStructure.vue"
import VolumeFlowChart from "@/components/widgets/VolumeFlowChart.vue"
</script>

<style scoped>
.option-console {
  min-height: 100vh;
  background: radial-gradient(circle at center, #000 0%, #0a0a0a 100%);
  color: #00f5ff;
  text-align: center;
  font-family: 'Orbitron', sans-serif;
  padding: 40px 20px;
}
.subtitle {
  color: #00f5ffb0;
  font-size: 16px;
  margin-bottom: 40px;
}
.summary {
  margin-bottom: 40px;
  display: flex;
  justify-content: center;
}
.charts {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
  gap: 30px;
  justify-items: center;
}
</style>
