var isUnivalTree = function(root) {
	if (root) {
		if (root.left && root.left.val != root.val){
			return false;
		}
		if (root.right && root.right.val != root.val){
			return false;
		}
		return isUnivalTree(root.left) && isUnivalTree(root.right);
	}
	return true;
};