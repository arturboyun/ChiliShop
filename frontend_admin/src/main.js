import { createApp } from 'vue';
import App from './App.vue';
import './registerServiceWorker';
import store from './store';
import Equal from 'equal-vue';
import router from '@/router';

// Styles
import 'equal-vue/dist/style.css';

import './assets/css/index.scss';

// App
const app = createApp(App);

app.use(Equal);
app.use(store);
app.use(router);
app.mount('#app');
