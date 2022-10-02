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

  </div>
</template>

<script setup>
import {computed, ref} from 'vue'
import {UseDark} from '@vueuse/components'

const themeDark = ref(false)
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