#include <stdio.h>
#include <stdlib.h>
#define bool int
#define false 0
#define true 1
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
bool isBadVersion(int version);

int firstBadVersion(int n) {
    int t,f = 1,e = n;
	while(1)
    {
    	t = f / 2 + e / 2;
		if(isBadVersion(t) == true)
		{
			if(isBadVersion(t - 1) == false)
                break;
			else
				e = t - 1;
		}
		else
		{
			if(isBadVersion(t + 1) == true)
            {
                t += 1;
                break;
            }
			else
				f = t + 1;
		}
	}
	return t;
}






