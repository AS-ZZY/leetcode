bool backspaceCompare(char* S, char* T)
{
    int k;
    char s1[200],t1[200];
    ex(S,s1);
    ex(T,t1);
    printf("%s\n",s1);
    printf("%s\n",t1);
    k=strcmp(s1,t1);
    if(k==0)
        return true;
    else
        return false;
    
}
void ex(char* s,char *s1)
{
	int i,j=-1;
	for(i=0;i<strlen(s);i++)
	{
		if(s[i]!='#')
		{
			j++;
			s1[j]=s[i];	
				
		}	
		else
		{
			if(j!=-1)
			{
				s1[j]='\0';
				j--;
			}
		}
	}
	j++;
	s1[j]='\0';
}
