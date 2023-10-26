function debounce(fn, t) {
	let timer = null
	
	return function(...args) {
		if (timer) {
			clearTimeout(timer)
		}
		timer = setTimeout(() => {
			timer = null
			fn(...args)
		}, t)
	}
};