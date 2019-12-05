var repeatedNTimes = function(A) {
	for ( var i = 1; i < A.length; i++ ){
		if (A[i] == A[i - 1]){
			return A[i];
		}
	}
	if (A[0] == A[2] || A[0] == A[3]){
		return A[0];
	}
	return A[1];
};