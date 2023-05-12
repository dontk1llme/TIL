import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    articles : [],
    articleId: 3
  },
  getters: {
  },
  mutations: {
    SAVE_ARTICLES(state, articles){
      state.articles.push(...articles)
    },
    SAVE_ARTICLE(state, article){
      state.articles.push(article)
      console.log(state.articles)
      
      state.articleId += 1
    }
  },
  actions: {
    saveArticle(context, payload){
      const article = {
        id : context.state.articleId,
        ...payload
      }
      context.commit('SAVE_ARTICLE', article)

    },
    fetchAritcles(context){
      // axios 요청을 보내야 하지만 받았다고 가정을 하고
      const articles = [
        // {
        //   id : 1,
        //   title : '제목',
        //   content : '내용'
        // },
        // {
        //   id : 2,
        //   title : '제목2',
        //   content : '내용2'
        // },
      ]
      context.commit('SAVE_ARTICLES', articles)
    }
  },
  modules: {
  }
})
