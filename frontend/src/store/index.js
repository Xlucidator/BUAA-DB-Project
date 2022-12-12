import {createStore} from 'vuex'
import {getApplyForm, getInfo, getUserForm} from "../api/manager";
import {getCurrentPage} from "../api/posts";
import {getToken, removeToken} from "../composable/auth"

function changeForm(form) {
    // let tmpForm = {CodeName: '', Permission: '', Class: '', Region: '', Race: '', Description: ''}

    return form
}

export const store = createStore({
    state() {
        return {
            user: {},
            applyForm: {},
            userForm: {},
            skin: 'light',
            passageList: [],
            CurrentPageNum: 1,
            totalPageNum: 5,
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
        SET_PASSAGE_LIST(state, passageList) {
            state.passageList = passageList["pageObj"]
            state.currentPageNum = passageList["pageIdx"]
            state.totalPageNum = passageList["totalPage"]
        },
    },
    actions: {
        get_info({commit}) {
            return new Promise((resolve, reject) => {
                getInfo()
                    .then(res => {
                        console.log("getInfo", res.data)
                        commit("SET_USERINFO", res.data)
                        //console.log(">>>", store.state.user['token'])
                        resolve(res)
                    })
                    .catch(err => reject(err))
            })
        },
        get_apply_form({commit}) {
            return new Promise((resolve, reject) => {
                getApplyForm()
                    .then(res => {
                        console.log("get_apply_form", res)
                        commit("SET_APPLY_FORM", res.data)
                        resolve(res)
                    })
                    .catch(err => reject(err))
            })
        },
        get_user_form({commit}) {
            return new Promise((resolve, reject) => {
                getUserForm()
                    .then(res => {
                        console.log("get_user_form", res)
                        commit("SET_USER_FORM", res.data)
                        resolve(res)
                    })
                    .catch(err => reject(err))
            })
        },
        set_Skin(context, value) {
            context.commit('GET_SKIN', value)
        },
        get_passage_list({commit}) {
            return new Promise((resolve, reject) => {
                getCurrentPage(getToken(), 1)
                    .then(res => {
                        console.log("get_passage_list", res)
                        commit("SET_PASSAGE_LIST", res.data)
                        resolve(res)
                    })
                    .catch(err => reject(err))
            })
        },

    }
})

export default store