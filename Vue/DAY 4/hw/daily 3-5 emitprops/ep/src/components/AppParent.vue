<template>
  <div id='appParent'>
    <h1>AppParent</h1>
    <input v-model.number='InputNum2' type="number" @change='funcNum23'>
    <p>appData:{{InputNum1}}</p>
    <p>childData:{{InputNum3}}</p>
    <AppChild
      :InputNum1 = "InputNum1"
      :InputNum2 = 'InputNum2'
      @num3= 'getNum3'
      />
  </div>
  
</template>

<script>
import AppChild from './AppChild.vue'
export default {
  name: 'AppParent',
  components:{
    AppChild
  },
  data(){
    return{
      InputNum2: null,
      InputNum3: null,
    }
  },
  props:{
    InputNum1: Number,
  },
  methods:{
    getNum3(input){
      // console.log(input)
      this.InputNum3 = input
    },
    funcNum23: function(){
      const context = {
        InputNum3: this.InputNum3, 
        InputNum2: this.InputNum2, 
      }
      this.$emit('num23',context)
    }
  }
  

}
</script>

<style>

</style>