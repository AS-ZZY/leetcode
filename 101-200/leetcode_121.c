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
int maxProfit(int* prices, int pricesSize){
    if(pricesSize == 0)
        return 0;
    int min = prices[0],all = 0;
    for(int i = 1;i < pricesSize;i++)
    {
        if(min < prices[i])
            all = all > prices[i] - min ? all : prices[i] - min;
        else
            min = prices[i];
    }
    return all;
}






