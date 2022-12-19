<template>
  <div class="message-input-box">
    
    <div class="input-tools">
      <i slot="reference" class="el-icon-s-opportunity" title="表情"></i>
      <el-icon title="文件" style="float:left"><Files /></el-icon>
      <div style="float:left">  </div>
      <img src="../../../assets/face.png" alt="表情" style="float: left;border:0;width:20px;height:20px"/>
      
      <el-button size="mini" type="primary" class="send-button" 
                 style="float: right;" @click="sendMessage">
        发送/Send
      </el-button>
    </div>

    <el-input 
      type="textarea" resize="none" 
      :autosize="{minRows: 6, maxRows: 10}"
      v-model="inputText"
      @keyup.enter="sendMessage">
    </el-input>

    
  </div>
</template>


<script setup>
import {ref, onMounted} from 'vue'
import {gotoBottom} from '../../../composable/utils'
import faceIcon from '../../../assets/face.png'

defineProps({
  concats: Array,
  nowSwitchId: String,
  localInfo: Object,
})

const inputText = ref('')

const imgSrc = faceIcon

function sendMessage() {
  let message = {
    type: nowSwitchType(),
    id  : localInfo.id,
    body: {
      type    : 'user-message',
      sendTo  : nowSwitchId,
      sendFrom: localInfo.id,
      avatar  : localInfo.avatar,
      nickName: localInfo.nickName,
      message : {
        time    : + new Date(),
        content : obj.replaceFace(inputTextFilter()),
        textContent: inputTextFilter(),
      }
    }
  }
  if (checkBlank()) {
    // 发送消息
    inputText = ''
    gotoBottom()
  }
}

function nowSwitchType() {
  return nowSwitchId === 'group' ? 'group-message' : 'user-message'
}

function inputTextFilter() {
  return inputText.replace(/\n/g, '').replace(new RegExp('<', 'gm'), '&lt')
}

function checkBlank() {
  if (inputText.replace(/\s+/g, '') === '') {
    this.$alert('请输入内容')
    return false
  }
  return true
}

onMounted(() => {
  this.obj = new window.Face({
    el: document.querySelector('.el-icon-s-opportunity'),
    callBack: face => {
      this.inputText += `[${face.title}]`
      document.querySelector('.face-warp').getElementsByClassName.display = 'none'
    }
  })
})

</script>


<style lang="scss" scoped>
.message-input-box {
  // height: 150px;
  background-color: rgba(255, 255, 255, .85);
  border-top: 1px solid #dddddd;
  .input-tools {
    position: relative;
    padding-left: 10px;
    padding-top: 10px;
    .upload-demo {
      display: inline;
    }
    i {
      margin-left: 10px;
      color: rgb(94, 94, 94);
      font-size: 20px;
      cursor: pointer;
    }
  }
  .el-textarea {
    .el-textarea__inner {
      padding: 5px 20px;
      border-radius: 0;
      border: 0;
      background-color: transparent;
    }
  }
  .footer-tools {
    text-align: right;
    .send-button {
      padding: 7px 10px;
      margin-right: 20px;
      background: #377ec8;
    }
  }
}
.face-pabel {
  .face {
    display: inline-block;
    width: 20px;
    height: 20px;
  }
}
</style>