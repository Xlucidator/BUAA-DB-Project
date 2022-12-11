<template>
  <div>
    <div class="block">
      <el-timeline>
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


      </el-timeline>
    </div>
    <el-pagination class="mpage"
                   background
                   layout="prev, pager, next"
                   :current-page="currentPageNum"
                   :page-size="pageArticleSize"
                   :total="totalPageNum"
                   @current-change="handleCurrentChange"
    >
    </el-pagination>
  </div>
</template>

<script lang='ts' setup>
import {getToken} from "../../../composable/auth";
import {NOTATION} from "../../../composable/utils";
import {getCurrentPage} from "../../../api/posts";
import store from "../../../store/index.js";

let currentPageNum = 1
let blogs = store.state['passageList']
let totalPageNum = store.state['totalPageNum']
let pageArticleSize = 5

const handleCurrentChange = (index: number) => {
  console.log("getCurrentPage ", index)
  getCurrentPage(getToken(), index)
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
          NOTATION(1, "posts ready")

          blogs = res.data["passageList"];
          currentPageNum = res.data["pageIdx"];
          totalPageNum = res.data['totalPageNum']
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