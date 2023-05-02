<template>
  <div class="container">
    <h1>버튼 박스 제작</h1>
    <div id='box'>

      <h2>예약 페이지</h2>
      <h3>시간 선택</h3>
      <div class="time-box">
        <button
          v-for="time in times"
          :key="time"
          :class="{ 'time-btn': true, 'selected': selectedTimes.includes(time) }"
          @click="selectTime(time)"
        >
          <!-- 위에서 뺐음 :disabled="selectedTimes.length >= 5 && !selectedTimes.includes(time)" -->
          {{ time }}
        </button>
      </div>
    </div>
    <hr>
    <div class="selected-times">
      <h3>선택한 시간</h3>
      <span v-for="time in selectedTimes" :key="time">{{ time }}  </span>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      times: [
        "09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30",
        "14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30",
        "19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30",
      ], // 09:00 부터 23:30 까지 30분 단위로 저장하는 배열
      selectedTimes: [] // 선택한 시간들을 저장하는 배열
    }
  },
  methods: {
    selectTime(time) {
      if (this.selectedTimes.includes(time)) {
        // 이미 선택된 시간인 경우
        this.selectedTimes = this.selectedTimes.filter(selectedTime => selectedTime !== time)
      } else {
        // 선택되지 않은 시간인 경우
        if (this.selectedTimes.length >= 5) {
          alert('5개 이상 선택할 수 없습니다.')
        } else {
          this.selectedTimes.push(time)
        }
      }
    }
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR&display=swap');
*{
  font-family: 'Noto Sans KR', sans-serif !important
}

.container {
  text-align: center;
}
#box{
  border: 1px solid #333232;
}
.time-box {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  margin: 20px auto;
  width: 80%;
}
.time-btn {
  background-color: #f0f0f0;
  border: 1px solid #ddd;
  border-radius: 5px;
  color: #333;
  font-size: 16px;
  margin: 5px;
  padding: 10px 20px;
  transition: background-color 0.3s;
}
.selected {
  background-color: #658dc63d;
  border-color: #658dc63d;
  color: #0F4C81;
}
</style>