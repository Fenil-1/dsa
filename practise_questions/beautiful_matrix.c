#include<stdio.h>
#include<stdlib.h>
int main(){

int m1[5][5];
int x;
int a,b;
int result;

for(int i=1;i<=5;i++){
    for(int j=1;j<=5;j++){
        printf("enter");
        scanf("%d",&x);
        m1[i][j]=x;
        if(x==1){
            a=i;
            b=j;
    }
}
}
for(int i=1;i<=5;i++){
    for(int j=1;j<=5;j++){
        printf("%d ",m1[i][j]);
        }
    printf("\n");
}

result = abs(3-a) + abs(3-b);
printf("%d",result);
return 0;
}



