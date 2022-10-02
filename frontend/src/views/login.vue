<template>
  <div class="login_header">
    <h2> -- LOGIN -- </h2>
  </div>

  <div class="input-box">
    <el-input
        v-model="userName"
        class="w-50 m-2"
        size="large"
        placeholder="userName"
    />
  </div>
  <div class="input-box">
    <el-input
        v-model="password"
        class="w-50 m-2"
        size="large"
        placeholder="password"
        :show-password=true
    />
    <br/>
    <el-button size="large" type="primary" square @click="onSubmit()">confirm</el-button>
  </div>

</template>

<script setup>
import {ref} from "vue";
import {login} from "../api/manager";
import {ElNotification} from "element-plus";
import {useCookies} from "@vueuse/integrations/useCookies"

/* data */
let userName = ref("")
let password = ref("")

const onSubmit = () => {
  login(userName.value, password.value)
      .then(res => {
        //console.log(res)

        // message
        ElNotification({
          title: 'Success',
          message: 'This is a success message',
          type: 'success',
        })

        // store cookie
        const cookie = useCookies()
        cookie.set("admin-token", res.token)

        // getinfo
        // getinfo().then(res2 => {
        //   console.log(res)
        // })
      })
      .catch(err => {
        //console.log(err.response.data)

      })
}

</script>

<style scoped>
.login_header {
  margin-top: 200px;
  text-align: center;
}

.input-box {
  margin-bottom: 25px;
  text-align: center
}

.el-input {
  width: 300px;
  text-align: center
}

.el-button {
  margin-top: 25px;
  text-align: center
}

</style>