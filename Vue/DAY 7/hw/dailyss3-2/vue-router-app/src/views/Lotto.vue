<template>
  <div>
    <h1>로또</h1>
    <button @click="getNums">Get Lucky Numbers</button>
    <p>럭키 넘바,,~~~</p>
    <p>{{number}}</p>
  </div>
</template>

<script>
import _ from 'lodash' //랜덤
export default {
  name: 'LottoVue',
  data(){
    return{
      number:""
    }
  },
  methods:{
    getNums(){
      this.number = ""
      for (let i=0; i<6;i++){
        this.number+=(String(_.sample(_.range(1,46)))+" ")
      }
    }
  }
  
}
</script>