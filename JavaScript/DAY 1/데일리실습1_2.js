// 알고리즘 연습, 회문 검사 함수

words = ['level', 'noon', 'mom', 'happy', 'ssafy', 'life']

function palindrome(word) {
    for (let i=0; i<word.length/2;i++){
        // 역순으로 바꾸기
        const reversed = word.split('').reverse().join(''); //배열변환,역순,문자화
        // 같은지 확인
        return reversed===word ? true : false;
    }
    
  }
  
for (const word of words) {
  console.log(palindrome(word))
}

// 출력 예시
// true
// true
// true
// false
// false
// false
