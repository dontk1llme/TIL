<template>
  <div>
    <h1>Index</h1>
    <ArticleItem 
      v-for='article in articles'
      :key='article.id'
      :article='article'/>

    <!-- {{articles}} -->
  </div>
</template>

<script>
import ArticleItem from '@/components/index/ArticleItem'
export default {
    name:'IndexView',
    components:{
      ArticleItem
    },
    computed:{
      articles(){
        return this.$store.state.articles
      }
    },
    created(){ //생성되었을때 article 주라
    // 가져오는거, 저장하는건 store에ㅓㅅ 함
      this.$store.dispatch('fetchArticles')


    }
}
</script>

<style>

</style>