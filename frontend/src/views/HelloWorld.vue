<script lang="ts" setup>
import {computed, ref} from 'vue';
import {getApplyForm, editApplyForm, acceptApply, rejectApply, addUser, getUserForm} from '../api/manager.js';
import {getToken} from '../composable/auth.js';
import {NOTATION} from '../composable/utils.js';
import store from "../store/index.js";

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

interface User {
  CodeName: string
  Permission: string
  Class: string
  Region: string
  Race: string
  Description: string
}

let applyForm = store.state['applyForm']
console.log(store.state)
let userForm = store.state['userForm']
let tableForm = ref({CodeName: '', Permission: '', Class: '', Region: '', Race: '', Description: ''})

let dialogFormVisible = ref(false);
let dialogIdx = 0;

const dialogConfirm = () => {
  console.log("dialogConfirm", tableForm.value)
  dialogFormVisible.value = false;
  applyForm.splice(dialogIdx, 1, tableForm)
  editApplyForm(getToken(), tableForm.value)
      .then(res => {
        console.log(res)
        if (res.request.flag === 'no') {
          NOTATION(0, res.request.msg)
        } else {
          NOTATION(1, res.request.msg)
        }
      })
      .catch(err => {
        console.log(err)
        NOTATION(0, err.msg)
      })
}

const updateApplyForm = () => {
  console.log("updateApplyForm", getToken())
  getApplyForm(getToken())
      .then(res => {
        console.log(res)
        if (res.request.flag === 'no') {
          NOTATION(0, res.request.msg)
        } else {
          // message
          NOTATION(1, res.request.msg)

          // store form
          console.log(res['result'])
          applyForm = res['result']
        }
      })
      .catch(err => {
        console.log(err)
        NOTATION(0, err.msg)
      })

  getUserForm(getToken())
      .then(res => {
        console.log(res)
        if (res.request.flag === 'no') {
          NOTATION(0, res.request.msg)
        } else {

          // message
          NOTATION(1, res.request.msg)

          // store form
          userForm = res.request.userForm
          // console.log("?????", userForm.length)
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
            data.CodeName.toLowerCase().includes(searchApply.value.toLowerCase())
    )
)

const handleEdit = (index: number, row: User) => {
  tableForm.value = JSON.parse(JSON.stringify(row));
  dialogFormVisible.value = true
  dialogIdx = index
  console.log("handleEdit")
}

const handleAccept = (index: number, row: User) => {
  console.log("accept ", index, row)
  acceptApply(getToken(), row)
      .then(res => {
        console.log("acceptApply", res)

        if (res.request.flag === 'no') {
          NOTATION(0, res.request.msg)
        } else {
          // message
          NOTATION(1, res.request.msg)

          // update tables
          console.log("?????", userForm.length)
          let len = userForm.length
          //userForm.splice(len, 0, applyForm[index])
          //applyForm.splice(index, 1)

        }
      })
      .catch(err => {
        console.log("accept err ", err)
        NOTATION(0, err.msg)
      })

  // addUser(getToken(), row)
  //     .then(res => {
  //       console.log(res)
  //
  //       if (res.request.flag === 'no') {
  //         NOTATION(0, res.request.msg)
  //       } else {
  //         // message
  //         NOTATION(1, res.request.msg)
  //
  //         // store form
  //         userForm = res.request.userForm
  //       }
  //     })
  //     .catch(err => {
  //       console.log(err)
  //       NOTATION(0, err.msg)
  //     })
  updateApplyForm()
}
const handleReject = (index: number, row: User) => {
  console.log("reject: ", index, row)
  applyForm.splice(index, 1)
  console.log(applyForm)
  rejectApply(getToken(), row)
      .then(res => {
        console.log(res)

        if (res.request.flag === 'no') {
          NOTATION(0, res.request.msg)
        } else {
          // message
          NOTATION(1, res.request.msg)

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
          <span class="font-bold text-xs"> NAME: {{ $store.state.user.CodeName }} </span>
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

          <!-- -----------------------------------form--------------------------------------- -->

          <br/>
          <br/>
          <br/>
          <span class="text-xm " style="margin-left: 10%">Good morning, </span>
          <span class="text-xl font-extrabold"
                style="margin-left: 0.5%; margin-right: 0.5%"> {{ $store.state.user.CodeName }} </span>
          <span class="text-xm">.</span>
          <br/>
          <span class="text-xm test-bold" style="margin-left: 10%">Welcome to the new world.</span>
          <br/>
          <br/>
          <br/>
          <br/>

          <div class="form">
            <el-button class="mt-4" style="width: 10%" @click="updateApplyForm">
              refresh
            </el-button>
            <div class="formHeader">
              <span class="text-2xl test-bold">Waiting List</span>
            </div>
            <el-table :data="filterApplyForm" style="width: 100%">
              <el-table-column fixed prop="CodeName" label="CodeName" width="100"/>
              <el-table-column prop="Permission" label="Permission" width="100"/>
              <el-table-column prop="Class" label="Class" width="100"/>
              <el-table-column prop="Region" label="Region" width="100"/>
              <el-table-column prop="Race" label="Race" width="100"/>
              <el-table-column prop="Description" label="Description" width="100"/>
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
              <el-table-column fixed prop="CodeName" label="CodeName" width="150"/>
              <el-table-column prop="Permission" label="Permission" width="150"/>
              <el-table-column prop="Class" label="Class" width="150"/>
              <el-table-column prop="Region" label="Region" width="150"/>
              <el-table-column prop="Race" label="Race" width="150"/>
              <el-table-column prop="Mail" label="Mail" width="150"/>
            </el-table>
          </div>

          <br/>
          <br/>
          <br/>

          <!-- dialog -->
          <el-dialog v-model="dialogFormVisible" title="EDIT INFORMATION">
            <el-form :model="tableForm">
              <el-form-item label="name" :label-width="60">
                <el-input v-model="tableForm.CodeName" disabled/>
              </el-form-item>
              <el-form-item label="perm" :label-width="60">
                <el-input v-model="tableForm.Permission" autocomplete="off"/>
              </el-form-item>
              <el-form-item label="class" :label-width="60">
                <el-input v-model="tableForm.Class" autocomplete="off"/>
              </el-form-item>
              <el-form-item label="region" :label-width="60">
                <el-input v-model="tableForm.Region" autocomplete="off"/>
              </el-form-item>
              <el-form-item label="race" :label-width="60">
                <el-input v-model="tableForm.Race" autocomplete="off"/>
              </el-form-item>
              <el-form-item label="desc" :label-width="60">
                <el-input v-model="tableForm.Description" autocomplete="off"/>
              </el-form-item>
            </el-form>
            <template #footer>
              <span class="dialog-footer">
                <el-button @click="dialogFormVisible = false">Cancel</el-button>
                <el-button type="primary" @click="dialogConfirm"
                >Confirm</el-button
                >
              </span>
            </template>
          </el-dialog>

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
  margin-left: 10%;
  margin-right: 10%;
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
