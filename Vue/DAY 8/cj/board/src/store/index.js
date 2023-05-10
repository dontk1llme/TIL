import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    articles: [
      
    ],
  },
  getters: {
  },
  mutations: {
    SAVE_ARTICLES(state, articles){
      state.articles = articles
    }
  },
  actions: {
    fetchArticles(context){
      //axios 요청을 통해서 articles 받았다고 가정! => actions 에서 했어야 함
      // 비동기!
      const articles = [
        {
          id:1, 
          title: '제목',
          content: '내용'
        },
        {
          id:2, 
          title: '제목2',
          content: '내용2'
        },
      ]
      context.commit('SAVE_ARTICLES', articles)
    }
  },
  modules: {
  }
})
