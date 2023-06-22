<template>
  <div>
    <h1>index</h1>
    <ArticleItem
      v-for="article in articles"
      :key="article.id"

      :article="article"
    />
  </div>
</template>

<script>
import ArticleItem from "@/components/index/ArticleItem"

export default {
  name: 'IndexView',
  components:{
    ArticleItem
  },
  computed:{
    articles(){
      return this.$store.state.articles
    }
  },
  created(){
    // axios요청을 통해서 받았다고 가정 => actions로 들어가야함
    this.$store.dispatch('fetchAritcles')


  }

}
</script>

<style>

</style>