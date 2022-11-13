import {createRouter, createWebHistory} from 'vue-router'
// 开启历史模式
// vue2中使用的mode：history 实现
const routes = [
    {
        path: '/',
        redirect: '/home', // 重定向到home页面
        meta: { transition: 'slide-left' },
    },
    {
        path: '/home',
        component: () => import('../views/HelloWorld.vue'), // 在src文件夹下新建的views文件夹，用于存放各个页面
        meta: { transition: 'slide-left' },},
    {
        path: '/login',
        component: () => import('../views/login.vue'),
        meta: { transition: 'slide-left' },
    },
    {
        path: '/register',
        component: () => import('../views/register.vue'),
        meta: { transition: 'slide-left' },
    },
    {
        path: '/settings',
        component: () => import('../views/settings.vue'),
        meta: { transition: 'slide-left' },
    },
    {
        path: '/announcements',
        component: () => import('../views/announcements.vue'),
        meta: { transition: 'slide-left' },
    },
    {
        //path:'/announcements/:id',
        path: '/singlePage',
        component: () => import('../views/singlePage.vue'),
        meta: { transition: 'slide-left' },
    },
    {
        path: '/:pathMatch(.*)*',
        component: () => import('../views/404.vue'),
        meta: { transition: 'slide-left' },
    }
]
const router = createRouter(
    {
        history: createWebHistory(),
        routes,
        scrollBehavior(to, from, savedPosition) {
            if (savedPosition) {
                return savedPosition
            } else {
                return {top: 0}
            }
        }
    },
)

export default router

