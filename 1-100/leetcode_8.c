#define int_max (-(int_min+1))
#define int_min -2147483648
int myAtoi(char* str){
    int i,n = 0,odd = 0,start = 0,big = 0;
    int a;
    for(i = 0;i <strlen(str);i++)
    {
        if(odd == 0&&start == 0&&str[i] == '-'&&i < strlen(str) - 1)
        {
             if(str[i+1] >= '0'&&str[i+1] <= '9')
                odd = 1;
            start = 1;
        }
        else if(str[i] >= '0'&&str[i] <= '9')
        {
            a = str[i] - '0';
            if(odd == 1&&((n > 214748364)||(n == 214748364&&a >= 8)))
            {
                big = 1;
                n = int_min;
                break;
            }
            else if((n > 214748364)||(n == 214748364&&a >= 7))
            {
                n = int_max;
                break;
            }
            else
                n = n * 10 + a;
            start = 1;
        }
        else if(start == 1&&(str[i] < '0'||str[i] > '9'))
            break;
         else if(str[i]=='+')
            start = 1;
        else if(start == 0&&(str[i] < '0'||str[i] > '9')&&str[i]!=' ')
            break;
    }
    if(big == 0&&odd == 1)
        n = -n;
    if(start == 1)
        return n;
    else
        return 0;
}
