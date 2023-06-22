<template>
  <div id="app">
    <h1>이곳은 App.vue입니다.</h1>
    <img alt="Vue logo" src="./assets/logo.png">
    <hr>
    <HelloWorld msg="이곳은 HelloWorld.vue입니다."/>
    <MyChild msg = '싸피'/>

  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import MyChild from '@/components/MyChild'

export default {
  name: 'App',
  components: {
    HelloWorld,
    MyChild,
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
</style>
