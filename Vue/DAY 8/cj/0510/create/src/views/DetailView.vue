<template>
  <div>
    <h1>detail</h1>
    <h1>제목 : {{ article?.title }}</h1>
    <h1>내용 : {{ article?.content }}</h1>
    <router-link :to="{ name : 'IndexView' }"> 메인으로 </router-link>
  </div>
</template>

<script>
export default {
  name: 'DetailView',
  data(){
    return {
      article : {}
    }
  },
  methods:{
    fetchArticle(articleId){
      const articles = this.$store.state.articles

      // axios.get(`https://django/article/${articleId}`)
      const article = articles.filter((article) => {
        return article.id == articleId
      })[0]

      this.article = article
    }
  },
  created(){
    const articleId = this.$route.params.id
    // 액시오스 대체
    this.fetchArticle(articleId)
  }

}
</script>

<style>

</style>