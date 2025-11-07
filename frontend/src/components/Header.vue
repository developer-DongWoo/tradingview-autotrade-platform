<template>
  <header class="bg-gray-900 text-white py-3 px-6 flex justify-between items-center">
    <h1 class="text-xl font-bold">동우의 플랫폼</h1>

    <nav class="space-x-4">
      <RouterLink to="/" class="hover:underline">홈</RouterLink>
      <RouterLink to="/board" class="hover:underline">게시판</RouterLink>
      <RouterLink to="/login" class="hover:underline">로그인</RouterLink>
    </nav>
  </header>
</template>
