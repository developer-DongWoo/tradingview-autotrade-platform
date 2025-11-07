<template>
  <div class="settings-page">
    <h1>⚙️ 시스템 설정</h1>
    <p>여기서 사용자 환경, 알림, 테마 등을 설정할 수 있습니다.</p>

    <div class="settings-box">
      <label>
        <span>테마 선택</span>
        <select v-model="theme">
          <option value="dark">다크 모드</option>
          <option value="light">라이트 모드</option>
        </select>
      </label>

      <label>
        <span>알림</span>
        <input type="checkbox" v-model="notifications" />
        <span>활성화</span>
      </label>
    </div>

    <button @click="saveSettings">저장</button>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const theme = ref('dark')
const notifications = ref(true)

const saveSettings = () => {
  console.log('설정 저장됨:', {
    theme: theme.value,
    notifications: notifications.value,
  })
  alert('✅ 설정이 저장되었습니다.')
}
</script>

<style scoped>
.settings-page {
  color: #00f5ff;
  font-family: 'Rajdhani', sans-serif;
  padding: 40px;
}
h1 {
  font-family: 'Orbitron', sans-serif;
  color: #00f5ff;
  margin-bottom: 20px;
}
.settings-box {
  display: flex;
  flex-direction: column;
  gap: 15px;
  margin-bottom: 20px;
}
label {
  display: flex;
  align-items: center;
  gap: 10px;
}
select,
input[type='checkbox'] {
  background: #101010;
  border: 1px solid rgba(0, 245, 255, 0.3);
  color: #00f5ff;
  padding: 5px;
  border-radius: 6px;
}
button {
  background: linear-gradient(145deg, #00f5ff30, #00f5ff10);
  border: 1px solid rgba(0, 245, 255, 0.4);
  color: #00f5ff;
  padding: 8px 16px;
  border-radius: 8px;
  cursor: pointer;
  font-weight: bold;
}
button:hover {
  background: linear-gradient(145deg, #00f5ff40, #00f5ff20);
}
</style>
