import {createStore} from 'vuex'
import {getInfo} from "../api/manager";
import {getToken} from "../composable/auth"

const store = createStore({
    state() {
        return {
            user: {}
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
        }
    },
    actions: {
        getinfo({commit}) {
            return new Promise((resolve, reject) => {
                getInfo(getToken())
                    .then(res => {
                        console.log(">>>", store.state.user['token'])
                        commit("SET_USERINFO", res)
                        resolve(res)
                    })
                    .catch(err => reject(err))
            })
        }
    }
})

export default store