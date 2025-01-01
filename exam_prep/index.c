#include<stdio.h>
int main(){
    int array[5]={};
    int max=0;
    int i=1;
    int x;
    for(int i=1;i<6;i++){
        printf("Enter a number : ");
        scanf("%d",&x);
        array[i]=x;

    }
    while(i < 5){
        if(array[i]>=max){
            max=array[i];
            i++;
        }
        else{
            i++;
        }
    }
    printf("%d",max);
    return 0;
}   