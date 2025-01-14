// src/frontend/src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import ChatView from '../views/ChatView.vue'
import AnalyticsView from '../views/AnalyticsView.vue'

const routes = [
  { path: '/', name: 'Chat', component: ChatView },
  { path: '/analytics', name: 'Analytics', component: AnalyticsView }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
