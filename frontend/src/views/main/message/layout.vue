<template>
  <el-container>
    <el-aside class="group-bar">

      <el-header style="float:left; width:100%">
        <el-input v-model="targroup" style="width:80%; margin: 3%" placeholder="搜索群组/联系人" prefix-icon="Search" />
        <el-button type="primary" :icon="add" circle>
          <el-icon><Plus /></el-icon>
        </el-button>
      </el-header>

      <MessageGroupBar :concats="concats" @switchGroup="switchGroup"/>
      <!-- <el-menu
            default-active="announcement"
            class="el-menu-vertical-demo"
            background-color="rgba(0,0,0,0)">
        <el-menu-item index="announcement">
          <span>A1行动小组</span>
        </el-menu-item>
        <el-menu-item index="message">
          <span>A3行动预备小组</span>
        </el-menu-item>
        <el-menu-item index="archive">
          <span>档案公示</span>
        </el-menu-item>        
      </el-menu> -->
    </el-aside>

    <el-main>
      <el-header>
        asdf
      </el-header>
    </el-main>
  </el-container>
</template>

<script setup>
import {ref} from 'vue'
import MessageGroupBar from './MessageGroupBar.vue'

const concats = ref([
  {
    id: 0,
    active: false,
    nickName: '聊天室',
    avatar: '../../../assets/avatar_demo.png',
    message: {
      time: 1580572800000,
      content: 'Welcome'
    }
  }
])

</script>

<style scoped>

.group-bar {
  border: solid;
  padding-top: 1%;
  height: 100%;
}

</style>