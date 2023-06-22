import Vue from 'vue'
import Vuex from 'vuex'
//중앙집권식~~~~~~~

Vue.use(Vuex)

export default new Vuex.Store({
  state: { //data와 비슷
    message: 'message in store'
  },
  getters: { //computed와 비슷
    messageLength(state){
      return state.message.length
    },
    doubleLength(state, getters){
      return getters.messageLength * 2
    },
  },
  mutations: { //methods 비슷 actions에서 실행된 걸 then으로 받는 느낌
    // CHANGE_MESSAGE(state, payload(message))
    CHANGE_MESSAGE(state, payload){
      // console.log(state)
      // console.log(message)
      state.message = payload
    }
  },
  actions: { //methods와 비슷. 일단 모든 건 여기에서 실행하고. . .(ex. axios(비동기))
    changeMessage(context, message){ //message = appvue의 newmessage. payload라고부름
      // console.log(context)
      // console.log(message)
      context.commit('CHANGE_MESSAGE', message) //앞의게 mutation임
    }
  },
  modules: {
  }
})
