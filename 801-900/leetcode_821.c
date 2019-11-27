#define MIN(a, b) a < b ? a : b

int* shortestToChar(char * S, char C, int* returnSize){
    *returnSize = strlen(S);
    int *ans = (int*)malloc(*returnSize * sizeof(int));
    char* front = S, rear = S;
    for(int i = 0; i < *returnSize; ++i)
    {
        if(S[i] == C)
        {
            ans[i] = 0;
            continue;
        }
        int left = i - 1, right = i + 1;
        while(left >= 0 && S[left] != C)
            --left;
        while(right < *returnSize && S[right] != C)
            ++right;
        if(!i || left < 0)
            ans[i] = right - i;
        else if(i + 1 == *returnSize || right >= *returnSize)
            ans[i] = i - left;
        else
            ans[i] = MIN(i - left, right - i);
    }
    return ans;
}