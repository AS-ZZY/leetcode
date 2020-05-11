var findSecondMinimumValue = function(root) {
	if(!root || !root.left){
		return -1;
	}
	return findVal(root, root.val);
};

var findVal = function(root, val) {
	if(!root) return -1;
	if(root.val > val){
		return root.val;
	}
	var left = findVal(root.left, val);
	var right = findVal(root.right, val);
	if(left < 0) return right;
	if(right< 0) return left;
	return Math.min(left, right);
};