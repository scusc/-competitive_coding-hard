#include<iostream>
using namespace std;
struct Queue
{
int a[10];
int r;
int l;
}q;
int main()
{
int p,f,i,j,t,c1=0,c2=0,k=0;
cout<<"Enter Number of Pages:";
cin>>p;
cout<<"Enter Number of Frames:";
cin>>f;
int rs[p],h=100;
cout<<"Enter Reference String:";
for(i=0;i<p;i++)
cin>>rs[i];
q.r=0;
t=0;
q.l=0;
for(i=0;i<p;i++)
{
for(j=0;j<f;j++)
{
if(rs[i]==q.a[j])
{
c1++;
k--;
break;
}
}
if(j==f)
{
if(q.l!=f)
{
q.a[q.l]=rs[i];
        q.l++;
}
else
{
if(t!=q.l)
{
q.a[t]=rs[i];
t++;
}
if(t==q.l)
t=0;
}
}
for(j=0;j<f;j++)
cout<<q.a[j]<<" ";
if(h!=k)
cout<<"Page fault :"<<k+1<<"\n";
else
cout<<"\n";
h=k;
k++;
}
cout<<"Number of page faults:"<<p-c1<<"\n";
cout<<"Hit Ratio:"<<c1<<"\n";
cout<<"Miss Ratio:"<<k<<"\n";
return 0;
}
