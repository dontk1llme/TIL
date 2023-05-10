<template>
  <div id="app">
    <!-- <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <h1>SSAFY TUBE</h1>
    <YouTube/>
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import YouTube from './components/YouTube.vue'

export default {
  name: 'App',
  components: {
    // HelloWorld
    YouTube
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
h1{
  color: blue;
}
</style>
