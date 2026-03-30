import { createApp, type App } from 'vue';
import {router} from './router';
import { default as MainApp } from './App.vue'

const app: App<Element> = createApp(MainApp);

app.use(router);

app.mount('#app');