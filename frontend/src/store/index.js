import {createStore} from 'vuex'
import {getApplyForm, getInfo} from "../api/manager";
import {getToken, removeToken} from "../composable/auth"

const store = createStore({
    state() {
        return {
            user: {},
            form: {}
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
        SET_APPLY_FORM(state, form) {
            state.form = form
            console.log("set_apply_form", store.state.form)
        }
    },
    actions: {
        getinfo({commit}) {
            return new Promise((resolve, reject) => {
                getInfo(getToken())
                    .then(res => {
                        console.log(">>>", res['request'])
                        if(res['request']['flag'] === 'no') {
                            removeToken()
                        } else {
                            commit("SET_USERINFO", res['result'])
                            //console.log(">>>", store.state.user['token'])
                            resolve(res)
                        }
                    })
                    .catch(err => reject(err))
            })
        },
        getApplyForm({commit}) {
            return new Promise((resolve, reject) => {
                getApplyForm(getToken())
                    .then(res => {
                        console.log(">>>", res['request'])
                        commit("SET_APPLY_FORM", res['result'])
                        resolve(res)
                    })
                    .catch(err => reject(err))
            })
        }
    }
})

export default store