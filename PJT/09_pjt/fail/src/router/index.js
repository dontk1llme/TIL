import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieView from '../views/MovieView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'movie',
    component: MovieView
  },
  {
    path: '/random',
    name: 'random',
    component: () => import(/* webpackChunkName: "about" */ '../views/RandomView.vue')
  },
  {
    path: '/watchlist',
    name: 'watchlist',
    component: () => import(/* webpackChunkName: "about" */ '../views/WatchListView.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
