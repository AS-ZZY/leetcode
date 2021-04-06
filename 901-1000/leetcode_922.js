var sortArrayByParityII = function (A) {
	var odd = [];
	var even = [];
	for (var i = 0; i < A.length; i++) {
		if (A[i] % 2 != 0) {
			odd.push(A[i]);
		}
		else {
			even.push(A[i]);
		}
	}
	for (var i = 0; i < odd.length; i++) {
		A[i * 2] = even[i];
		A[i * 2 + 1] = odd[i]
	}
	return A;
}