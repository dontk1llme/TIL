<template>
  <div>
    <input 
      type="text" 
      v-model="title" 
      @keyup.enter="createTodo"
    >
    <button @click="createTodo">+</button>
  </div>
</template>

<script>
import axios from'axios'

export default {
  name: 'CreateTodo',
  data: function () {
    return {
      title: null,
    }
  },
  methods: {
    createTodo: function () {
      // ...
      // 데이터 serialize
      const todoData = new TodoSerializer({
        title: this.title,
        is_completed: false,
      }).data;

      // POST 요청 보내기
      axios.post('/api/todos/', todoData)
        .then(response => {
          // todo 생성 성공 시, 입력창 초기화
          this.title = null;
          // todo list 갱신
          this.$emit('created', response.data);
        })
        .catch(error => console.log(error));
    },
  },
}
</script>