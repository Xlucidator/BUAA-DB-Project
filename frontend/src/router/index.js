import {createRouter, createWebHistory} from 'vue-router'
import GlobalLayout from '../views/main/index.vue'

const routes = [
    {
        path: '/',
        redirect: '/main' // 重定向到home页面
    },
    {
        path: '/login',
        name: 'login',
        component: () => import('../views/authority/login.vue')
    },
    {
        path: '/register',
        name: 'register',
        component: () => import('../views/authority/register.vue')
    },
    {
        path: '/main',
        name: 'main',
        component: GlobalLayout,
        redirect: '/main/home',
        children: [
            {
                path: 'home',       // -> '/main/home/'
                name: 'home',
                component: () => import('../views/main/home.vue')
            },
            {
                path: 'bulletin',   // -> '/main/bulletin/'
                name: 'bulletin',
                component: () => import('../views/main/bulletin/announcements.vue')
            },
            {
                path: 'bulletin/singlePage/:id',
                name: 'bulletin/singlePage/:id',
                component: () => import('../views/main/bulletin/singlePage.vue'),
            },
            {
                path: 'bulletin/singlePage/home',
                name: 'bulletin/singlePage/home',
                redirect: '/main/home',
            },
            {
                path: 'bulletin/singlePage/message',
                name: 'bulletin/singlePage/message',
                redirect: '/main/message',
            },
            {
                path: 'bulletin/singlePage/bulletin',
                name: 'bulletin/singlePage/bulletin',
                redirect: '/main/bulletin',
            },
            {
                path: 'affair',     // -> '/main/affair/'
                name: 'affair',
                component: () => import('../views/main/affair/index.vue')
            },
            {
                path: 'message',    // -> '/main/message/'
                name: 'message',
                component: () => import('../views/main/message/layout.vue')
            },
            {
                path: 'archive',   // -> '/main/archive/'
                name: 'archive',
                component: () => import('../views/main/archive/index.vue')
            },
            {
                path: '/settings',
                name: 'settings',
                component: () => import('../views/settings.vue'),
                meta: {transition: 'slide-left'},
            },
            {
                path: '/profile',
                name: 'profile',
                component: () => import('../views/main/profile/profile.vue'),
                meta: {transition: 'slide-left'},
            },
        ]
    },
    {
        path: '/home',
        name: '/home',
        redirect: '/main/home',
    },
    {
        path: '/bulletin',
        name: '/bulletin',
        redirect: '/main/bulletin',
    },
    {
        path: '/message',
        name: '/message',
        redirect: '/main/message',
    },
    {
        path: '/:pathMatch(.*)*',
        component: () => import('../views/404.vue'),
        meta: {transition: 'slide-left'},
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

