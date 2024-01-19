// Step 1: Start the Program.
// Step 2: Input the number of processes.
// Step 3: Input the burst time and priority for each process.
// Step 4: Sort the element on the basis of priority.
// Step 5: Print order of execution of their process with their time stamp (wait time and turnaround time).
// Step 6: End the Program.

#include <stdio.h>
void swap(int *a,int *b)
{
    int temp=*a;
    *a=*b;
    *b=temp;
}
int main()
{
    int n;
    printf("Enter Number of Processes: ");
    scanf("%d",&n);
    int b[n],p[n],index[n];
    for(int i=0;i<n;i++)
    {
        printf("Enter Burst Time and Priority Value for Process %d: ",i+1);
        scanf("%d %d",&b[i],&p[i]);
        index[i]=i+1;
    }
    for(int i=0;i<n;i++)
    {
        int a=p[i],m=i;
        for(int j=i;j<n;j++)
        {
            if(p[j] > a)
            {
                a=p[j];
                m=j;
            }
        }
        swap(&p[i], &p[m]);
        swap(&b[i], &b[m]);
        swap(&index[i],&index[m]);
    }
    int t=0;
    printf("Order of process Execution is\n");
    for(int i=0;i<n;i++)
    {
        printf("P%d is executed from %d to %d\n",index[i],t,t+b[i]);
        t+=b[i];
    }
    printf("\nProcess Id\t Burst Time\t Waiting Time\t   Turnaround Time");
    int wait_time=0;
    for(int i=0;i<n;i++)
    {
        printf("\n p%d\t\t    %d\t\t   %d\t\t\t %d",index[i],b[i],wait_time,wait_time + b[i]);
        wait_time += b[i];
    }
    printf("\n");
    return 0;
}


// Enter Number of Processes: 3
// Enter Burst Time and Priority Value for Process 1: 10 2
// Enter Burst Time and Priority Value for Process 2: 5 0
// Enter Burst Time and Priority Value for Process 3: 8 1
// Order of process Execution is
// P1 is executed from 0 to 10
// P3 is executed from 10 to 18
// P2 is executed from 18 to 23