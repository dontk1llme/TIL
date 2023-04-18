const nums = [1, 2, 3, 4]

// for문으로 처리
for (let i=0; i<nums.length; i++){
    nums[i]=nums[i]**3;
}
console.log(nums)

//map 사용
const nums2 = [1, 2, 3, 4]
let nums3 = nums2.map(function(element){
    return element**3;
});
console.log(nums3);