// https://taewow.tistory.com/12
const inputs = [
    [3, 10, 5, [1, 3, 5, 7, 9]],    // 3
    [3, 10, 5, [1, 3, 7, 8, 9]],    // 0
    [5, 20, 5, [4, 7, 9, 14, 17]],  // 4
  ]

  function solution(K, N, M, chargers) {
    let now = 0;
    let can_go = now + K;
    let charge_station = 0;
    let count = 0;

    //2
    while (can_go < N) {
        //3
        for (let i of chargers) {
            if (now < i && i <= can_go) {
                charge_station = i;
            } else if (can_go < i) {
                break;
            }
        }
        //4
        if (charge_station == 0) {
            count = 0;
            break;
        }
        //5
        now = charge_station;
        can_go = now + K;
        count++;
        charge_station = 0;
    }

    console.log(`#${count}`);
  }
  
  for (const input of inputs) {
    solution(input[0], input[1], input[2], input[3])
  }