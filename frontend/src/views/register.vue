<template>
  <div class="register">
    <span class="text-5xl"> -- REGISTER -- </span>
  </div>

  <div class="input-box">
    <el-form :model="form" label-width="120px">
      <el-form-item label="CodeName">
        <el-input v-model="form.CodeName" @blur="checkSyntax(form.CodeName)"/>
      </el-form-item>
      <el-form-item label="Password">
        <el-input v-model="form.Password" :show-password="true"/>
      </el-form-item>
      <el-form-item label="Password again">
        <el-input v-model="form.PwConfirm" :show-password="true"/>
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
          <el-option v-for="op in region_options" :label="op.zhcn" :value="op.eng"/>
        </el-select>
      </el-form-item>
      <el-form-item label="Race">
        <el-select v-model="form.Race" placeholder="please select your zone">
          <el-option v-for="op in race_options" :label="op.zhcn" :value="op.eng"/>
        </el-select>
      </el-form-item>
      <el-form-item label="Description">
        <div class="test-box">
          <el-input v-model="form.Description" type="textarea" autosize=""/>
        </div>
      </el-form-item>
    </el-form>
  </div>

  <div class="Button">
    <Button
        tabindex="-1"
        class="transition !duration-300 focus:outline-none w-full py-3 rounded font-bold text-white bg-blue-400 ring-4 ring-blue-500 ring-opacity-50 cursor-pointer hover:bg-indigo-400 hover:ring-indigo-500 transform hover:scale-110 hover:-translate-y-1 hover:shadow-xl hover:opacity-80 shadow-indigo-500"
        @click="onSubmit()">
      register
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
import {ref} from "vue";

const router = useRouter()

let registerFlag = ref(1)

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

const checkSyntax = (str) => {
  const pattern = /^[A-za-z0-9][A-za-z0-9'.\s]*$/
  if (str !== '') {
    if (!pattern.test(str)) {
      NOTATION(0, 'contains only alnum and . and space')
      registerFlag.value = 0
    } else {
      registerFlag.value = 1
    }
  } else {
    registerFlag.value = 0
    NOTATION(0, 'CodeName shouldn\'t be null')
  }
}

const onSubmit = () => {
  if (form.Password === '') {
    NOTATION(0, "passwords not null")
  }
  if (form.Password !== form.PwConfirm) {
    NOTATION(0, "passwords do not coordinate")
  } else if (!registerFlag.value) {
    NOTATION(0, "please check your CodeName")
  } else {
    register(form)
        .then(res => {
          console.log(res)

          if (res.status !== 200 && res.status !== 201) {
            if ("details" in res.data) {
              NOTATION(0, res.data.details)
            } else {
              NOTATION(0, "ops~! other error")
            }
          } else {
            // message
            NOTATION(1, "registered successfully")

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

const region_options = ref([
  {zhcn: '炎', eng: 'Yan'},
  {zhcn: '哥伦比亚', eng: 'Columbia'},
  {zhcn: '卡西米尔', eng: 'Kazimierz'},
  {zhcn: '谢拉格', eng: 'Kjerag'},
  {zhcn: '拉特兰', eng: 'Laterano'},
  {zhcn: '莱塔尼亚', eng: 'Leithanien'},
  {zhcn: '雷姆必拓', eng: 'Rim Billiton'},
  {zhcn: '萨米', eng: 'Sami'},
  {zhcn: '米诺斯', eng: 'Minos'},
  {zhcn: '玻利瓦尔', eng: 'Bolívar'},
  {zhcn: '萨尔贡', eng: 'Sargon'},
  {zhcn: '叙拉古', eng: 'Siracusa'},
  {zhcn: '维多利亚', eng: 'Victoria'},
  {zhcn: '卡兹戴尔', eng: 'Kazdel'},
  {zhcn: '伊比利亚', eng: 'Iberia'},
  {zhcn: '阿戈尔', eng: 'Ægir'},
  {zhcn: '罗德岛', eng: 'Rhodes Island'},
  {zhcn: '未知', eng: 'Unknown'},
])

const race_options = ref([
  {zhcn: '龙', eng: 'Lung'},
  {zhcn: '黎博利', eng: 'Liberi'},
  {zhcn: '鲁珀', eng: 'Lupo'},
  {zhcn: '鬼', eng: 'Oni'},
  {zhcn: '阿达克利斯', eng: 'Archosauria'},
  {zhcn: '萨科塔', eng: 'Sankta'},
  {zhcn: '萨卡兹', eng: 'Sarkaz'},
  {zhcn: '菲林', eng: 'Feline'},
  {zhcn: '瓦伊凡', eng: 'Vouivre'},
  {zhcn: '德拉克', eng: 'Draco'},
  {zhcn: '沃尔珀', eng: 'Vulpo'},
  {zhcn: '杜林', eng: 'Durin'},
  {zhcn: '札拉克', eng: 'Zalak'},
  {zhcn: '库兰塔', eng: 'Kuranta'},
  {zhcn: '卡特斯', eng: 'Cautus'},
  {zhcn: '卡普里尼', eng: 'Caprinae'},
  {zhcn: '佩洛', eng: 'Perro'},
  {zhcn: '丰蹄', eng: 'Forte'},
  {zhcn: '乌萨斯', eng: 'Ursus'},
  {zhcn: '阿斯兰', eng: 'Aslan'},
  {zhcn: '麒麟', eng: 'Kylin'},
  {zhcn: '阿戈尔', eng: 'Ægir'},
  {zhcn: '未知', eng: 'Unknown'}
])

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

.test-box {
  width: 40%;
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