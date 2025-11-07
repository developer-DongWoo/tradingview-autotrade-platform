<template>
  <div class="login-form">
    <h2>Predator Console 로그인</h2>

    <BaseInput label="ID" v-model="id" />
    <BaseInput label="Password" type="password" v-model="password" />

    <BaseButton class="mt-3" @click="login">접속</BaseButton>
  </div>
</template>

<script setup>
import { ref } from "vue"
import { useRouter } from "vue-router"
import BaseInput from "@/components/base/BaseInput.vue"
import BaseButton from "@/components/base/BaseButton.vue"

const router = useRouter()
const id = ref("")
const password = ref("")

const login = () => {
  if (id.value && password.value) {
    router.push("/dashboard") // ✅ 로그인 성공 시 대시보드 이동
  } else {
    alert("아이디와 비밀번호를 입력하세요.")
  }
}
</script>

<style scoped>
.login-form {
  display: flex;
  flex-direction: column;
  gap: 14px;
  padding: 40px;
  background: linear-gradient(145deg, #101010, #1a1a1a);
  border: 1px solid rgba(0, 245, 255, 0.2);
  border-radius: 12px;
  box-shadow:
    0 0 20px rgba(0, 245, 255, 0.2),
    inset 0 0 10px rgba(255, 255, 255, 0.05);
  color: #00f5ff;
  width: 340px;
  margin: 0 auto;
  font-family: "Rajdhani", sans-serif;
}
h2 {
  text-align: center;
  font-family: "Orbitron", sans-serif;
  margin-bottom: 10px;
}
</style>
