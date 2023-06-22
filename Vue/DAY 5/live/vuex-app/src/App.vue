<template>
  <div id="app">
    <!-- <h1>{{$store.state.message}}</h1> -->
    <!-- 위처럼 쓰기보다는 아래 computed에 넣어서 변수만 주는 경우가 많음 -->
    <h1>{{message}}</h1> 
    <h1>message의 길이는 {{messageLength}}</h1>
    <h1>두배는 {{doubleLength}}</h1>
    <input type="text" v-model='inputData' @keyup.enter='changeMessage'>
    {{inputData}}

  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  data(){
    return{
      inputData:null,
    }
  },
  components: {
    // HelloWorld
  },
  methods:{
    changeMessage(){
      const newMessage = this.inputData
      this.$store.dispatch('changeMessage',newMessage) //action이름, 변수
      this.inputData=null
    }
  },
  computed: {
    message(){
      return this.$store.state.message
    },
    messageLength(){
      return this.$store.getters.messageLength
    },
    doubleLength(){
      return this.$store.getters.doubleLength
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
