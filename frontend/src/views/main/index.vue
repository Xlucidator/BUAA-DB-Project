<template>
    <el-config-provider>
    <!-- config for language and so on -->

      <el-container class="layout-container-demo" style="height: 100vh">
        <el-aside width="15%" height="100%">
          <div class="avatar">
            <span> avatar </span>
          </div>
          <div class="userinfo">
            <span class="font-bold text-xs"> NAME: {{ store.state.user.CodeName }} </span>
          </div>
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
                  <el-breadcrumb-item :to="{ path: '/'}">通讯</el-breadcrumb-item>
                </el-breadcrumb>
              </el-menu-item>

              <div class="flex-grow"></div>

              <el-menu-item index="/settings">
                <template #title>Settings</template>
              </el-menu-item>
            </el-menu>
          </el-header>

          <el-main>
              <router-view></router-view>
          </el-main>
        </el-container>
      </el-container>

    </el-config-provider>
  </template>

  <script lang="ts" setup>
      import store from '../../store/index.js'
      import { ArrowRight } from '@element-plus/icons-vue'
  </script>


  <style scoped>
  .flex-grow {
    flex-grow: 1;
  }

  .avatar {
    margin-top: 100px;
    margin-bottom: 100px;
    text-align: center;
  }

  .userinfo {
    margin: 20px;
  }

  </style>
  