<template>
  <span :key="itemKey.value"></span>
  <!--  line above is to refresh this page, or else nothing will be shown -->
  <el-card v-if="passage.length > 0" class="box-card">
    <template #header>
      <div class="card-header">
        <p class="text-3xl font-extrabold">{{ passage[0].Title }}</p>
        <el-button @click="dialogFormVisible = true" class="button" text>
          <el-icon>
            <EditPen/>
          </el-icon>
          Edit
        </el-button>

      </div>
    </template>
    <v-md-preview-html :html="htmlContent" preview-class="vuepress-markdown-body">
    </v-md-preview-html>
  </el-card>

  <div class="deletePassage">
    <el-button @click="deleteThisPassage" class="button" text>
      delete passage
      <el-icon>
        <Delete/>
      </el-icon>
    </el-button>
  </div>

  <el-dialog width="90%" v-model="dialogFormVisible" title="EDIT PASSAGE">
    <el-form :model="tableForm">
      <el-form-item label="title" :label-width="60">
        <el-input v-model="tableForm.Title"/>
      </el-form-item>
      <el-form-item label="author" :label-width="60">
        <el-input v-model="tableForm.Poster" disabled/>
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
import {getSinglePage, deleteSinglePage, updatePostContent} from "../../../api/posts";
import VueMarkdownEditor, {xss} from '@kangc/v-md-editor';
import {ElMessageBox} from "element-plus";

const router = useRouter()
console.log("router", router)

let passage = []
let itemKey = ref(0)
let dialogFormVisible = ref(false)
let tableForm = ref({Title: '', Content: '', Poster: ''})
let htmlContent = ref("");

getSinglePage(getToken, router.currentRoute.value.params.id)
    .then(res => {
      console.log("getSinglePage", res)

      if (res.status !== 200) {
        if ("details" in res.data) {
          NOTATION(0, res.data.details)
        } else {
          NOTATION(0, "ops~! other error")
        }
      } else {
        // message
        NOTATION(1, "got passage successfully~")
        // store
        passage.splice(0, 1, res.data)
        console.log("passage", passage)
        console.log("itemKey", itemKey)
        tableForm.value.Title = passage[0].Title;
        tableForm.value.Poster = passage[0].Poster;
        tableForm.value.Content = passage[0].Content;
        htmlContent.value = xss.process(VueMarkdownEditor.vMdParser.themeConfig.markdownParser.render(passage[0].Content))
        console.log("itemKey", itemKey)
        console.log("htmlContent", htmlContent)
        itemKey.value = Math.random()
      }
    })
    .catch(err => {
      console.log(err)
      NOTATION(0, err.detail)
    })

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
  passage[0].Title = tableForm.value.Title
  passage[0].Content = tableForm.value.Content
  passage[0].Poster = tableForm.value.Poster
  updatePostContent(getToken(), router.currentRoute.value.params.id, passage[0])
      .then(res => {
        console.log("updatePostContent ", res)

        if (res.status !== 200) {
          if ("details" in res.data) {
            NOTATION(0, res.data.details)
          } else {
            NOTATION(0, "ops~! other error")
          }
        } else {
          // message
          NOTATION(1, res.data)
          passage.splice(0, 1, res.data)
          dialogFormVisible.value = false;
          htmlContent.value = xss.process(VueMarkdownEditor.vMdParser.themeConfig.markdownParser.render(passage[0].Content))
          itemKey.value = Math.random()
        }
      })
      .catch(err => {
        console.log("updatePostContent err ", err)
        NOTATION(0, err.detail)
      })
}


const deleteThisPassage = () => {
  ElMessageBox.confirm(
      'this action will permanently delete the post. Continue?',
      'Warning',
      {
        confirmButtonText: 'OK',
        cancelButtonText: 'Cancel',
        type: 'warning',
      }
  )
      .then(() => {
        deleteSinglePage(getToken(), router.currentRoute.value.params.id)
            .then(res => {
              console.log("deletePassage ", res)

              if (res.status !== 204) {
                if ("details" in res.data) {
                  NOTATION(0, res.data.details)
                } else {
                  NOTATION(0, "ops~! other error")
                }
              } else {
                // message
                NOTATION(1, res.data)
                router.go(-1)
              }
            })
            .catch(err => {
              console.log("updatePostContent err ", err)
              NOTATION(0, err.detail)
            })
      })
      .catch(() => {
        console.log("updatePostContent err ")
      })
}

</script>

<style scoped>

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.text {
  font-size: 14px;
}

.item {
  margin-bottom: 18px;
}

.box-card {
  width: 80%;
  margin-top: 3%;
  margin-left: 10%;
}

.editor {
  flex: auto;
  align-content: center;
}

.deletePassage {
  margin-top: 10px;
  margin-left: 80%;
}

</style>