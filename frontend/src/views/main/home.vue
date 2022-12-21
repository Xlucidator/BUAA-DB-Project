<template>

    <br/>
    <br/>
    <br/>

    <span class="text-xm " style="margin-left: 10%"> {{ greetings }} ,</span>
    <span class="text-xl font-extrabold" style="margin-left: 0.5%; margin-right: 0.5%"> {{ store.state.user.CodeName }} </span>
    <span class="text-xm">.</span>

    <br/>

    <span class="text-xm test-bold" style="margin-left: 10%">Welcome to Rhodes Island!</span>

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
      <el-table :data="filterApplyForm" style="width: 100%" :key="itemKey">
        <el-table-column fixed prop="CodeName" label="CodeName" width="100"/>
        <el-table-column prop="Permission" label="Permission" width="100"/>
        <el-table-column prop="Class" label="Class" width="100"/>
        <el-table-column prop="Region" label="Region" width="100"/>
        <el-table-column prop="Race" label="Race" width="100"/>
        <el-table-column prop="Description" label="Description" width="300" />
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
      <el-table :data="userForm" style="width: 100%" :key="itemKey">
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
          <el-button type="primary" @click="dialogConfirm">Confirm</el-button>
        </span>
      </template>
    </el-dialog>
    
</template>


<script lang="ts" setup>

import {computed, ref} from 'vue';
import {getApplyForm, editApplyForm, acceptApply, rejectApply, getUserForm} from '../../api/manager.js';
import {getToken} from '../../composable/auth.js';
import {NOTATION} from '../../composable/utils.js';
import store from "../../store/index.js";

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
let time = new Date().getHours()
const greetings = computed(() => {
  return time < 6  ? 'Good night, your health is your most precious asset' : 
         time < 12 ? 'Good morning'  :
         time < 18 ? 'Good afternoon': 'Good evening'
})
let itemKey = ref(0);

const dialogConfirm = () => {
  console.log("dialogConfirm", tableForm.value)
  dialogFormVisible.value = false;

  applyForm[dialogIdx] = tableForm.value
  console.log("dialogConfirm", applyForm)
  editApplyForm(tableForm.value)
      .then(res => {
        console.log(res)
        if (res.status !== 200) {
          if ("details" in res.data) {
            NOTATION(0, res.data.details)
          } else {
            NOTATION(0, "ops~! other error")
          }
        } else {
          NOTATION(1, "success")
        }
      })
      .catch(err => {
        console.log(err)
        NOTATION(0, err.msg)
      })
  itemKey.value = Math.random()
}

const updateApplyForm = () => {
  console.log("updateApplyForm", getToken())
  getApplyForm()
      .then(res => {
        console.log(res)
        if (res.status !== 200) {
          if ("details" in res.data) {
            NOTATION(0, res.data.details)
          } else {
            NOTATION(0, "ops~! other error")
          }
        } else {
          // message
          NOTATION(1, "success")

          // store form
          console.log(res.data)
          applyForm = res.data
        }
      })
      .catch(err => {
        console.log(err)
        NOTATION(0, err.msg)
      })

  getUserForm()
      .then(res => {
        console.log(res)
        if (res.status !== 200) {
          if ("details" in res.data) {
            NOTATION(0, res.data.details)
          } else {
            NOTATION(0, "ops~! other error")
          }
        } else {
          // message
          NOTATION(1, "success")
          // store form
          userForm = res.data.userForm
          // console.log("?????", userForm.length)
        }
      })
      .catch(err => {
        console.log(err)
        NOTATION(0, err.msg)
      })
  itemKey.value = Math.random()
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
  acceptApply(row)
      .then(res => {
        console.log("acceptApply", res)
        console.log(res.status)

        if (Math.floor(res.status / 100) !== 2) {
          if ("details" in res.data) {
            NOTATION(0, res.data.details)
          } else {
            NOTATION(0, "ops~! other error")
          }
        } else {
          // message
          NOTATION(1, "accepted")
          console.log("accecpt success")

          // update form
          userForm.splice(userForm.length, 0, row)
          applyForm.splice(index, 1)
        }
      })
      .catch(err => {
        console.log("accept err ", err)
        NOTATION(0, err.msg)
      })
  itemKey.value = Math.random()
}

const handleReject = (index: number, row: User) => {
  console.log("reject: ", index, row)
  applyForm.splice(index, 1)
  console.log(applyForm)
  rejectApply(row)
      .then(res => {
            console.log(res)
            if (res.status !== 204) {
              if ("details" in res.data) {
                NOTATION(0, res.data.details)
              } else {
                NOTATION(0, "ops~! other error")
              }
            } else {
              // message
              NOTATION(1, "reject succeeds")
            }
          }
      )
      .catch(err => {
        console.log(err)
        NOTATION(0, err.msg)
      })
}


</script>


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
