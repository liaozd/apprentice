// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'

Vue.config.productionTip = false

Vue.filter('uppercase', (key) => {
  return key.toUpperCase()
})

Vue.filter('leftpad', (value) => {
  if (value >= 10) {
    return value
  }
  return '0' + value
})

/* eslint-disable no-new */
new Vue({
  el: 'app',
  components: { App }
})
