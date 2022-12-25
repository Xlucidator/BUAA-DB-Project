import {createApp} from 'vue'
import './styles/style.css'
import App from './App.vue'
import router from './router'
import store from "./store";
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import './styles/dark-vars.css'
import './styles/light-vars.css'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
import 'virtual:windi.css'
import './permission'
import VueMarkdownEditor from '@kangc/v-md-editor';
import '@kangc/v-md-editor/lib/style/base-editor.css';
import vuepressTheme from '@kangc/v-md-editor/lib/theme/vuepress.js';
import VMdPreviewHtml from '@kangc/v-md-editor/lib/preview-html';
import '@kangc/v-md-editor/lib/theme/style/vuepress.css';
import Prism from 'prismjs';
import Particles from 'particles.vue3'

const app = createApp(App)

for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
}

VueMarkdownEditor.use(vuepressTheme, {
    Prism,
});

//app.prototype.$axios = axios
app.use(store)
app.use(router)
app.use(ElementPlus)
app.use(VueMarkdownEditor)
app.use(VMdPreviewHtml)
app.use(Particles)

app.mount('#app')