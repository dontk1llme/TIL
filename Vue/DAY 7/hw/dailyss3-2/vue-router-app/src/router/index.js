import Vue from 'vue'
import Router from 'vue-router'
import Lunch from '@/views/Lunch.vue'
import Lotto from '@/views/Lotto.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'LunchVue',
      component: Lunch
    },
    {
      path: '/lotto/6',
      name: 'LottoVue',
      component: Lotto
    }
  ]
})