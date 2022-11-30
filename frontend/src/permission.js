import router from "./router";
import {getToken} from "./composable/auth"
import {ElNotification} from "element-plus";
import store from "./store";

router.beforeEach(async (to, from, next) => {
    console.log("router.beforeEach")

    const token = getToken()
    if (!token && to.path !== '/login' && to.path !== '/register') {
        ElNotification({
            title: 'PLEASE LOGIN',
            message: "Don't panic, login first!",
            type: 'error',
        })
        return next({path: '/login'})
    }

    // to login twice is forbidden
    if (token && to.path === '/login') {
        ElNotification({
            title: 'TWINS',
            message: "Don't be greedy, login only once!",
            type: 'error',
        })
        return next({path: from.path ? from.path : '/'})
    }

    // if logged in, then getinfo and store info into vuex
    if (token) {
        await store.dispatch("get_info")
    }

    if(to.path === '/main/home') {
        await store.dispatch("get_apply_form")
        await store.dispatch("get_user_form")
    }

    next()
})

router.afterEach((to, from) => {
    const toDepth = to.path.split('/').length
    const fromDepth = from.path.split('/').length
    to.meta.transitionName = toDepth < fromDepth ? 'slide-right' : 'slide-left'
})