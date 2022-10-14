<script lang="ts" setup>
import {computed, ref} from 'vue'

const activeIndex1 = ref('1')
const handleSelect = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}

const handleOpen = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
const handleClose = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}


const handleClick = () => {
  console.log('click')
}

const tableData = [
  {
    date: '2016-05-03',
    name: 'Tom',
    state: 'California',
    city: 'Los Angeles',
    address: 'No. 189, Grove St, Los Angeles',
    zip: 'CA 90036',
    tag: 'Home',
  },
  {
    date: '2016-05-02',
    name: 'Tom',
    state: 'California',
    city: 'Los Angeles',
    address: 'No. 189, Grove St, Los Angeles',
    zip: 'CA 90036',
    tag: 'Office',
  },
  {
    date: '2016-05-04',
    name: 'Tom',
    state: 'California',
    city: 'Los Angeles',
    address: 'No. 189, Grove St, Los Angeles',
    zip: 'CA 90036',
    tag: 'Home',
  },
  {
    date: '2016-05-01',
    name: 'Tom',
    state: 'California',
    city: 'Los Angeles',
    address: 'No. 189, Grove St, Los Angeles',
    zip: 'CA 90036',
    tag: 'Office',
  },
]

</script>

<template>
  <el-config-provider>
    <el-container class="layout-container-demo" style="height: 100vh">
      <el-header style="height: 80px; min-width: 100vh">
        <el-menu
            :default-active="activeIndex1"
            class="el-menu-demo"
            mode="horizontal"
            background-color="rgba(0,0,0,0)"
            text-color-light="#000"
            active-text-color-light="rgba(80,50,250,1)"
            @select="handleSelect"
            style="height: 100%;min-width: 100vh"
            :ellipsis=false
            :router=true
        >
          <el-menu-item index="home">
            <template #title>Home</template>
          </el-menu-item>

          <div class="flex-grow"/>

          <!--          <el-menu-item index="register">-->
          <!--            <template #title>Register</template>-->
          <!--          </el-menu-item>-->

          <!--          <el-menu-item index="login">-->
          <!--            <template #title>Login</template>-->
          <!--          </el-menu-item>-->

          <el-menu-item index="settings">
            <template #title>Settings</template>
          </el-menu-item>
        </el-menu>
      </el-header>

      <el-container>

        <el-aside width="200px" height="100%">
          <el-menu
              default-active="2"
              class="el-menu-vertical-demo"
              @open="handleOpen"
              @close="handleClose"
              background-color="rgba(0,0,0,0)"
          >
            <el-sub-menu index="1">
              <template #title>
                <span>Navigator One</span>
              </template>
              <el-menu-item-group title="Group One">
                <el-menu-item index="1-1">item one</el-menu-item>
                <el-menu-item index="1-2">item two</el-menu-item>
              </el-menu-item-group>
              <el-menu-item-group title="Group Two">
                <el-menu-item index="1-3">item three</el-menu-item>
              </el-menu-item-group>
              <el-sub-menu index="1-4">
                <template #title>item four</template>
                <el-menu-item index="1-4-1">item one</el-menu-item>
              </el-sub-menu>
            </el-sub-menu>
            <el-menu-item index="2">
              <el-icon>

              </el-icon>
              <span>Navigator Two</span>
            </el-menu-item>
            <el-menu-item index="3" disabled>
              <el-icon>
                <document/>
              </el-icon>
              <span>Navigator Three</span>
            </el-menu-item>
            <el-menu-item index="4">
              <el-icon>
                <setting/>
              </el-icon>
              <span>Navigator Four</span>
            </el-menu-item>
          </el-menu>
        </el-aside>
        <el-main>
          <router-view></router-view>
          <div style="text-align: center;margin-top: 15%">
            <span class="text-7xl">Vite + Vue </span>
            <br/>
            <span class="text-xs"> {{ $store.state.user }} </span>
            <br/>
          </div>

          <el-table :data="tableData" style="width: 100%">
            <el-table-column fixed prop="date" label="Date" width="150"/>
            <el-table-column prop="name" label="Name" width="120"/>
            <el-table-column prop="state" label="State" width="120"/>
            <el-table-column prop="city" label="City" width="120"/>
            <el-table-column prop="address" label="Address" width="600"/>
            <el-table-column prop="zip" label="Zip" width="120"/>
            <el-table-column fixed="right" label="Operations" width="120">
              <template #default>
                <el-button link type="primary" size="small" @click="handleClick"
                >Detail
                </el-button
                >
                <el-button link type="primary" size="small">Edit</el-button>
              </template>
            </el-table-column>
          </el-table>

        </el-main>
      </el-container>
    </el-container>

  </el-config-provider>
</template>

<style scoped>

.flex-grow {
  flex-grow: 1;
}
</style>
