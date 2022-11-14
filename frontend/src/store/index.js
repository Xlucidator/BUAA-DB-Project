import {createStore} from 'vuex'
import {getApplyForm, getInfo, getUserForm} from "../api/manager";
import {getToken, removeToken} from "../composable/auth"

function changeForm(form) {
    // let tmpForm = {CodeName: '', Permission: '', Class: '', Region: '', Race: '', Description: ''}

    return form
}

const store = createStore({
    state() {
        return {
            user: {},
            applyForm: {},
            userForm: {},
            skin: 'light',
        }
    },
    mutations: {
        SET_USERINFO(state, user) {
            state.user = user
            console.log("set_userinfo", store.state.user)
        },
        REMOVE_USERINFO(state) {
            state.user = null
            console.log("remove_userinfo")
        },
        SET_APPLY_FORM(state, applyForm) {
            state.applyForm = changeForm(applyForm)
            console.log("set_apply_form", store.state.applyForm)
        },
        SET_USER_FORM(state, userForm) {
            state.userForm = changeForm(userForm)
            console.log("set_user_form", store.state.userForm)
        },
        GET_SKIN(state, newValue) {
            state.skin = newValue
        },
    },
    actions: {
        get_info({commit}) {
            return new Promise((resolve, reject) => {
                getInfo(getToken())
                    .then(res => {
                        console.log("getInfo", res['request'])
                        commit("SET_USERINFO", res['result'])
                        //console.log(">>>", store.state.user['token'])
                        resolve(res)
                    })
                    .catch(err => reject(err))
            })
        },
        get_apply_form({commit}) {
            return new Promise((resolve, reject) => {
                getApplyForm(getToken())
                    .then(res => {
                        console.log("get_apply_form", res['request'])
                        commit("SET_APPLY_FORM", res['result'])
                        resolve(res)
                    })
                    .catch(err => reject(err))
            })
        },
        get_user_form({commit}) {
            return new Promise((resolve, reject) => {
                getUserForm(getToken())
                    .then(res => {
                        console.log("get_user_form", res['request'])
                        commit("SET_USER_FORM", res['result'])
                        resolve(res)
                    })
                    .catch(err => reject(err))
            })
        },
        set_Skin(context, value) {
            context.commit('GET_SKIN', value)
        },
    }
})

export default store