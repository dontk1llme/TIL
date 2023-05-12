<template>
  <div>
    <h1>create</h1>
    <form @submit.prevent="saveArticle">
      <label for="title">제목</label>
      <input type="text" id="title" v-model="title">

      <label for="content">내용</label>
      <input type="text" id="content" v-model="content">
      
      <input type="submit">
    </form>
  </div>
</template>

<script>
export default {
  name: 'CreateView',
  methods:{
    saveArticle(){
      const payload = {
        title : this.title,
        content : this.content
      }
      this.$store.dispatch('saveArticle', payload)
      this.$router.push({name: 'IndexView'})
    }
  },
  data(){
    return{
      title : "",
      content: ""
    }
  }

}
</script>

<style>

</style>