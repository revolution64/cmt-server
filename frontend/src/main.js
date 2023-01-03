import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import 'material-design-icons-iconfont/dist/material-design-icons.css'
import './assets/main.css'


// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

const vuetify = createVuetify({
    components,
    directives,
});

const app = createApp(App).use(vuetify);

app.use(router);

app.mount('#app');
