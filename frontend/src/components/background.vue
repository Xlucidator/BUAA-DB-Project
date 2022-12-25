<template>
  <Particles
      id="tsparticles"
      :particlesInit="particlesInit"
      :particlesLoaded="particlesLoaded"
      :options="options"
  />
</template>

<script setup lang='ts'>
import {reactive} from 'vue'
import {loadFull} from "tsparticles"
import type {Engine} from 'tsparticles-engine'

const particlesInit = async (engine: Engine) => {
  await loadFull(engine)
}

const particlesLoaded = async (container: any) => {
  console.log('Particles container loaded', container)
}
const options = reactive({
  fullScreen: { enable: true },
  background: {
    color: {
      value: '#ffffff' // 粒子颜色
    }
  },
  backgroundMask: {
	  composite: 'destination-out',
	  cover: {
		color: {
		  value: "#fff"
		},
		opacity: 1
	  },
    enable: false
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
      value: '#5c5c5c'
    },
    links: {
      color: '#bbbbbb', // '#dedede'。线条颜色。
      distance: 150, // 线条长度
      enable: true, // 是否有线条
      opacity: 0.5, // 线条透明度。
      width: 2 // 线条宽度。
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
      value: 50 // 粒子数量。
    },
    opacity: {
      value: 0.4 // 粒子透明度。
    },
    shape: {
      type: 'circle' // 可用的粒子外观类型有："circle","edge","triangle", "polygon","star"
    },
    size: {
      random: true,
      value: 5
    },
  },
  detectRetina: true,
})


</script>

<style scoped>
.flex-grow {
  flex-grow: 1;
}
</style>