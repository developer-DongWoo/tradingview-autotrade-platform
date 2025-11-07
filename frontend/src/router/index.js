import { createRouter, createWebHistory } from "vue-router"

// 페이지 import
import IntroPage from "@/pages/IntroPage.vue"
import LoginPage from "@/pages/LoginPage.vue"
import OptionConsole from "@/pages/OptionConsole.vue" // ✅ 추가

const routes = [
  { path: "/", name: "Intro", component: IntroPage },
  { path: "/login", name: "Login", component: LoginPage },
  { path: "/option-console", name: "OptionConsole", component: OptionConsole } // ✅ 추가
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
