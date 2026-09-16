<template>
  <van-tabbar v-model="active" route>
    <van-tabbar-item v-if="admin" to="/knowledge">
      <span>知识库</span>
      <template #icon>
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/>
          <line x1="12" y1="11" x2="12" y2="17"/>
          <line x1="9" y1="14" x2="15" y2="14"/>
        </svg>
      </template>
    </van-tabbar-item>
    <van-tabbar-item to="/chat">
      <span>AI助手</span>
      <template #icon>
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
          <line x1="9" y1="10" x2="15" y2="10"/>
          <line x1="12" y1="7" x2="12" y2="13"/>
        </svg>
      </template>
    </van-tabbar-item>
    <van-tabbar-item to="/my">
      <span>我的</span>
      <template #icon>
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
          <circle cx="12" cy="7" r="4"/>
        </svg>
      </template>
    </van-tabbar-item>
  </van-tabbar>
</template>

<script setup>
/**
 * TabBar 底部导航栏 —— 管理员(test) 3 个 Tab：知识库、AI助手、我的；
 * 普通用户 2 个 Tab（知识库管理功能仅管理员可用）。
 * 配合 Vue Router 的 route 属性实现页面切换。
 */
import { ref, watch } from 'vue'
import { useRoute } from 'vue-router'
import { isAdminUser } from '../utils/permission'

const route = useRoute()
// 管理员状态用 ref：本组件随 keep-alive 页面缓存，需在路由变化时重判
// （isAdminUser 读 localStorage 非响应式，登出/切换用户后靠 watcher 刷新）
const admin = ref(isAdminUser())
const active = ref(0)

function setActiveTab() {
  admin.value = isAdminUser()
  const path = route.path
  let section = ''
  if (path.includes('/knowledge')) {
    section = '/knowledge'
  } else if (path.includes('/chat') || path.includes('/aichat')) {
    section = '/chat'
  } else if (path.includes('/my')) {
    section = '/my'
  }

  // 与模板中可见 tab 的顺序对应（知识库 tab 仅管理员可见，索引随之变化）
  const tabs = admin.value ? ['/knowledge', '/chat', '/my'] : ['/chat', '/my']
  const idx = tabs.indexOf(section)
  if (idx >= 0) {
    active.value = idx
  }
}

setActiveTab()

watch(() => route.path, () => {
  setActiveTab()
})
</script>
