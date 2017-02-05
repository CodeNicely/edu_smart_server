//15115006 4th sem Aditya Agrawal
#include<stdio.h>
int main()
{
    printf("Aditya Agrawal\n15115006\n");
	int store[10000];
int n;
printf("enter size of array\n");
scanf("%d",&n);

int i,j;
printf("enter elements of array\n");
for(i=0;i<n;i++)
{
printf("enter %d element of array\n",i+1);
scanf("%d",&store[i]);
}

for(i=0;i<n;i++)
{
int tmp=store[i],jj,check=0;
for(j=i+1;j<n;j++)
if(store[j]<tmp){check=1;tmp=store[j];jj=j;}
if(check==1){
store[jj]=store[i];
store[i]=tmp;}
}
for(i=0;i<n;i++)
printf("%d ",store[i]);
int l,r,mid,flag=0,x;
l=0;r=n-1;
printf("enter element to search\n");
scanf("%d",&x);
while(l<=r)
{
//printf("..%d %d..\n",l,r);
mid=(l+r)/2;
if(store[mid]==x){//printf("qw\n");
flag=1;break;}
if(store[mid]>x)r=mid-1;
if(store[mid]<x)l=mid+1;
}
if(flag==1)printf("at index %d\n",mid+1);
else printf("not found\n");
}
