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
#define INT_MAX 2147483647
#define INT_MIN (-INT_MAX - 1)
int reverse(int x) {
    int i;
    int j = x;
    int n = 0;
    while(j > 0)
    {
        i = j % 10;
        if((n > INT_MAX / 10)||(n == INT_MAX /10&&i > 7))
            return 0;
        else
        {
            n = n * 10 + i;
            j /= 10;
        }
    }
    while(j < 0)
    {
        i = j % 10;
        if((n < INT_MIN /10)||(n == INT_MIN&&i<-8))
            return 0;
        else
        {
            n = n * 10 + i;
            j /= 10;
        }
    }
    return n;
}













