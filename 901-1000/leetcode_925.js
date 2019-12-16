var isLongPressedName = function(name, typed) {
	if ( name.length > typed.length ) {
		return false;
	}
	if (name[0] !== typed[0]){
		return false;
	}
	var i = 1;
	var j = 1;
	for( ; i < name.length && j < typed.length; j++){
		if ( name[i] !== typed[j] ) {
			if (typed[j] !== typed[j - 1]) {
				return false;
			}
		}
		else {
			i++;
		}
	}
	if ( i === name.length ) {
		for ( ; j < typed.length ; j++ ){
			if (typed[j] !== typed[j - 1]){
				return false;
			}
		}
		return true;
	}
	return false;
};