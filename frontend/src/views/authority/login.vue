<template>

  <div class="login_header">
    <span class="text-5xl"> -- LOGIN -- </span>
  </div>

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

  <div class="jump">
    <p style="color: #888888">don't have an account yet?</p>
    <el-button
        tabindex="-1"
        @click="reg()">

      REGISTER
    </el-button>
  </div>

  <Particles
      id="tsparticles"
      :particlesInit="particlesInit"
      :particlesLoaded="particlesLoaded"
      :options="options"
  />

</template>

<script setup lang = "ts">
import {ref} from "vue";
import {login} from "../../api/manager";
import {useStore} from "vuex";
import {useRouter} from "vue-router";
import {ElNotification} from "element-plus";
import {setToken} from "../../composable/auth";
import {NOTATION} from "../../composable/utils";

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

import { reactive } from 'vue'
import { loadFull } from "tsparticles"
import type { Engine } from 'tsparticles-engine'

const particlesInit = async (engine:Engine) => {
    await loadFull(engine)
}

const particlesLoaded = async (container:any) => {
    console.log('Particles container loaded', container)
}
const options = reactive({
      background: {
        color: {
          value: '#ffffff' // 粒子颜色
        }
      },
      fpsLimit: 60,
      interactivity: {
        events: {
          onClick: {
            enable: true,
            mode: 'push' // 可用的click模式有: "push", "remove", "repulse", "bubble"。
          },
          onHover: {
            enable: true,
            mode: 'grab' // 可用的hover模式有: "grab", "repulse", "bubble"。
          },
          resize: true
        },
        modes: {
          bubble: {
            distance: 400,
            duration: 2,
            opacity: 0.8,
            size: 40
          },
          push: {
            quantity: 4
          },
          repulse: {
            distance: 200,
            duration: 0.4
          }
        }
      },
      particles: {
        color: {
          value: '#888888'
        },
        links: {
          color: '#888888', // '#dedede'。线条颜色。
          distance: 150, // 线条长度
          enable: true, // 是否有线条
          opacity: 0.5, // 线条透明度。
          width: 1 // 线条宽度。
        },
        collisions: {
          enable: false
        },
        move: {
          direction: 'none',
          enable: true,
          outMode: 'bounce',
          random: false,
          speed: 1.5, // 粒子运动速度。
          straight: false
        },
        number: {
          density: {
            enable: true,
            area: 800
          },
          value: 80 // 粒子数量。
        },
        opacity: {
          value: 0.5 // 粒子透明度。
        },
        shape: {
          type: 'circle' // 可用的粒子外观类型有："circle","edge","triangle", "polygon","star"
        },
        size: {
          random: true,
          value: 5
        }
      },
      detectRetina: true
    })


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
  margin-top: 2%;
  margin-bottom: 4%;
  max-width: 10%;
  max-height: 3%;
  margin-left: 45%;
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

</style>