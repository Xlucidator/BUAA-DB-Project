<template>
  <el-button @click="handleBack" style="margin-top : 3%;margin-left: 5%">
    <el-icon>
      <ArrowLeft/>
    </el-icon>
    back
  </el-button>
  <div class="block">
    <el-avatar :size="150" :src="circleUrl"/>
    <br/>
    <p class="text-3xl" style="color: #333333">{{ CodeName }}</p>
    <el-divider>
      <el-icon>
        <star-filled/>
      </el-icon>
    </el-divider>
  </div>
  <div>
    <span class="information text-xl lineHeight">Class: </span>
    <span class="data text-xl lineHeight">{{ ClassC }}</span>
    <br/>
    <span class="information text-xl lineHeight">Region: </span>
    <span class="data text-xl lineHeight">{{ Region }}</span>
    <br/>
    <span class="information text-xl lineHeight">Race: </span>
    <span class="data text-xl lineHeight">{{ Race }}</span>
    <br/>
    <span class="information text-xl lineHeight">Description: </span>
    <span class="data text-xl lineHeight">{{ Description }}</span>
  </div>

</template>

<script lang="ts" setup>
import store from '../../../store/index.js'
import axios from '../../../axios'
import {computed, ref} from 'vue';
import {useRouter} from "vue-router";

const curCodeName = store.state.user.CodeName
let url = ref("");
let CodeName = curCodeName;
let ClassC = ref("");
let Region = ref("");
let Race = ref("");
let Description = ref("");

const router = useRouter();

function loadProfile(name) {
  console.log("index/profile/" + name + '/')
  axios
      .get("index/profile/" + name + '/')
      .then(resp => {
        console.log(resp)
        if (resp.status !== 200) {
          console.log("failed to get")
          return ''
        } else {
          console.log("loadProfile", resp.data)
          url.value = resp.data['Avatar']
          ClassC.value = resp.data['Class']
          Region.value = resp.data['Region']
          Race.value = resp.data['Race']
          Description.value = resp.data['Description']
        }
      })
      .catch(err => {
        console.log("axios failed")
        console.log(err)
        return ''
      })
  console.log("index/profile/" + name + '/')
}

const handleBack = () => {
  router.go(-1)
}

loadProfile(curCodeName)

</script>

<style scoped>
.block {
  text-align: center;
  margin-top: 7%;
}

.information {
  text-align: center;
  margin-left: 30%;
  color: #888888;
}

.data {
  padding-left: 10%;
  float: inside;
  text-align: center;
}

.lineHeight {
  line-height: 300%;
}

</style>