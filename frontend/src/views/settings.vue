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
  <div class="revoke">
    <div class="Button">
      <Button tabindex="-1"
              class="transition !duration-300 focus:outline-none w-full py-3 rounded font-bold text-white bg-blue-400 ring-4 ring-blue-500 ring-opacity-50 cursor-pointer hover:bg-indigo-400 hover:ring-indigo-500 transform hover:scale-110 hover:-translate-y-1 hover:shadow-xl hover:opacity-80 shadow-indigo-500"
              @click="openBox">revoke
      </Button>
    </div>
  </div>
</template>

<script setup>
import {computed, ref} from 'vue'
import {UseDark} from '@vueuse/components'
import {ElMessage, ElMessageBox, ElNotification} from 'element-plus'
import {revoke} from "../api/manager";
import {useRouter} from "vue-router";

const router = useRouter();

const checkDel = (username, password) => {
  revoke(username, password)
      .then(res => {
        console.log(res.request)
        const flag = res.request['flag']
        if (flag === 'no') {
          ElNotification({
            title: 'Error',
            message: res.request['msg'],
            type: 'error',
          })
        } else {
          // message
          ElNotification({
            title: 'Success',
            message: res.request['msg'],
            type: 'success',
          })

          router.push("/login")
        }
      })
      .catch(err => {
        console.log(err)
        ElNotification({
          title: 'Error',
          message: err.msg,
          type: 'error',
        })
      })
}

const openBox = () => {
  ElMessageBox.prompt('Please input your password', 'Confirm', {
    confirmButtonText: 'OK',
    cancelButtonText: 'Cancel',
  })
      .then(({value}) => {
        checkDel(value, value)
      })
      .catch(() => {
        ElMessage({
          type: 'info',
          message: 'on second thought?',
        })
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