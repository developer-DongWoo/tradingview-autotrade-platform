<template>
  <div class="option-tile">
    <h3>{{ name }}</h3>
    <p class="ratio" :style="{ color: ratioColor }">
      📊 Put/Call Ratio: {{ putCallRatio }}
    </p>
    <p>IV: {{ iv }}%</p>
    <p>📈 추세: {{ trend }}</p>
  </div>
</template>

<script setup>
import { computed } from "vue"  // ✅ 반드시 세미콜론 포함

const props = defineProps({
  name: String,
  putCallRatio: Number,
  iv: Number,
  trend: String,
});

const ratioColor = computed(() => {
  if (props.putCallRatio > 1) return "#ff003c"; // 하락 우위
  if (props.putCallRatio < 0.8) return "#00f5ff"; // 상승 우위
  return "#ffaa00"; // 중립
});
</script>

<style scoped>
.option-tile {
  background: linear-gradient(145deg, #0a0a0a, #000);
  border: 1px solid rgba(0, 245, 255, 0.4); /* ✅ 테두리 더 진하게 */
  border-radius: 12px;
  padding: 20px;
  text-align: center;
  width: 100%; /* ✅ 고정폭 대신 부모 grid에 맞게 */
  max-width: 260px; /* ✅ 너무 넓어지지 않게 제한 */
  box-shadow: 0 0 15px rgba(0, 245, 255, 0.15); /* ✅ 은은한 네온 효과 */
  transition: all 0.3s ease;
}

.option-tile:hover {
  transform: scale(1.03);
  box-shadow: 0 0 25px rgba(0, 245, 255, 0.4); /* ✅ hover시 빛 확산 */
  border-color: rgba(0, 245, 255, 0.8);
}

h3 {
  color: #00f5ff;
  margin-bottom: 10px;
  font-size: 18px;
  letter-spacing: 0.5px;
}

p {
  color: #fff;
  margin: 5px 0;
}

.ratio {
  font-weight: bold;
}
</style>


