import Vue from 'vue'
import VueAnalytics from 'vue-analytics'
import './plugins/axios'
import './plugins/bootstrap-vue'

import App from './App.vue'

Vue.config.productionTip = false
Vue.use(VueAnalytics, {
  id: 'UA-79993277-2'
})

new Vue({
  render: h => h(App)
}).$mount('#app')
