<template>
  <el-config-provider :locale="locale">
    <el-container class="layout-container-demo" style="height: 500px">
      <el-header style="height: 80px; min-width: 100vh">
        <el-menu
            :default-active="activeIndex1"
            class="el-menu-demo"
            mode="horizontal"
            background-color="rgba(0,0,0,0)"
            text-color-light="#000"
            active-text-color-light="rgba(80,50,250,1)"
            @select="handleSelect"
            style="height: 100%;min-width: 100vh"
            :ellipsis=false
            :router=true
        >
          <el-menu-item index="Home">
            <template #title>Home</template>
          </el-menu-item>

          <div class="flex-grow"/>

          <el-menu-item index="login">
            <template #title>Login</template>
          </el-menu-item>

          <el-menu-item index="settings">
            <template #title>Settings</template>
          </el-menu-item>
        </el-menu>
      </el-header>

      <el-container>

        <el-aside width="200px" height="100%">
          <el-menu
              default-active="2"
              class="el-menu-vertical-demo"
              @open="handleOpen"
              @close="handleClose"
              background-color="rgba(0,0,0,0)"
          >
            <el-sub-menu index="1">
              <template #title>
                <el-icon>
                  <location/>
                </el-icon>
                <span>Navigator One</span>
              </template>
              <el-menu-item-group title="Group One">
                <el-menu-item index="1-1">item one</el-menu-item>
                <el-menu-item index="1-2">item two</el-menu-item>
              </el-menu-item-group>
              <el-menu-item-group title="Group Two">
                <el-menu-item index="1-3">item three</el-menu-item>
              </el-menu-item-group>
              <el-sub-menu index="1-4">
                <template #title>item four</template>
                <el-menu-item index="1-4-1">item one</el-menu-item>
              </el-sub-menu>
            </el-sub-menu>
            <el-menu-item index="2">
              <el-icon>
                <icon-menu/>
              </el-icon>
              <span>Navigator Two</span>
            </el-menu-item>
            <el-menu-item index="3" disabled>
              <el-icon>
                <document/>
              </el-icon>
              <span>Navigator Three</span>
            </el-menu-item>
            <el-menu-item index="4">
              <el-icon>
                <setting/>
              </el-icon>
              <span>Navigator Four</span>
            </el-menu-item>
          </el-menu>
        </el-aside>
        <el-main>
          <router-view></router-view>
        </el-main>
      </el-container>
    </el-container>

  </el-config-provider>
</template>

<script setup>
import {computed, ref} from 'vue'

const activeIndex2 = ref('1')
const handleSelect = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}

const handleOpen = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
const handleClose = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
</script>

<style scoped>
.flex-grow {
  flex-grow: 1;
}
</style>