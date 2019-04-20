#include <stdio.h>
#include <stdlib.h>
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
struct ListNode {
    int val;
    struct ListNode *next;
 };
int main()
{
    return 0;
}
bool isUgly(int num) {
    int n = num;
	while(n % 2 == 0 || n % 3 == 0 || n % 5 == 0)
	{
		if(n % 2 == 0)
			n /= 2;
		if(n % 3 == 0)
			n /= 3;
		if(n % 5 == 0)
			n /= 5;
        if(n == 0)
            break;
	}
	if(n == 1)
		return true;
	else
		return false;
}
















