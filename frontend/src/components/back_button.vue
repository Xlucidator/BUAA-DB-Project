<template>
  <back_button>
    <el-button @click="handleBack" type="primary">
      <el-icon>
        <ArrowLeft/>
      </el-icon>
      back
    </el-button>
  </back_button>
</template>

<script setup lang='ts'>
import {useRouter} from "vue-router";
const router = useRouter()
const handleBack = () => {
  router.go(-1)
}
</script>

<style scoped>

</style>