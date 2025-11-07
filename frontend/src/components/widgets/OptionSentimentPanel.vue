<template>
  <div class="option-panel">
    <h3>🎯 Option Market Sentiment</h3>

    <div class="metric">
      <span>📊 Put / Call Ratio:</span>
      <strong :class="getRatioColor(ratio)">{{ ratio }}</strong>
    </div>

    <div class="metric">
      <span>💥 OI Concentration:</span>
      <strong>{{ callZone }}~{{ putZone }}</strong>
    </div>

    <div class="metric">
      <span>🌡️ IV Index:</span>
      <strong :class="getIVColor(iv)">{{ iv }}%</strong>
    </div>

    <div class="comment">
      <p>{{ aiComment }}</p>
    </div>
  </div>
</template>

<script setup>
const ratio = 0.72 // 예시: 현재 풋콜비율
const callZone = 4700 // 콜 집중 구간
const putZone = 4300 // 풋 집중 구간
const iv = 18.3 // 변동성 인덱스
const aiComment = "콜옵션 매수세가 단기 과열되고 있습니다."

// 색상 매핑 함수
const getRatioColor = (r) => {
  if (r > 0.8) return "bearish"
  if (r < 0.6) return "bullish"
  return "neutral"
}

const getIVColor = (v) => {
  if (v > 25) return "hot"
  if (v < 15) return "cool"
  return "normal"
}
</script>

<style scoped>
.option-panel {
  background: rgba(0, 0, 0, 0.4);
  border: 1px solid rgba(0, 245, 255, 0.25);
  border-radius: 12px;
  padding: 20px;
  color: #00f5ff;
  font-family: 'Orbitron', sans-serif;
  width: 280px;
  text-align: left;
  box-shadow: 0 0 15px rgba(0, 245, 255, 0.1);
}

h3 {
  color: #00f5ff;
  text-align: center;
  margin-bottom: 15px;
}

.metric {
  display: flex;
  justify-content: space-between;
  margin-bottom: 10px;
  font-size: 15px;
}

.metric strong {
  font-weight: bold;
}

.bullish {
  color: #00ffae;
}
.bearish {
  color: #ff004c;
}
.neutral {
  color: #ffcc00;
}
.hot {
  color: #ff6b00;
}
.cool {
  color: #00c2ff;
}
.normal {
  color: #b0b0b0;
}

.comment {
  margin-top: 15px;
  font-size: 14px;
  color: #00f5ffcc;
  text-align: center;
  border-top: 1px solid rgba(0, 245, 255, 0.1);
  padding-top: 10px;
}
</style>
