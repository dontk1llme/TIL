<template>
  <div>
    <h3>This is child component</h3>
    <p>{{staticProps}}</p>
    <p>{{myProps}}</p>
    <button @click="childToParent">클릭</button>
    <input type="text" v-model="childInputData" @keyup.enter="childInput">
  </div>            
</template>

<script>
export default {
  name: 'MyChild',
  data: function(){
    return{
      childInputData: null,
    }
  },
  props:{
    staticProps: String,
    myProps: String, //받아오고 위에서 쓰면됨
  },
  methods:{
    childToParent: function(){
      this.$emit('child-to-parent','child Data') //data->부모에서 데이터받기
    },
    childInput: function(){
      this.$emit('child-input',this.childInputData)
      this.childInputData = ""
    },
  }
}
</script>

<style>
  
</style>
