#include<stdio.h>
int main()
{
	int pos,n,i,j,bt[20],pr[20],tat[20],wt[20],sum1,sum2,awt=0,atat=0;
	printf("enter no. process");
	scanf("%d",&n);
	printf("burst times");
	for (i=0;i<n;i++)
	{
		scanf("%d",&bt[i]);
	}
	printf("priorities");
	for(i=0;i<n;i++)
	{
		scanf("%d",&pr[i]);
	}
	for (i=0;i<n;i++)
	{
		pos=i;
		for(j=i+1;j<n;j++)
		{
			if(pr[j]<pr[pos])
			{
				pos=j;
			}
		}
		int t=pr[i];
		pr[i]=pr[pos];
		pr[pos]=t;
		
		t=bt[i];
		bt[i]=bt[pos];
		bt[pos]=t;
	}
	wt[0]=0;
	printf("\nprocess\tburst time\tpriority\twaiting time\tturnaround time");
	for(i=0;i<n;i++)
	{
		wt[i]=0;
		tat[i]=0;
		for(j=0;j<n;j++)
		{
			wt[i]=wt[i]+bt[j];
		}
		tat[i]=wt[i]+bt[i];
		awt=awt+wt[i];
		atat=atat+tat[i];
		printf("\np%d\t%d\t\t%d\t\t%d\t\t%d",i+1,bt[i],pr[i],wt[i],tat[i]);
	}
	printf("\navh waiting time is %d",awt/n);
	printf("\navg turnaround time is %d",atat/n);
}
