<script setup>
import {computed, ref} from 'vue'
import {getApplyForm, editApplyForm, acceptApply, rejectApply, addUser, getUserForm} from '../api/manager'
import {getToken} from '../composable/auth'
import {NOTATION} from '../composable/utils'
import {ElNotification} from "element-plus";

const activeIndex1 = ref('1')
const handleSelect = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}

const handleOpen = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
const handleClose = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}

const handleClick = () => {
  console.log('click')
}

let applyForm = []
let userForm = []

let username = '';
let perm = '';

export const updateApplyForm = () => {
  getApplyForm(getToken())
      .then(res => {
        console.log(res)

        const flag = res.request['flag']
        if (flag === 'no') {
          NOTATION(0, res.request['msg'])
        } else {

          // message
          NOTATION(1, res.request['msg'])

          // store form
          applyForm = res.request['applyForm'];
        }
      })
      .catch(err => {
        console.log(err)
        NOTATION(0, err.msg)
      })

  getUserForm(getToken())
      .then(res => {
        console.log(res)

        const flag = res.request['flag']
        if (flag === 'no') {
          NOTATION(0, res.request['msg'])
        } else {

          // message
          NOTATION(1, res.request['msg'])

          // store form
          applyForm = res.request['applyForm'];
        }
      })
      .catch(err => {
        console.log(err)
        NOTATION(0, err.msg)
      })
}

//TODO
const changeApply = () => {
  editApplyForm(getToken(), username, perm)
      .then(res => {
        console.log(res)

        const flag = res.request['flag']
        if (flag === 'no') {
          NOTATION(0, res.request['msg'])
        } else {
          // message
          NOTATION(1, res.request['msg'])

          // nothing to do
        }
      })
      .catch(err => {
        console.log(err)
        NOTATION(0, err.msg)
      })
}

const deleteApply = () => {
  rejectApply(getToken(), username)
      .then(res => {
        console.log(res)

        const flag = res.request['flag']
        if (flag === 'no') {
          NOTATION(0, res.request['msg'])
        } else {
          // message
          NOTATION(1, res.request['msg'])

          // nothing to do
        }
      })
      .catch(err => {
        console.log(err)
        NOTATION(0, err.msg)
      })
}


const agreeApply = () => {
  acceptApply(getToken(), username)
      .then(res => {
        console.log(res)

        const flag = res.request['flag']
        if (flag === 'no') {
          NOTATION(0, res.request['msg'])
        } else {
          // message
          NOTATION(1, res.request['msg'])

          // store form
          applyForm = res.request['applyForm'];
        }
      })
      .catch(err => {
        console.log(err)
        NOTATION(0, err.msg)
      })

  addUser(getToken(), username)
      .then(res => {
        console.log(res)

        const flag = res.request['flag']
        if (flag === 'no') {
          NOTATION(0, res.request['msg'])
        } else {
          // message
          NOTATION(1, res.request['msg'])

          // store form
          userForm = res.request['userForm'];
        }
      })
      .catch(err => {
        console.log(err)
        NOTATION(0, err.msg)
      })
}

</script>

<template>
  <el-config-provider>
    <el-container class="layout-container-demo" style="height: 100vh">
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
          <el-menu-item index="home">
            <template #title>Home</template>
          </el-menu-item>

          <div class="flex-grow"/>

          <!--          <el-menu-item index="register">-->
          <!--            <template #title>Register</template>-->
          <!--          </el-menu-item>-->

          <!--          <el-menu-item index="login">-->
          <!--            <template #title>Login</template>-->
          <!--          </el-menu-item>-->

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
          <div style="text-align: center;margin-top: 15%">
            <span class="text-7xl">Vite + Vue </span>
            <br/>
            <span class="text-xs"> {{ $store.state.user }} </span>
            <br/>
          </div>

          <!--                TODO-->
          <el-table :data="applyForm" style="width: 80%; text-align: center">
            <el-table-column fixed prop="username" label="username" width="150"/>
            <el-table-column fixed="permission" label="Name" width="120"/>
            <el-table-column fixed="right" label="Operations" width="210">
              <template #default>
                <el-button link type="primary" size="small">Edit</el-button>
                <el-button link type="primary" size="small">accept</el-button>
                <el-button link type="primary" size="small">reject</el-button>
              </template>
            </el-table-column>
          </el-table>

          <br/>

          <el-table :data="userForm" style="width: 80%; text-align: center">
            <el-table-column fixed prop="username" label="username" width="150"/>
            <el-table-column fixed="permission" label="Name" width="120"/>
            <el-table-column fixed="right" label="Operations" width="120">
              <template #default>
                <el-button link type="primary" size="small">Edit</el-button>
              </template>
            </el-table-column>
          </el-table>
        </el-main>
      </el-container>
    </el-container>

  </el-config-provider>
</template>

<style scoped>

.flex-grow {
  flex-grow: 1;
}
</style>
