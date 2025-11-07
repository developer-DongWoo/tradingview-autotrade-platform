<template>
  <div class="activity-feed">
    <div v-for="(item, i) in items" :key="i" class="feed-item">
      <div class="dot"></div>
      <span class="time">{{ item.time }}</span>
      <span class="desc">{{ item.desc }}</span>
    </div>
  </div>
</template>

<script setup>
const items = [
  { time: '14:05', desc: '시스템 진단 완료' },
  { time: '13:50', desc: '데이터 동기화 성공' },
  { time: '13:32', desc: '보안 로그 업데이트' },
]
</script>

<style scoped>
.activity-feed {
  display: flex;
  flex-direction: column;
  gap: 8px;
  font-family: 'Rajdhani', sans-serif;
}

.feed-item {
  display: flex;
  align-items: center;
  gap: 10px;
  background: linear-gradient(145deg, #0f0f0f, #181818);
  padding: 10px 12px;
  border-radius: 6px;
  border: 1px solid rgba(0, 245, 255, 0.1);
  transition: all 0.2s ease;
}
.feed-item:hover {
  border-color: rgba(0, 245, 255, 0.3);
}
.dot {
  width: 6px;
  height: 6px;
  background: #00f5ff;
  border-radius: 50%;
  box-shadow: 0 0 8px rgba(0, 245, 255, 0.8);
}
.time {
  font-size: 13px;
  color: #00f5ff;
  width: 50px;
}
.desc {
  font-size: 14px;
  color: rgba(255, 255, 255, 0.8);
}
</style>
