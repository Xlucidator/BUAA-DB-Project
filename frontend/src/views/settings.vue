<template>
  <div class='header'>
    <span class="text-3xl">SETTINGS</span>
  </div>
  <div class="setting">
    <div class="switch">
      <el-switch
          v-model=(isDark)
          active-text="Dark"
          inactive-text="Light"
      />
    </div>
  </div>

  <div class="buttonToCenter">
    <el-button
        tabindex="-1"
        @click="logOut()">
      logout
    </el-button>

    <div class="jump">
      <p style="color: #888888">i'll be gone forever</p>
      <el-button
          tabindex="-1"
          @click="openBox()">
        cancel account
      </el-button>
    </div>
  </div>
</template>

<script lang = "ts" setup>
import {computed, ref} from 'vue'
import {useDark, useToggle} from '@vueuse/core'
import {ElMessage, ElMessageBox, ElNotification} from 'element-plus'
import {getInfo, revoke} from "../api/manager";
import {useRouter} from "vue-router";
import {useStore} from "vuex";
import {removeToken} from "../composable/auth"
import {getToken} from "../composable/auth";
import {NOTATION} from "../composable/utils";

const store = useStore()
const router = useRouter();

const logOut = () => {
  // logout and remove userinfo at frontend
  store.commit("REMOVE_USERINFO")

  // remove token from cookie
  removeToken()

  router.push("/login")

}

const checkDel = (password) => {
  revoke(password)
      .then(res => {
        console.log(res.request)
        const flag = res.request['flag']
        if (flag === 'no') {
          NOTATION(0, res.request['msg'])
        } else {
          // message
          NOTATION(1, res.request['msg'])
          store.commit("REMOVE_USERINFO")

          // remove token from cookie
          removeToken()
          router.push("/login")
        }
      })
      .catch(err => {
        console.log(err)
        NOTATION(0, err.msg)
      })
}

const openBox = () => {
  ElMessageBox.prompt('Please input your password', 'Confirm', {
    confirmButtonText: 'OK',
    cancelButtonText: 'Cancel',
  })
      .then(({value}) => {
        checkDel(value)
      })
      .catch(err => {
        NOTATION(0, err.msg)
      })
}
const isDark = useDark()
</script>

<style scoped>
.setting {
  text-align: center;
  margin-top: 5%;
}

.header {
  text-align: center;
  margin-top: 10%;
}

.switch {
  margin: 25px;
  text-align: center;
}

.jump {
  margin-top: 2%;
}

.buttonToCenter {
  margin-top: 5%;
  text-align: center;
}

</style>