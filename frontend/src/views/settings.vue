<template>
  <div class='header'>
    <h2>SETTINGS</h2>
  </div>
  <div class="setting">
    <div class="switch">
      <UseDark v-slot="{ isDark, toggleDark }">
        <el-switch
            v-model="themeDark"
            @click="toggleDark()"
            active-text="Dark"
            inactive-text="Light"
        />
      </UseDark>
    </div>
  </div>

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
</template>

<script setup>
import {computed, ref} from 'vue'
import {UseDark} from '@vueuse/components'
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
  revoke(getToken(), password)
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
      .catch(() => {
        NOTATION(0, err.msg)
      })
}

const themeDark = ref(false)
</script>

<style scoped>
.setting {
  margin-left: 38%;
  margin-top: 5%;
}

.header {
  margin-left: 40%;
  margin-top: 10%;
}

.switch {
  margin: 25px;
}

.Button {
  margin-top: 4%;
  max-width: 8%;
  max-height: 2%;
  margin-left: 40%;
  text-align: center;
}

</style>