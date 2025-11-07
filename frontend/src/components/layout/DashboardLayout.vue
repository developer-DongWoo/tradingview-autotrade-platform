<template>
  <div class="layout">
    <aside class="sidebar">
      <h1 class="logo">PREDATOR<span>SYS</span></h1>
      <nav>
        <a href="#" class="nav-item active">대시보드</a>
        <a href="#" class="nav-item">로그</a>
        <a href="#" class="nav-item">설정</a>
      </nav>
    </aside>

    <main class="main">
      <slot />
    </main>
  </div>
</template>

<script setup></script>

<style scoped>
.layout {
  display: flex;
  height: 100vh;
  background: linear-gradient(145deg, #0a0a0a, #121212);
  color: #e0e0e0;
  font-family: 'Rajdhani', sans-serif;
}

.sidebar {
  width: 220px;
  background: linear-gradient(180deg, #0d0d0d, #151515);
  border-right: 1px solid rgba(0, 245, 255, 0.15);
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 24px 0;
}

.logo {
  font-family: 'Orbitron', sans-serif;
  color: #00f5ff;
  font-size: 22px;
  margin-bottom: 40px;
}
.logo span {
  color: #ff003c;
}

.nav-item {
  display: block;
  width: 80%;
  text-align: center;
  padding: 10px 0;
  margin: 6px 0;
  color: rgba(255, 255, 255, 0.6);
  border: 1px solid transparent;
  border-radius: 6px;
  transition: all 0.2s ease;
}
.nav-item:hover {
  color: #00f5ff;
  border-color: rgba(0, 245, 255, 0.2);
}
.active {
  background: linear-gradient(145deg, #00f5ff20, #00f5ff10);
  color: #00f5ff;
  border-color: rgba(0, 245, 255, 0.25);
}

.main {
  flex: 1;
  padding: 32px;
  overflow-y: auto;
}
</style>
