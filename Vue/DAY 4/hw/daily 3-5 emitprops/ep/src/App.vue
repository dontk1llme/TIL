<template>
  <div id="app">
    <h1>APP</h1>
    <input v-model.number='InputNum1' type="number">
    <p>parentData:{{InputNum2}}</p>
    <p>childData:{{InputNum3}}</p>

    <AppParent
    :InputNum1 = 'InputNum1'
    @num23 = 'getNum23'/>
  </div>
</template>

<script>
import AppParent from './components/AppParent.vue'

export default {
  name: 'App',
  components: {
    AppParent,
  },
  data(){
    return{
      InputNum1: null,
      InputNum2: null,
      InputNum3: null
    }
  },
  methods:{
    getNum23(input){
          // console.log(input)
          this.InputNum2= input.InputNum2
          this.InputNum3 = input.InputNum3
        },
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
