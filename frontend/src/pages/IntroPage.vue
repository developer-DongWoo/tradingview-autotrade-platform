<template>
  <div class="intro">
    <h1>🧠 Predator Market Overview</h1>
    <p class="subtitle">AI 기반 옵션 심리 분석</p>

    <div class="tile-grid">
      <OptionTile name="S&P500" :putCallRatio="0.72" :iv="18.3" trend="중립" />
      <OptionTile name="NASDAQ100" :putCallRatio="0.65" :iv="20.1" trend="상승" />
      <OptionTile name="KOSPI200" :putCallRatio="0.83" :iv="22.5" trend="하락" />
      <OptionTile name="VIX" :putCallRatio="1.05" :iv="15.2" trend="하락" />
    </div>

    <p class="ai-comment">AI 엔진이 4개 주요 지수의 옵션 데이터를 분석했습니다.</p>

    <button class="cta" @click="goConsole">
      내 포트폴리오 분석 보기 →
    </button>
  </div>
</template>

<script setup>
import { useRouter } from "vue-router"
import OptionTile from "@/components/widgets/OptionTile.vue"

const router = useRouter()
const goConsole = () => router.push("/option-console")
</script>

<style scoped>
.intro {
  min-height: 100vh;
  background: radial-gradient(circle at center, #000 0%, #0a0a0a 100%);
  color: #00f5ff;
  text-align: center;
  font-family: 'Orbitron', sans-serif;
  padding: 60px 20px;
}
.subtitle {
  color: #00f5ffb0;
  margin-bottom: 40px;
}
.tile-grid {
  display: flex;
  flex-wrap: wrap; /* ✅ grid → flex로 변경 */
  justify-content: center; /* ✅ 항상 중앙 정렬 */
  gap: 20px; /* ✅ 간격 일정하게 유지 */
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
</style>
