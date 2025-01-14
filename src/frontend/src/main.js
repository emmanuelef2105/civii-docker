import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router'
import { createPinia } from 'pinia'  // Si usas Pinia para store

import './assets/global.css'

const app = createApp(App)

app.use(router)
app.use(createPinia())
app.mount('#app')
