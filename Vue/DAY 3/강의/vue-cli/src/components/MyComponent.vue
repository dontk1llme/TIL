<template>
<!-- 0. .vue 만들기 -->
  <div class='border'> 
    <h1>This is MyComponent</h1> 
    <MyChild/>
  </div>
  <!-- 또 다른 div는 쓸 수 없. 하나의 element만 가능함 -->
</template>

<script>
import MyChild from '@/components/MyChild'
export default {
    name: 'MyComponentaaaaa', //new Vue 같은 거 안 써도 댐
    components:{
        MyChild,
    }

}
</script>

<style>
.border{
    border: solid;
}
</style>