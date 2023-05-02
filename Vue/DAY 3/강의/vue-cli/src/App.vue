<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <!-- 3 사용하기 -->
    <MyComponent /> 
    <MyComponent /> 
    <HelloWorld msg="만반잘부"/>
    <!-- data 예시 확인 -->
    {{haha}}
    {{haha2()}}
    {{haha3}}
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import MyComponent from '@/components/MyComponent' //1 불러오기. 
// 뒤에 파일명이랑 앞에(변수)랑 일치시킬 필요는 없지만 헷갈리지 않게 일치시켜주셈
// 콘솔에서 변수명 다르게 보고싶으면 해당 vue 가서 name 수정하셈

export default {
  name: 'App',
  components: {
    HelloWorld,
    MyComponent, //2 등록하기
  },

  //data 예시
  data(){
    return{
      haha: 1
    }
  },
  methods:{
    haha2(){
      return 2
    }
  },
  computed:{
    haha3(){
      return this.haha*3
    }
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
