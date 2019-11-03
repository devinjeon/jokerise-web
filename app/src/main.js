import Vue from 'vue'
import * as Sentry from '@sentry/browser'
import * as Integrations from '@sentry/integrations'
import VueAnalytics from 'vue-analytics'
import './plugins/axios'
import './plugins/bootstrap-vue'

import App from './App.vue'

Sentry.init({
  dsn: 'https://25b2563098514cf7af24e9fc663513a8@sentry.io/1806124',
  integrations: [new Integrations.Vue({ Vue, attachProps: true })],
  environment: process.env.VUE_APP_ENV
})

Vue.config.productionTip = false
Vue.use(VueAnalytics, {
  id: 'UA-79993277-2'
})

new Vue({
  render: h => h(App)
}).$mount('#app')
