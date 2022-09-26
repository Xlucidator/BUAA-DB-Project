import { createRouter, createWebHistory } from 'vue-router'
// 开启历史模式
// vue2中使用的mode：history 实现
const routes = [
  {
    path: '/',
    redirect: '/home' // 重定向到home页面
  },
  {
    path: '/home',
    component: () => import('../views/HelloWorld.vue') // 在src文件夹下新建的views文件夹，用于存放各个页面
  },
  {
    path: '/login',
    component: () => import('../views/login.vue')
  },
  {
    path: '/404',
    component: () => import('../views/404.vue')
  }
]
const router = createRouter(
  {
    history: createWebHistory(),
    routes
  }
)

export default router

