<script lang="ts" setup>
import {computed, ref} from 'vue';
import {getApplyForm, editApplyForm, acceptApply, rejectApply, addUser, getUserForm} from '../api/manager';
import {getToken} from '../composable/auth';
import {NOTATION} from '../composable/utils';

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

let applyForm = [{username: 'emilyu', permission: 2}, {username: 'yyy', permission: 1}]
let userForm = [{username: 'doctor', permission: 0}]

let username = '';
let perm = '';

const updateApplyForm = () => {
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

const searchApply = ref('')
const filterApplyForm = computed(() =>
    applyForm.filter(
        (data) =>
            !searchApply.value ||
            data.username.toLowerCase().includes(searchApply.value.toLowerCase())
    )
)

interface User {
  username: string
  permission: string
}

//TODO
const handleEdit = (index: number, row: User) => {
  console.log(index, row)

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
const handleAccept = (index: number, row: User) => {
  console.log("accept ", index, row)
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
const handleReject = (index: number, row: User) => {
  console.log("reject: ", index, row)
  applyForm.splice(index, 1)
  console.log(applyForm)
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

</script>

<template>
  <el-config-provider>
    <el-container class="layout-container-demo" style="height: 100vh">
      <el-aside width="15%" height="100%">
        <div class="avatar">
          <span> avatar </span>
        </div>
        <div class="userinfo">
          <span class="font-bold text-xs"> NAME:{{ $store.state.user.username }} </span>
        </div>
        <el-menu
            default-active="2"
            class="el-menu-vertical-demo"
            @open="handleOpen"
            @close="handleClose"
            background-color="rgba(0,0,0,0)"
        >
          <el-menu-item index="1">
            <el-icon>
              <document/>
            </el-icon>
            <span>announcement</span>
          </el-menu-item>
          <el-sub-menu index="2">
            <template #title>
              <el-icon>
                <SetUp/>
              </el-icon>
              <span>arrangement</span>
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
          <el-menu-item index="3">
            <el-icon>
              <ChatLineSquare/>
            </el-icon>
            <span>communication</span>
          </el-menu-item>

          <el-menu-item index="4">
            <el-icon>
              <Management/>
            </el-icon>
            <span>Archive</span>
          </el-menu-item>
        </el-menu>
      </el-aside>


      <el-container>
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

        <el-main>
          <router-view></router-view>
          <!--          <div style="text-align: center;margin-top: 15%">-->
          <!--            <span class="text-7xl">Vite + Vue </span>-->
          <!--            <br/>-->
          <!--            <span class="text-xs"> {{ $store.state.user }} </span>-->
          <!--            <br/>-->
          <!--          </div>-->

          <!--                TODO-->
          <!-- -----------------------------------form--------------------------------------- -->

          <br/>
          <br/>
          <span class="text-xm test-bold" style="margin-left: 10%">good morning, </span>
          <span class="text-xl test-bold" style="margin-left: 10%"> {{ $store.state.user.username }} </span>
          <span class="text-xm test-bold" style="margin-left: 10%">.</span>
          <br/>
          <span class="text-xm test-bold" style="margin-left: 10%">welcome to the new world.</span>
          <br/>
          <br/>
          <br/>
          <br/>
          <br/>

          <div class="form">
            <el-button class="mt-4" style="width: 10%" @click="updateApplyForm()">
              refresh
            </el-button>
            <div class="formHeader">
              <span class="text-2xl test-bold">Waiting List</span>
            </div>
            <el-table :data="filterApplyForm" style="width: 100%">
              <el-table-column fixed prop="username" label="username" width="150"/>
              <el-table-column prop="permission" label="perm" width="150"/>
              <el-table-column align="right">
                <template #header>
                  <el-input v-model="searchApply" size="small" placeholder="Type to search"/>
                </template>
                <template #default="scope">
                  <el-button size="small" @click="handleEdit(scope.$index, scope.row)">Edit</el-button>
                  <el-button size="small" @click="handleAccept(scope.$index, scope.row)">accept</el-button>
                  <el-button
                      size="small"
                      type="danger"
                      @click="handleReject(scope.$index, scope.row)"
                  >reject
                  </el-button>
                </template>
              </el-table-column>
            </el-table>
          </div>
          <br/>
          <div class="form">
            <div class="formHeader">
              <span class="text-2xl test-bold">User List</span>
            </div>
            <el-table :data="userForm" style="width: 100%">
              <el-table-column fixed prop="username" label="username" width="150"/>
              <el-table-column prop="permission" label="permission" width="120"/>
            </el-table>
          </div>
        </el-main>
      </el-container>
    </el-container>

  </el-config-provider>
</template>

<style scoped>

.flex-grow {
  flex-grow: 1;
}

.form {
  margin-left: 20%;
  margin-right: 20%;
}

.formHeader {
  margin-bottom: 2%;
  text-align: center;
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
