<template>
  <div class="parti">
    <Particles id="tsparticles"></Particles>
  </div>

  <div class="card">
    <el-card class="box-card">

      <template #header>
        <div class="card-header">
          <div class="login_header">
            <p class="text-5xl"> -- LOGIN -- </p>
          </div>
        </div>
      </template>
      <br/>
      <div class="input-box">
        <el-input
            v-model="userName"
            class="w-50 m-2"
            size="large"
            placeholder="userName"
        />
      </div>
      <div class="input-box">
        <el-input
            v-model="password"
            class="w-50 m-2"
            size="large"
            placeholder="password"
            :show-password=true
        />
        <br/>

      </div>
      <div class="Button">
        <Button
            tabindex="-1"
            class="transition !duration-300 focus:outline-none w-full py-3 rounded font-bold text-white bg-blue-400 ring-4 ring-blue-500 ring-opacity-50 cursor-pointer hover:bg-indigo-400 hover:ring-indigo-500 transform hover:scale-110 hover:-translate-y-1 hover:shadow-xl hover:opacity-80 shadow-indigo-500"
            @click="onSubmit()">

          CONFIRM
        </Button>
      </div>

        <br/>
      <div class="jump">
        <p style="color: #888888">don't have an account yet?</p>
        <el-button
            tabindex="-1"
            @click="reg()">

          REGISTER
        </el-button>
        <br/>
        <br/>
        <br/>
      </div>
    </el-card>
  </div>


</template>

<script setup lang="ts">
import {ref} from "vue";
import {login} from "../../api/manager";
import {useStore} from "vuex";
import {useRouter} from "vue-router";
import {ElNotification} from "element-plus";
import {setToken} from "../../composable/auth";
import {NOTATION} from "../../composable/utils";
import Particles from "../../components/background.vue"

/* data */
let userName = ref("")
let password = ref("")
const store = useStore()
const router = useRouter()

const reg = () => {
  router.push("/register")
}

const onSubmit = () => {
  login(userName.value, password.value)
      .then(res => {
        console.log("login", res)

        if (res.status !== 200) {
          if ("details" in res.data) {
            NOTATION(0, res.data.details)
          } else {
            NOTATION(0, "ops~! other error")
          }
        } else {
          // message
          NOTATION(1, "welcome~")
          // store cookie
          setToken(res.data.token)
          // store user info
          store.commit("SET_USERINFO", res.data.CodeName)

          // jump
          router.push("/main/home")
        }
      })
      .catch(err => {
        console.log(err)
        NOTATION(0, err.detail)
      })
}

</script>

<style scoped>
.login_header {
  margin-top: 12%;
  margin-bottom: 5%;
  text-align: center;
}

.input-box {
  margin-bottom: 2%;
  text-align: center
}

.el-input {
  width: 300px;
  text-align: center
}

.Button {
  margin-top: 8%;
  margin-bottom: 4%;
  max-width: 25%;
  max-height: 3%;
  margin-left: 38%;
  margin-right: 25%;
  text-align: center;
}

.transition {
  -webkit-transition-property: background-color, border-color, color, fill, stroke, opacity, -webkit-box-shadow, -webkit-transform, filter, backdrop-filter;
  -o-transition-property: background-color, border-color, color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter;
  transition-property: background-color, border-color, color, fill, stroke, opacity, box-shadow, -webkit-box-shadow, transform, -webkit-transform, filter, backdrop-filter;
  -webkit-transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  -o-transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  -webkit-transition-duration: 150ms;
  -o-transition-duration: 150ms;
  transition-duration: 150ms;
}

.jump {
  margin-top: 2%;
  text-align: center;
}

.parti {
  z-index: -1;
  position: absolute;
}

.card {
  padding-top: 10%;
  padding-left: 30%;
  padding-right: 30%;
}

</style>