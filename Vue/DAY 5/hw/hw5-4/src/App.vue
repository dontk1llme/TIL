// App.vue

<template>
  <div id="app">
    <p>Counter: {{ $store.state.counter }}</p>
    <p>Counter Double: {{ $store.getters.counterDouble }}</p>
    <button @click="$store.commit('increase')">Increase</button>
    <button @click="$store.commit('decrease')">Decrease</button>
  </div>
</template>


//  <script>
export default {
  name: 'App', 
}
// export default {
//   name: 'App', 
//   data: function() {
//     return {
//       counter: 0,
//     }
//   },
//   methods: {
//     increase: function () {
//       this.counter += 1
//     },
//     decrease: function () {
//       this.counter -= 1
//     },
//   },
//   computed: {
//     counterDouble: function () {
//       return this.counter * 2
//     },
//   },
// }
// </script>
</script>


<style>
</style>