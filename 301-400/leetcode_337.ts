
class TreeNode {
	val: number
	left: TreeNode | null
	right: TreeNode | null
	constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
		this.val = (val===undefined ? 0 : val)
		this.left = (left===undefined ? null : left)
		this.right = (right===undefined ? null : right)
	}
}

function calcRob(root: TreeNode | null) {
	if(!root) {
		return {
			rob: 0,
			notRob: 0
		}
	} else {
		const left = calcRob(root.left)
		const right = calcRob(root.right)
		return {
			rob: root.val + left.notRob + right.notRob,
			notRob: Math.max(left.rob, left.notRob) + Math.max(right.rob, right.notRob)
		}
	}

}

function rob(root: TreeNode | null): number {
	const { rob, notRob } = calcRob(root)
	return Math.max(rob, notRob)
};
