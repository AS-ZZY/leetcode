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
bool judgeCircle(char* moves) {
    int w = 0;
    int h = 0;
    int len = strlen(moves);
    for(int i=0;i<len;i++)
        {
            if(moves[i]=='R') w++;
            else if(moves[i]=='L') w--;
            else if(moves[i]=='U') h++;
            else if(moves[i]=='D') h--;
        }

    if(w == 0&&h == 0)
        return true;
    else
        return false;
}






