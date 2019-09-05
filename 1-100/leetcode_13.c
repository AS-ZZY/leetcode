char* longestCommonPrefix(char** strs, int strsSize) {
    int i,j;
    if(strsSize == 1)
        return strs[0];
    for(i = 0;;i++)
    {
        for(j = 1;j < strsSize;j++)
        {
            if(strs[j][i] == '\0'||strs[j][i] != strs[j - 1][i])
                break;
        }
        if(j != strsSize)
            break;
    }
    char* s = (char*)malloc(sizeof(char) * (i + 1));
    for(j = 0;j < i;j++)
        s[j] = strs[0][j];
    s[i] = '\0';
    return s;
}
