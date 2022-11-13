<template>
  <div class="editor">
    <v-md-editor
        :placeholder="placeholder"
        :disabled-menus="[]"
        v-model="newValue"
        :height="height"
        @change="handleChange"></v-md-editor>
  </div>
</template>

<script lang = 'ts' setup>
import {computed} from "vue";
import {getToken} from "../composable/auth";
import {NOTATION} from "../composable/utils";
import {updatePostContent} from "../api/posts";

interface Props {
  modelValue: string
  height?: string // 编辑器的高度
  placeholder?: string
}

interface EmitEvent {
  (e: 'update:modelValue', params: string): void
}

const props = withDefaults(defineProps<Props>(), {
  height: '700px',
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

const submitCotent = (html:string) => {
  updatePostContent(getToken(), this.$route.params.id, html)
      .then(res => {
        console.log("getCurrentPage ", res)

        if (res.request.flag === 'no') {
          NOTATION(0, res.request.msg)
        } else {
          // message
          NOTATION(1, res.request.msg)
        }
      })
      .catch(err => {
        console.log("getCurrentPage err ", err)
        NOTATION(0, err.msg)
      })
}
</script>

<style scoped>

.editor {
  flex: auto;
  margin: 5%;
  align-content: center;
}

</style>