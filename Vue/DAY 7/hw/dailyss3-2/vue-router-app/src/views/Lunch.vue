<template>
  <div>
    <h1>점심메뉴</h1>
    <button @click='getLunch'>Pick Lunch</button>
    <p>{{lunchgot}}</p>
    <br><br><br><br>
    <h2>로또를 뽑아보자</h2>
    <button @click='toLotto'>Pick Lotto</button>
  </div>
</template>

<script>
// import HelloWorld from '@/components/HelloWorld.vue'
//랜덤을 위해 아래 lodash import
import _ from 'lodash'

export default {
  name: 'LunchVue',
  components: {
  },
  data () {
    return {
      lunchlst: ['피자','파스타','초밥','국밥','제육','돈까스','치킨','마제소바'],
      lunchgot: "",
    }
  },
  methods:{
    toLotto(){
      this.$router.push('lotto/6')
    },
    getLunch(){
      this.lunchgot = _.sample(this.lunchlst)
    },
  }
}
</script>