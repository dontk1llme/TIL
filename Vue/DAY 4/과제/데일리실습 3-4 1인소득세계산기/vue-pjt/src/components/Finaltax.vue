<template>
  <div>
    <h2>결정세액: {{ taxAmount-Reduction }} 만원</h2>
  </div>
</template>

<script>
export default {
  name:'FinalTax',
  props:{
    taxAmount: Number,
    Reduction: Number
  }
}
</script>

<style>

</style>