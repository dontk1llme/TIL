//1793. 데일리과제 2-2. JS 알고리즘 기초 실습 - 별찍기2
// https://velog.io/@wldns12378/JS-%EB%B3%84-%EC%B0%8D%EA%B8%B0star

let case4 = function (n) {
    // console.log(`[case4] 입력된 수: ${n}`);
    for (let i = 1; i <= n; i++) {
      let floor = '';
      for (let j = 1; j < n; j++) {
        if (n - i < j) {
          floor += '**';
        } else {
          floor += ' ';
        }
      }
      floor += '*';
      console.log(floor);
    }
  }
  
  case4(5);
  console.log();