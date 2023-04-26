// axios.(a)('https://api.example.com/data')
// 	.(b)(function (response) {
// 	console.log((c))
// })
axios.get('https://api.example.com/data')
	.then(function (response) {
	console.log(response)
})

//동기함수: 한 작업이 실행되는 동안 다른 작업은 멈추고 자신의 차례를 기다림
//비동기함수: 요청이 끝날 때까지 기다리는 것이 아니라 응답에 관계없이 바로 다음 동작 실행