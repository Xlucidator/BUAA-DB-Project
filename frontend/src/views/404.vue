<template>
  <div class="Page404">
    <el-result
        icon="error"
        title="404 NOT FOUND"
        sub-title="Who lead you here, my dear poor little strayed?"
    >
      <template #extra>
        <el-button type="primary" @click="$router.push('/')">BACK</el-button>
      </template>
    </el-result>
  </div>
</template>

<script>
export default {
  name: "404"
}
</script>

<style scoped>
.Page404 {
  margin-top: 18%;
}

</style>