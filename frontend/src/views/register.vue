<template>
  <div class="register">
    <span class="text-5xl"> -- REGISTER -- </span>
  </div>

  <div class="input-box">
    <el-form :model="form" label-width="120px">
      <el-form-item label="CodeName">
        <el-input v-model="form.CodeName"/>
      </el-form-item>
      <el-form-item label="Password">
        <el-input v-model="form.Password"/>
      </el-form-item>
      <el-form-item label="Password again">
        <el-input v-model="form.PwConfirm"/>
      </el-form-item>
      <el-form-item label="Class">
        <el-select v-model="form.Class" placeholder="please select your class">
          <el-option label="近卫干员" value="Guard"/>
          <el-option label="狙击干员" value="Sniper"/>
          <el-option label="重装干员" value="Defender"/>
          <el-option label="医疗干员" value="Medic"/>
          <el-option label="辅助干员" value="Supporter"/>
          <el-option label="术师干员" value="Caster"/>
          <el-option label="特种干员" value="Specialist"/>
          <el-option label="先锋干员" value="Vanguard"/>
        </el-select>
      </el-form-item>
      <el-form-item label="Region">
        <el-select v-model="form.Region" placeholder="please select your zone">
          <el-option label="泰拉" value="Terra"/>
          <el-option label="炎" value="Yan"/>
          <el-option label="龙门" value="Lungmen"/>
        </el-select>
      </el-form-item>
      <el-form-item label="Race">
        <el-select v-model="form.Race" placeholder="please select your zone">
          <el-option label="龙" value="Lung"/>
          <el-option label="黎博利" value="Liberi"/>
          <el-option label="鲁珀" value="Lupo"/>
        </el-select>
      </el-form-item>
      <el-form-item label="Description">
        <el-input v-model="form.Description"/>
      </el-form-item>
    </el-form>
  </div>

  <div class="Button">
    <Button
        tabindex="-1"
        class="transition !duration-300 focus:outline-none w-full py-3 rounded font-bold text-white bg-blue-400 ring-4 ring-blue-500 ring-opacity-50 cursor-pointer hover:bg-indigo-400 hover:ring-indigo-500 transform hover:scale-110 hover:-translate-y-1 hover:shadow-xl hover:opacity-80 shadow-indigo-500"
        @click="onSubmit()">

      START
    </Button>
  </div>

  <div class="jump">
    <p style="color: #888888">yes i already have an account</p>
    <el-button
        tabindex="-1"
        @click="back()">
      click me to log in
    </el-button>
  </div>
</template>

<script setup>
import {useRouter} from "vue-router";
import {register} from "../api/manager";
import {NOTATION} from "../composable/utils";
import {reactive} from "@vue/reactivity";

const router = useRouter()

const form = reactive({
  CodeName: '',
  Password: '',
  PwConfirm: '',
  Class: '',
  Region: '',
  Race: '',
  Description: ''
})

const back = () => {
  router.push("/login")
}

const onSubmit = () => {
  if (form.Password !== form.PwConfirm) {
    NOTATION(0, "passwords do not coordinate")
  } else {
    register(form)
        .then(res => {
          console.log(res)

          const flag = res.request['flag']
          if (flag === 'no') {
            NOTATION(0, res.request['msg'])
          } else {

            // message
            NOTATION(1, res.request['msg'])

            // jump
            router.push("/login")
          }
        })
        .catch(err => {
          console.log(err)
          NOTATION(0, err.msg)
        })
  }
}

</script>

<style scoped>
.register {
  margin-top: 8%;
  margin-bottom: 4%;
  text-align: center;
}

.input-box {
  margin-left: 32%;
  text-align: center;
}

.el-input {
  width: 250px;
  text-align: center
}


.Button {
  margin-top: 2%;
  margin-bottom: 4%;
  max-width: 8%;
  max-height: 3%;
  margin-left: 46%;
  text-align: center;
}

.jump {
  margin-top: 2%;
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

</style>