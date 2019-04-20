var lengthOfLastWord = function(s) {
	var i = s.length - 1;
	var len = 0;
	for(;i >= 0;i--)
	{
		if(i == s.length - 1 && is_letter(s[i]))
			len++;
		else if(is_letter(s[i]))
			len++;
		else if(!is_letter(s[i]) && len != 0)
			break;
	}
	return len;
};
function is_letter(a){
	if((a > 'a' && a < 'z')||(a > 'A' && a < 'Z'))
		return true;
	else
		return false;
};
