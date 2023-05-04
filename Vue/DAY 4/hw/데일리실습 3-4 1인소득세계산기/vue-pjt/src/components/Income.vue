<template>
  <div>
    <p>연봉 입력 (만원): <input v-model.number='Salary' type="number"></p> 
    <p>세액감면액 (만원): <input v-model.number='Reduction' type="number"></p> 
    <hr>
    <h2>종합소득금액: {{ Salary }} 만원</h2>
    <h2>종합소득공제: (-) {{ 150 }} 만원</h2>
    <h2>과세표준: {{taxBase}} 만원</h2>
    <hr>
    <TaxrateVue
      :tax-base = 'taxBase'
      :Reduction = 'Reduction'
    />
  </div>
  
</template>

<script>
import TaxrateVue from './Taxrate.vue'

export default {
  name: 'IncomeVue',
  components: {
    TaxrateVue
  },
  data(){
    return {
      Salary: null,
      Reduction: null,
    }
  },
  computed:{
    taxBase() {
      if (this.Salary-150 >=0){
        return this.Salary-150
      }
      else{
        return 0
      }
    }
  }
}
</script>

<style>

</style>