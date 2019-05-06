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
bool lemonadeChange(int* bills, int billsSize) {
    int num_5=0,num_10=0;
    int i;
    for(i=0;i<billsSize;i++)
    {
    	if(bills[i]==5)
		{
    		num_5++;
		}
		else if(bills[i]==10)
		{
			num_5--;
			num_10++;
		}
		else
		{
			if(num_10==0)
				num_5-=3;
			else
			{
				num_10--;
				num_5--;
			}
		}
    	if(num_5<0||num_10<0)
    		break;
	}
	if(i==billsSize)
		return true;
	else
		return false;
}





