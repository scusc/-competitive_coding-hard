#include<iostream>
using namespace std;
int main()
{
	int i,j,n,b,m;
	char c[100];
	int num,count=0,a[10];
	cout<<"enter no. of base addresses";
	cin>>n;
	cout<<"\n enter total no. of bytes per page";
	cin>>b;
	cout<<"enter total no. bytes in memory";
	cin>>m;
	cout<<"enter base address:\n";
	for (i=0;i<n;i++)
	{
		cout<<"p"<<i;
		cin>>a[i];
	}
	num=n*b;
	cout<<"enter input for the position";
	for (i=0;i<num;i++)
	{
		cout<<i;cin>>c[i];
	}
	cout<<"pages in pysical address\n";
	for(i=0;i<n;i++)
	{
		for (j=0;j<b;j++)
		{
			if((a[i]*b)+(j%b)>m)
			{
				cout<<"could not be stored as storage as value exceded ";cout<<m;		
			}
			count++;
			continue;
		}
		cout<<((a[i]*b)+j%b)<<c[count]<<"\n";
		count++;
	}
}
