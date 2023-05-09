import Vue from 'vue'
import Router from 'vue-router'
import First from '@/views/First.vue'
import Second from '@/views/Second.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'FirstVue',
      component: First
    },
    {
      path: '/second',
      name: 'SecondVue',
      component: Second
    }
  ]
})