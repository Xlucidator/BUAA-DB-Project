<template>
  <div class="login_header">
    <h2>login</h2>
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
    />
  </div>
  <el-button size="large" type="primary" square>confirm</el-button>

</template>

<script setup>
import {ref} from "vue";

/* data */
let userName = ref("")
let password = ref("")

</script>

<style scoped>

.input-box {
  margin-bottom: 25px ;
}

.el-input {
  width: 300px
}

</style>