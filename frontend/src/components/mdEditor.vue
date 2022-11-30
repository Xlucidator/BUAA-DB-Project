<template>
  <v-md-editor
      :placeholder="placeholder"
      :disabled-menus="[]"
      v-model="newValue"
      :height="height"
      @change="handleChange"></v-md-editor>
</template>

<script lang="ts" setup>
import {computed} from "vue";



interface Props {
  modelValue: string
  height?: string // 编辑器的高度
  placeholder?: string
}

interface EmitEvent {
  (e: 'update:modelValue', params: string): void
}

const props = withDefaults(defineProps<Props>(), {
  height: '500px',
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
</script>

<style scoped>

</style>