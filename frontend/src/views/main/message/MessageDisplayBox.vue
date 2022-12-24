<template>
  <div class="message-panel-box">

    <el-button class="browse-more">加载更多消息</el-button>

    <ul class="message-styles-box">
      <li v-for="(item, index) in getMessageTemplates()" 
          :key="index" :class="selectClass(item.type)">
      
        <el-avatar shape="square" fit="recover" 
                   src="../../../asset/avatar_demo.png" />
        <p class="message-nickname" v-if="item.type=='server'">
          {{item.nickName}} {{toMessageFormatTime(item.message.time)}}
        </p>
        <p class="message-nickname" v-else>
          {{toMessageFormatTime(item.message.time)}} {{item.sendFrom}}
        </p>
        <p class="message-classic" v-html="item.message.content"> </p>

      </li>
    </ul>

  </div>
</template>


<script setup>
import {ref, onMounted} from 'vue'
import store from '../../../store/index'

defineProps({
  GId         : Number,
  localInfo   : Object,
  concats     : Array,
})

const messages = ref([
  {
    MId : 0,
    Type: 1,
    SendFrom: store.state.userForm.CodeName,
    SendToPerson: null,
    SendToGroup: 0,
    ContentText: "welcome",
    Time: 1580572800000,
  },
  {
    MId : 1,
    Type: 1,
    SendFrom: store.state.user.CodeName,
    SendToPerson: null,
    SendToGroup: 0,
    ContentText: "hello",
    Time: 18972800000,
  }
])
const message = ref([])
const page = ref(0)
const isShowMore = ref(true)

function getMessageTemplates() {
  return this.message['group']
}

function toFullDate(date, showhm, sep) {
  date = new Date(date)
  let year = date.getFullYear()
  let month = date.getMonth() + 1
  let day = date.getDate()
  let hours = date.getHours()
  let minutes = date.getMinutes()

  if (showhm) return `${year}${month}${day}${hours}${minutes}`
  else {
    if (sep) return `${year}${sep}${month}${sep}${day}`
    else return `${year}${month}${day}`
  } 
}

function toMessageFormatTime(time) {
  let date = new Date(time)
  let hours = date.getHours()
  let minutes = date.getMinutes()
  if (hours   < 10) hours   = `0${hours}`
  if (minutes < 10) minutes = `0${minutes}`
  let curDate = new Date()

  if (toFullDate(date) === toFullDate(curDate))
    return `${hours}:${minutes}`
  else 
    return `${toFullDate(date, false, '/')} ${hours}:${minutes}`
}


function browseMore() {
  let obj = {
    id: localInfo.id,
    page: this.page += 1
  }
  // ...
}

function selectClass(type) {
  return type === 'server' ? 'message-layout-left' : 'message-layout-right'
}

onMounted(() => {
  
})

</script>


<style lang="scss" scoped>
.message-panel-box {
  height: 70%;
  padding: 0 20px;
  flex: 1;
  overflow-y: auto;
  -webkit-overflow-scrolling: touch;
  background: rgba(255, 255, 255, .8);

  .browse-more {
    width: 100%;
    padding: 10px 0;
    font-size: 12px;
    text-align: center;
  }

  .message-styles-box {
    margin-bottom: 20px;
    .message-layout-left,
    .message-layout-right {
      margin-top: 20px;
      width: 100%;
      .message-classic::before {
        content: '';
        position: absolute;
        border-width: 8px;
        border-style: solid;
      }
    }

    .message-layout-left {
      .message-avatar {
        float: left;
        margin-right: 10px;
      }
      .message-classic {
        background-color: rgba(255, 255, 255, .8);
        &::before {
          left: -16px;
          border-color: transparent rgba(255, 255, 255, .8) transparent transparent;
        }
      }
    }

    .message-layout-right {
      text-align: right;
      .message-avatar {
        float: right;
        margin-left: 10px;
      }
      .message-classic {
        text-align: left;
        color: #ffffff;
        background-color: rgba(55, 126, 200, .8);
        &::before {
          right: -16px;
          border-color:  transparent transparent  transparent rgba(55, 126, 200, .8);
        }
      }
    }

    .message-avatar {
      width: 40px;
      height: 40px;
      border-radius: 2px;
      border: 1px solid #eeeeee;
    }
    .message-nickname {
      color: #777777;
      font-size: 12px;
    }

    .message-classic {
      position: relative;
      max-width: 45%;
      margin-top: 5px;
      display: inline-block;
      padding: 9px 12px;
      font-size: 14px;
      color: #333333;
      border-radius: 5px;
      white-space: pre-line;
      word-break: break-all;
    }
  }
}
</style>