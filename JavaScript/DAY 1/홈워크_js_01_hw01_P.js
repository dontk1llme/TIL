// 1번
const nums = [1,2,3,4,5,6,7,8]

console.log('1번 출력 결과')
for ( i = 0; i < nums.length; i++) {
  console.log('nums[' + i + ']: ' + nums[i])
}
console.log()
// for (const i = 0; i < nums.length; i++) {
//                                     ^ 
// -> i가 const라서 ++가 적용이 안 된다
// TypeError: Assignment to constant variable.

// 2번
console.log('2번 출력 결과')
// for (num in nums) {
for (num of nums) {
  console.log(num, typeof num)
  // 출력 결과
  // 0 string
  // 1 string
  // 2 string
  // 3 string
  // 4 string
  // 5 string
  // 6 string
  // 7 string
}

/*
in 하면 키값 -> 인덱스 -> str
of 하면 벨류값 -> number
*/ 