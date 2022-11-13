<template>
  <div>
    <Header></Header>
    <div class="block">
      <el-timeline>
        <el-timeline-item :timestamp="blog.created" placement="top" v-for="blog in blogs">
          <el-card>
            <router-link :to="{name:'BlogDetail',params:{blogId:blog.id}}">
              <h4>{{ blog.title }}</h4>
            </router-link>
            <p>{{ blog.description }}</p>
          </el-card>
        </el-timeline-item>


      </el-timeline>
    </div>
    <el-pagination class="mpage"
                   background
                   layout="prev, pager, next"
                   :current-page="currentPage"
                   :page-size="pageSize"
                   :total="total"
                   @current-change=page
    >
    </el-pagination>
  </div>
</template>

<script setup>
import {getToken} from "../composable/auth";
import {NOTATION} from "../composable/utils";
import {getCurrentPage} from "../api/posts";

let currentPageNum = 1
let blogs = {}
let totalPageNum = 1
let pageArticleSize = 5

const handleCurrentPage = (index: number) => {
  console.log("getCurrentPage ", index)
  getCurrentPage(getToken(), index)
      .then(res => {
        console.log("getCurrentPage ", res)

        if (res.request.flag === 'no') {
          NOTATION(0, res.request.msg)
        } else {
          // message
          NOTATION(1, res.request.msg)

          // update number
          currentPageNum = res['result'].currentPageNum;
          blogs = res['result'].blogs;
          totalPageNum = res['result'].totalPageNum;
          pageArticleSize = res['result'].pageArticleSize;
        }
      })
      .catch(err => {
        console.log("getCurrentPage err ", err)
        NOTATION(0, err.msg)
      })
}

</script>

<style scoped>
.mpage {
  margin: 0 auto;
  text-align: center;
}
</style>