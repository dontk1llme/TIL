const inputs = [
    [3, 10, 5, [1, 3, 5, 7, 9]],    // 3
    [3, 10, 5, [1, 3, 7, 8, 9]],    // 0
    [5, 20, 5, [4, 7, 9, 14, 17]],  // 4
  ]

  function solution(K, N, M, chargers) {
    let count = 0
    let current = 0
    while (current + K < N) {
        for (let step = K; step > 0; step--) {
          if (chargers.includes(current + step)) {
            console.log(`#${count},${current}`)
            current += step;
            count++;
            console.log(`#${count},${current}`)
            break;
          }
        }
  
        if (current + K <N) break;
        console.log(`왓냐?`)
        count = 0;
        break;
      }
    console.log(`#${count}`)
  }
  
  for (const input of inputs) {
    solution(input[0], input[1], input[2], input[3])
  }