<template>
  <el-container class="wrapper" style="height:100%">
    <el-aside class="group-bar">

      <el-header style="width:100%">
        <el-input v-model="tarGroup" style="width:80%; margin: 3%" placeholder="搜索群组/联系人" prefix-icon="Search" />
        <el-button @click="handleAddGroup()" type="primary" circle>
          <el-icon><Plus /></el-icon>
        </el-button>
      </el-header>
      <MessageGroupBar :concats="concats" @switchGroup="switchGroup"/>

    </el-aside>

    <el-main>

      <el-header>
        <span class="title">{{concats[nowSwitch].GName}}</span>
      </el-header>
      <MessageDisplayBox 
        :concats="concats" :localInfo="localInfo"
        @message="message"/>
      <MessageInputBox 
        :concats="concats" :localInfo="localInfo" />

    </el-main>

    <!-- dialog -->
  <el-dialog v-model="dialogAddGroupVisible" title="AddGroup"
             width="30%" draggable style="height:500px">
             <el-row>
    <el-col :span="12">
      <el-scrollbar max-height="300px">
        <!-- <ul style="height:100%; background-color: rgba(0, 0, 0, 0.1)"> -->
        <ul class="operator-list">
          <li v-for="i in (1,5)" class="operator-item">
            <el-avatar shape="square"></el-avatar>
            <div style="text-align:center;">operator-name</div>
            <el-checkbox v-model="checked1" label="" size="large" />
          </li>
        </ul>
      </el-scrollbar>
    </el-col>
    <el-col :span="12">
      
      <el-scrollbar max-height="300px">
        <span style="margin-left:20px; width:70%">联络小组名</span>
        <el-input v-model="newGroupName" style="margin-left:20px; width:70%" />
       
      </el-scrollbar>
    </el-col>
  </el-row>
    
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="dialogAddGroupVisible = false">Cancel</el-button>
        <el-button type="primary" @click="dialogAddGroupVisible = false">
          Confirm
        </el-button>
      </span>
    </template>
  </el-dialog>
  </el-container>

  

</template>

<script setup>
import axios from '../../../axios'
import {ref, onMounted} from 'vue'
import MessageGroupBar from './MessageGroupBar.vue'
import MessageDisplayBox from './MessageDisplayBox.vue'
import MessageInputBox from './MessageInputBox.vue'
import store from '../../../store/index'

const dialogAddGroupVisible = ref(false)

const tarGroup = ref("")

const concats = ref([
  {
    GId: 0,
    GName: 'Rhodesisland',
    active: false,
    avatar: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT3vJJ9-GS20euNHyc4dMnz74JGf45ca8MxJtUGCy8&s',
    LastMessage: {
      time: 1580572800000,
      content: 'total'
    }
  },
  {
    GId: 1,
    GName: '日落即逝',
    active: false,
    avatar: 'https://pic1.zhimg.com/v2-6714b4912885f481d11776147a672fe0_b.jpg',
    LastMessage: {
      time: 1580572805123,
      content: 'nothing'
    }
  },
  {
    GId: 2,
    active: false,
    GName: 'A1行动预备组',
    avatar: 'https://i02piccdn.sogoucdn.com/31ea48572e9b87a4',
    LastMessage: {
      time: 1580572802345,
      content: 'nothing'
    }
  }
])

const groups = handleGetGroups()

const nowSwitch = ref(0)  // change name to current
const nowSwitchId = ref('group')
const localInfo = ref({
  CodeName: store.state.user.CodeName,
  Avatar: store.state.user.Avatar,
})

function switchGroup(index, id) {
  this.nowSwitch = index
  this.nowSwitchId = id
  
  if (this.concats[index].message.isNewMessage !== undefined) {
    this.concats[index].message.isNewMessage = false
    this.concats[index].message.newMeesageCount = 0
  }
}

function handleAddGroup() {
  dialogAddGroupVisible.value = true
  
}

function handleGetGroups(CodeName) {
  
}

function handleGetOperators() {
  axios.get()
}


onMounted(() => {

})

</script>

<style lang="scss" scoped>

.group-bar {
  // border: solid;
  padding-top: 0%;
  // width: 270px;
  height: 100%;
}

.dialog-footer button:first-child {
  margin-right: 10px;
}


.operator-list {
  background-color: rgba(0,0,0,0.1);
  overflow: auto;
  -webkit-overflow-scrolling: touch;

  .operator-item {
    display: flex;
    padding: 10px 15px;
    width: 100%;
    height: 70px;
    font-size: 12px;
    box-sizing: border-box;
    &:hover {
      background: rgba(255, 255, 255, 0.267);
    }
    .message-left {
      margin-right: 10px;
      font-size: 0;
      .message-avatar {
        width: 40px;
        height: 40px;
      }
      .message-group {
        border: 1px solid #dedede;
        box-sizing: border-box;
      }
    }
    .message-right {
      flex: 1;
      overflow: hidden;
      .message-header {
        display: flex;
        justify-content: space-between;
        .message-title {
          width: 100%;
          font-size: 14px;
        }
        .message-time {
          color: #aaaaaa;
        }
      }
      .message-content {
        margin-top: 4px;
        color: #999999;
        overflow: hidden;
        white-space: nowrap;
        text-overflow: ellipsis;
      }
    }
  }
}


.wrapper {
  height: 100%;
  // background-image: url('../../../assets/avatar_demo.png');
  // background-image: url('http://api.btstu.cn/sjbz/zsy.php');
  background-size: cover;
  background-repeat: no-repeat;
  .el-container {
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    width: 88%;
    margin: 30px auto;
    .el-aside,
    .el-main {
      display: flex;
      flex-direction: column;
      border-radius: 6px;
      box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
    }
    .el-aside {
      background: rgba(235, 233, 232, .8);
    }
    .el-main {
      padding: 0;
      margin-left: 20px;
    }
    .el-header {
      position: relative;
      line-height: 40px;
      background: rgb(55, 126, 200);
      overflow: hidden;
      .title,
      .icon-message {
        color: #ffffff;
      }
      .icon-message {
        font-size: 20px;
        vertical-align: middle;
      }
      .title {
        display: inline-block;
        margin-top: 15px;
        margin-left: 5px;
        font-size: 36px;
        letter-spacing: 1px;
      }
    }
  }
  .footer {
    position: absolute;
    bottom: -23px;
    right: 0;
    left: 0;
    margin: auto;
    font-size: 13px;
    width: 150px;
    color: #ffffff;
    text-align: center;
    a {
      color: #ffffff;
      &:hover {
        color: #377ec8;
      }
    }
  }
}

</style>