<template>
  <div class='header'>
    <h2>SETTINGS</h2>
  </div>
  <div class="setting">
    <div class="switch">
      <UseDark v-slot="{ isDark, toggleDark }">
        <el-switch
            v-model="themeDark"
            @click="toggleDark()"
            active-text="Dark"
            inactive-text="Light"
        />
      </UseDark>
    </div>
    <div class="switch">
      <el-switch
          v-model="themeLang"
          @click="switchLanguage()"
          active-text="CH"
          inactive-text="EN"
      />
    </div>
  </div>
</template>

<script setup>
import {computed, ref} from 'vue'
import {UseDark} from '@vueuse/components'

import zhCn from 'element-plus/dist/locale/zh-cn.mjs'
import en from 'element-plus/dist/locale/en.mjs'

export const language = ref('zh-cn')

const switchLanguage = () => {
  language.value = language.value === 'zh-cn' ? 'en' : 'zh-cn'
}

const themeDark = ref(false)
const themeLang = ref(true)

</script>

<style scoped>
.setting {
  margin-left: 38%;
  margin-top: 5%;
}

.header {
  margin-left: 40%;
  margin-top: 10%;
}

.switch {
  margin: 25px;
}

</style>