<template>
  <div id='appChild'>
    <h1>AppChild</h1>
    <input v-model.number='InputNum3' type="number" @change='funcNum3'>
    <p>appData:{{InputNum1}}</p>
    <p>parentData:{{InputNum2}}</p>
    <p>childData:{{InputNum3}}</p>

  </div>
</template>

<script>
export default {
    name: 'AppChild',
    data(){
        return{
        InputNum3: null,
        }
    },
    props:{
        InputNum1: Number,
        InputNum2: Number
    },
    methods:{
        funcNum3: function(){

            // const context = {
            //     InputNum3: this.InputNum3, 
            //     InputNum2: this.InputNum2, 
            // }
            // console.log('dd')
            this.$emit('num3', this.InputNum3)
        }
    }

}
</script>

<style>

</style>