<template>
  <div>
    <!-- <h1>{{ message }}</h1> -->
    <HelloWorld :message="message" />
  </div>
</template>

<script>
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'FirstVue',
  components: {
    HelloWorld
  },
  data () {
    return {
      message: '첫 번째 페이지입니다'
    }
  }
}
</script>