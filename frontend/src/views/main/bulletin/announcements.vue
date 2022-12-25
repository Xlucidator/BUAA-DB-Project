<template>
  <el-row class="mb-4" style="margin-top: 3%">
    <el-button @click="handleBack" style = "margin-left: 5%">
      <el-icon>
        <ArrowLeft/>
      </el-icon>
      back
    </el-button>
    <el-button @click="dialogFormVisible = true" type="primary" style = "margin-left: 74%"
               size="large" plain>
      <el-icon>
        <Edit/>
      </el-icon>
      New Post
    </el-button>
  </el-row>

  <div>
    <div class="block">
      <el-timeline>
        <template v-if="itemKey === 0">
          <el-timeline-item :timestamp="blog.PostDate" placement="top" v-for="blog in blogs">
            <el-card>
              <router-link :to="'bulletin/singlePage/'+blog.PId">
                <p class="text-xl font-extrabold">{{ blog.Title }}</p>
              </router-link>
              <p style="color: #888888">author: {{ blog.Poster }}</p>
              <p style="color: #888888">date: {{ blog.PostDate }}</p>
              <p style="color: #888888">type: {{ blog.Type }}</p>
              <!--            <p>{{ blog.description }}</p>-->
            </el-card>
          </el-timeline-item>
          <p>{{ blogs.value }}</p>
        </template>
        <template v-if="itemKey === 1">
          <el-timeline-item :timestamp="blog.PostDate" placement="top" v-for="blog in blogs">
            <el-card>
              <router-link :to="'bulletin/singlePage/'+blog.PId">
                <p class="text-xl font-extrabold">{{ blog.Title }}</p>
              </router-link>
              <p style="color: #888888">author: {{ blog.Poster }}</p>
              <p style="color: #888888">date: {{ blog.PostDate }}</p>
              <p style="color: #888888">type: {{ blog.Type }}</p>
              <!--            <p>{{ blog.description }}</p>-->
            </el-card>
          </el-timeline-item>
          <p>{{ blogs.value }}</p>
        </template>

      </el-timeline>
    </div>
    <el-pagination class="mpage"
                   background
                   layout="prev, pager, next"
                   v-model:current-page="currentPageNum"
                   :page-size="pageArticleSize"
                   :total="totalPageNum"
                   @current-change="changePage"
    >
    </el-pagination>
  </div>

  <el-dialog width="90%" v-model="dialogFormVisible" title="EDIT PASSAGE">
    <el-form :model="tableForm">
      <el-form-item label="title" :label-width="60">
        <el-input v-model="tableForm.Title"/>
      </el-form-item>
      <el-form-item label="author" :label-width="60">
        <el-input v-model="tableForm.Poster" disabled/>
      </el-form-item>
      <el-form-item label="type" :label-width="60">
        <el-input v-model="tableForm.Type"/>
      </el-form-item>
      <el-form-item label="content" :label-width="60">
        <div class="editor">
          <v-md-editor
              :placeholder="placeholder"
              :disabled-menus="[]"
              v-model="tableForm.Content"
              :height="height"
              :width="width"
              @change="handleChange"></v-md-editor>
        </div>
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

<script lang='ts' setup>
import {useRouter} from "vue-router";
import {computed, ref} from "vue";
import {getToken} from "../../../composable/auth";
import {NOTATION} from "../../../composable/utils";
import {getSinglePage} from "../../../api/posts";
import {newPost, getCurrentPage} from "../../../api/posts";
import store from "../../../store/index.js";

const router = useRouter()

const currentPageNum = ref(1)
let blogs = ref(store.state['passageList'])
let pageArticleSize = 5
const totalPageNum = ref(store.state['totalPageNum'] * pageArticleSize)
let itemKey = ref(0)
console.log("currentPageNum", currentPageNum.value)
console.log("totalPageNum", totalPageNum)

const handleBack = () => {
  router.go(-1)
}

const changePage = (val: number) => {
  console.log("changePage ", currentPageNum.value, val)
  getCurrentPage(getToken(), val)
      .then(res => {
        console.log("getCurrentPage ", res)

        if (res.status !== 200) {
          if ("details" in res.data) {
            NOTATION(0, res.data.details)
          } else {
            NOTATION(0, "ops~! other error")
          }
        } else {
          // message
          NOTATION(1, "success")
          totalPageNum.value = res.data['totalPage'] * pageArticleSize
          blogs.value = res.data['pageObj']
          currentPageNum.value = val
          itemKey.value = 1 - itemKey.value
        }
      })
      .catch(err => {
        console.log("getCurrentPage err ", err)
        NOTATION(0, err.detail)
      })
}


let dialogFormVisible = ref(false)
let tableForm = ref({
  //PId: '',
  Title: '',
  Poster: '',
  //PostDate: '',
  Content: '',
  LastEditor: '',
  //LastEditTime: '',
  Type: ''
})
tableForm.value.Poster = store.state.user['CodeName']
tableForm.value.LastEditor = store.state.user['CodeName']

interface Props {
  modelValue: string
  height?: string // 编辑器的高度
  width?: string // 编辑器的高度
  placeholder?: string
}

interface EmitEvent {
  (e: 'update:modelValue', params: string): void
}

const props = withDefaults(defineProps<Props>(), {
  height: '700px',
  width: '500px',
  placeholder: '请输入内容'
})

const emit = defineEmits<EmitEvent>()

const newValue = computed({
  get() {
    return props.modelValue
  },
  set(value: string) {
    emit('update:modelValue', value)
  }
})

// 内容变化时触发的事件。text 为输入的内容，html 为解析之后的 html 字符串。
const handleChange = (text: string, html: string) => {
  // console.log(JSON.stringify(text))
  console.log(html)
  // 如果有需要这些值，可以传回给父组件
}

const dialogConfirm = () => {
  newPost(getToken(), tableForm)
      .then(res => {
        console.log("newPost ", res)
        console.log("newPost ", tableForm)

        if (res.status !== 201) {
          if ("details" in res.data) {
            NOTATION(0, res.data.details)
          } else {
            NOTATION(0, "ops~! other error")
          }
        } else {
          // message
          NOTATION(1, res.data)
          dialogFormVisible.value = false
          console.log(itemKey.value)
          itemKey.value = 1 - itemKey.value
          changePage(1)
          console.log(itemKey.value)
        }
      })
      .catch(err => {
        console.log("newPost err ", err)
        NOTATION(0, err.detail)
      })
}

</script>

<style scoped>
.block {
  margin-left: 5%;
  margin-right: 5%;
}

.mpage {
  margin-bottom: 4%;
  text-align: center;
  margin-left: 5%;
}


.editor {
  flex: auto;
  align-content: center;
}
</style>