<template>
  <div>
    <h1>Detail</h1>
    <h2>제목: {{article.title}}</h2>
    <h2>내용: {{article.content}}</h2>
  </div>
</template>

<script>
export default {
    name:'DetailView',
    data(){
      return{
        article: {}
      }
    },
    methods:{
      fetchArticle(articleId){
        const articles = this.$store.state.articles
        const article = articles.filter((article)=>{
          return article.id == articleId
        })[0]
        this.article = article
      }
    },
    create(){ //장고에서 하나의 article을 가져온다
      // console.log(this.$route.params.id)
      // axios 대체
      const articleId = this.$route.params.id
      // this.$store.dispatch('fetchArticle', articleID) //store 거칠 필요가 업슴.. 데이터끼리 소통x
      this.fetchArticle(articleId)

    }

}
</script>

<style>

</style>