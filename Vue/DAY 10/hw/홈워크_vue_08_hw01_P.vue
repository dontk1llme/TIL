methods: {
  login: function () {
      axios(...생략...)
      .then(res => {
	const token = res.data.access
        // 이곳에 들어갈 코드를 작성하시오.
        localStorage.setItem('jwt', token);
      })
  }