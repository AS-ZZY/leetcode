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
double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int i=nums1Size+nums2Size,j,size=0,a=0,b=0,l=0;
	double s1,s2;
    if(i%2==0)
		j=i/2;
	else
		j=(i+1)/2;
	while(a<nums1Size||b<nums2Size)
	{
		if(a<nums1Size&&b<nums2Size)
		{
			if(nums1[a]<nums2[b])
			{
				s1=nums1[a];
				a++;
				l++;

			}
			else
			{
				s1=nums2[b];
				b++;
				l++;
			}
		}
		else if(a<nums1Size&&b==nums2Size)
		{
			s1=nums1[a];
			a++;
			l++;
		}
		else
		{
			s1=nums2[b];
			b++;
			l++;
		}
		if(i%2==1)
		{
			if(l==j)
				break;
		}
		else
		{
			if(l==j)
				s2=s1;
			else if(l==j+1)
			{
				s1=(s1+s2)/2;
				break;
			}
		}
	}
	return s1;
}













