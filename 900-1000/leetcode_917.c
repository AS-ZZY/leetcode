bool is(char s);
char* reverseOnlyLetters(char* S) {
    int i,j;
    char a;
    i = 0;
    j = strlen(S) - 1;
    while(i < j)
    {
        while(i < j&&!is(S[i]))
            i++;
        while(i < j&&!is(S[j]))
            j--;
        a = S[j];
        S[j] = S[i];
        S[i] = a;
        i++;
        j--;
    }
    return S;
}
bool is(char s)
{
    if(s <= 'Z'&&s >= 'A')
        return true;
    if(s <= 'z'&&s >= 'a')
        return true;
    return false;
}