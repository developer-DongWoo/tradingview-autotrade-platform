<template>
  <div class="intro">
    <h1>🧠 Predator Market Overview</h1>
    <div class="tile-grid">
      <OptionTile 
        v-for="(asset, i) in assets" 
        :key="i" 
        v-bind="asset" 
        @openModal="openModal" 
      />
    </div>

    <OptionDetailModal 
      v-if="showModal" 
      :name="selectedName" 
      @close="showModal = false" 
    />

    <p class="ai-comment">AI 엔진이 8개 주요 자산의 옵션 데이터를 분석했습니다.</p>

    <button class="cta" @click="goConsole">
      내 포트폴리오 분석 보기 →
    </button>
  </div>
</template>

<script setup>
import { ref } from "vue"
import { useRouter } from "vue-router"
import OptionTile from "@/components/widgets/OptionTile.vue"
import OptionDetailModal from "@/components/widgets/OptionDetailModal.vue"

// ✅ Router
const router = useRouter()
const goConsole = () => router.push("/option-console")

// ✅ Modal 상태
const showModal = ref(false)
const selectedName = ref("")

const openModal = (name) => {
  selectedName.value = name
  showModal.value = true
}

// ✅ 자산 데이터
const assets = [
  { name: "S&P500", putCallRatio: 0.72, iv: 18.3, oiDelta: 2.4, trend: "중립" },
  { name: "NASDAQ100", putCallRatio: 0.65, iv: 20.1, oiDelta: 3.8, trend: "상승" },
  { name: "DOW JONES", putCallRatio: 0.78, iv: 16.5, oiDelta: -0.9, trend: "중립" },
  { name: "RUSSELL2000", putCallRatio: 0.89, iv: 24.2, oiDelta: 1.2, trend: "하락" },
  { name: "KOSPI200", putCallRatio: 0.83, iv: 22.5, oiDelta: 4.7, trend: "하락" },
  { name: "KOSDAQ150", putCallRatio: 0.69, iv: 26.1, oiDelta: 2.9, trend: "상승" },
  { name: "VIX", putCallRatio: 1.05, iv: 15.2, oiDelta: -3.5, trend: "하락" },
  { name: "GOLD", putCallRatio: 0.75, iv: 12.9, oiDelta: 1.8, trend: "상승" },
]
</script>

<style scoped>
.intro {
  min-height: 100vh;
  background: radial-gradient(circle at center, #000 0%, #050505 100%);
  color: #00f5ff;
  text-align: center;
  font-family: 'Orbitron', sans-serif;
  padding: 60px 20px;
}
.tile-grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 18px;
  margin-bottom: 40px;
  width: 100%;
  max-width: 1500px;
  margin-left: auto;
  margin-right: auto;
}
.ai-comment {
  margin-bottom: 30px;
  color: #00f5ffcc;
  font-size: 14px;
}
.cta {
  background: linear-gradient(145deg, #00f5ff30, #00f5ff10);
  border: 1px solid rgba(0, 245, 255, 0.4);
  color: #00f5ff;
  padding: 12px 30px;
  border-radius: 10px;
  cursor: pointer;
  font-size: 16px;
  transition: all 0.3s ease;
}
.cta:hover {
  background: linear-gradient(145deg, #00f5ff50, #00f5ff20);
  box-shadow: 0 0 20px rgba(0, 245, 255, 0.3);
}
@media (max-width: 700px) {
  .tile-grid { gap: 12px; }
}
</style>
