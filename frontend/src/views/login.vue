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
        show-password="true"
    />
    <br/>
    <el-button size="large" type="primary" square>confirm</el-button>
  </div>

</template>

<script setup>
import {ref} from "vue";

/* data */
let userName = ref("")
let password = ref("")

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