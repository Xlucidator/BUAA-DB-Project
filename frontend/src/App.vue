<script lang="ts" setup>
import {computed, ref} from 'vue'

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

</script>

<template>
  <router-view></router-view>
</template>

<style scoped>

.flex-grow {
  flex-grow: 1;
}
</style>
