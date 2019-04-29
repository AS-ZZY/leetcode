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
    int all = 0;
    for(int i = 0;i < pricesSize - 1;i++)
    {
        if(prices[i] < prices[i + 1])
            all += (prices[i + 1] - prices[i]);
    }
    return all;
}






