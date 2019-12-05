var rangeSumBST = function(root, L, R) {
	if (!root) {
		return 0;
	}
	else if (root.val <= L){
		return rangeSumBST(root.right, L, R) + ( root.val == L ? L : 0 );
	}
	else if (root.val >= R){
		return rangeSumBST(root.left, L, R) + ( root.val == R ? R : 0 );
	}
	else{
		return rangeSumBST(root.left, L, R) + rangeSumBST(root.right, L, R) + root.val;
	}
};