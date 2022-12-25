<template>
    <el-config-provider>
    <!-- config for language and so on -->

      <el-container class="layout-container-demo" style="height: 100vh">
        <el-aside width="15%" height="100%">
          <div class="avatar">
            <el-avatar shape="square" :size="200" :fit="fit" :src="url" />
          </div>
          <div class="userinfo">
            <span class="font-bold text-xs"> NAME: {{ curCodeName }} </span>
          </div>
          <div>{{a}}</div>
          <el-menu
              default-active="announcement"
              class="el-menu-vertical-demo"
              background-color="rgba(0,0,0,0)"
              :router=true
          >
            <el-menu-item index="bulletin">
              <el-icon>
                <document/>
              </el-icon>
              <span>情报通知</span>
            </el-menu-item>

            <el-sub-menu index="arrangement">
              <template #title>
                <el-icon>
                  <SetUp/>
                </el-icon>
                <span>事务安排</span>
              </template>
              <el-menu-item-group title="Group One">
                <el-menu-item index="1-1">item one</el-menu-item>
                <el-menu-item index="1-2">item two</el-menu-item>
              </el-menu-item-group>
              <el-menu-item index="1-3">item three</el-menu-item>
            </el-sub-menu>

            <el-menu-item index="message">
              <el-icon>
                <ChatLineSquare/>
              </el-icon>
              <span>即时通讯</span>
            </el-menu-item>

            <el-menu-item index="archive">
              <el-icon>
                <Management/>
              </el-icon>
              <span>档案公示</span>
            </el-menu-item>

          </el-menu>
        </el-aside>


        <el-container>
          <el-header style="height: 60px; min-width: 100vh">
            <el-menu
                class="el-menu-demo"
                mode="horizontal"
                background-color="rgba(0,0,0,0)"
                text-color-light="#000"
                active-text-color-light="rgba(80,50,250,1)"
                style="height: 100%;min-width: 100vh"
                :ellipsis=false
                :router=true
            >
              <el-menu-item index="home">
                <template #title>Home</template>
              </el-menu-item>

              <el-menu-item>
                <el-breadcrumb :separator-icon="ArrowRight">
                  <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
                  <el-breadcrumb-item :to="{ path: '/'}"></el-breadcrumb-item>
                </el-breadcrumb>
              </el-menu-item>

              <div class="flex-grow"></div>
  
              <el-sub-menu index="2">
                <template #title> 
                  <el-avatar shape="circle" :size="40" :fit="fit" :src="url" />
                </template>
                <el-menu-item index="2-1">Profile</el-menu-item>
                <el-menu-item index="/settings">Settings</el-menu-item>
                <el-menu-item index="2-3">Logout</el-menu-item>
              </el-sub-menu>
            </el-menu>
          </el-header>

          <el-main>
              <router-view></router-view>
          </el-main>
        </el-container>
      </el-container>

    </el-config-provider>
  </template>
  
<script setup>
import store from '../../store/index.js'
import { ArrowRight } from '@element-plus/icons-vue'
import { UserFilled } from '@element-plus/icons-vue'
import { ref, reactive, toRefs, onMounted } from 'vue'
import avatarDemo from '../../assets/avatar_demo.png'
import axios from '../../axios'

const curCodeName = store.state.user.CodeName

function loadAvatar(CodeName) {
  console.log("index/profile/" + CodeName + '/')
  axios
  .get("index/profile/" + CodeName + '/')
  .then(resp => {
    console.log(resp)
    if (resp.status !== 200) {
      console.log("failed to get")
      return ''
    } else {
      console.log(resp.data['Avatar'])
      url.value = resp.data['Avatar']
    }
  })
  .catch(err => {
    console.log("axios failed")
    console.log(err)
    return ''
  })
  console.log("index/profile/" + CodeName + '/')
}

loadAvatar(curCodeName)

const fit = ref('cover')
const url = ref()
// url = test()

</script>
  
  
<style scoped>
  .flex-grow {
    flex-grow: 1;
  }

  .avatar {
    width: 100%;
    margin-top: 5%;
    margin-bottom: 5%;
    text-align: center;
  }

  .userinfo {
    margin: 20px;
  }
  
</style>
  