import { createApp } from 'vue'
import App from './App.vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'; 
import api from '@/api.js';
import router from './router'

const app = createApp(App)
app.config.globalProperties.api=api
app.use(ElementPlus)
// 挂载路由模块
app.use(router)
app.mount('#app')