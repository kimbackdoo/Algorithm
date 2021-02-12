#include <stdio.h>
#include <stdlib.h>
#include <math.h>
void find(int startNum,int endNum); /*
	C언어는 절차지향 언어이기 때문에 find 함수가 main 함수 이후에 정의되는 것을
	컴파일러에게 알리기 위해 find 함수의 원형 선언
*/
void main(){
	int startNum, endNum; //입력 값 변수 
	printf("범위 입력 해주세요 : ");
	scanf("%d",&startNum); //범위 값 입력 
	scanf("%d",&endNum);
	find(startNum,endNum); //소수 찾기 함수 
}
void find(int startNum, int endNum){
	int cnt=0;   //소수갯수 cnt변수 
	int i,j;   //for문 변수  
	int *check = malloc(sizeof(int) * endNum); //동적할당  
   
	for(i=startNum; i<=endNum; i++) check[i]=0;  //약수확인변수 초기화  --> 배열 선언과 동시에 초기화
	check[1] = 1;  //1은 소수가 아니므로 1 입력  
	for(i=startNum; i<=endNum; i++){
    	for(j=2; j<=sqrt(i); j++){  //제곱근 이후의 수는 확인할 필요가 없기 때문에 제곱근 까지 탐색  
        	if(i%j==0) {
            	check[i]++;  
        	break; //1을 제외한 약수가 존재할때마다 check[i]++ 
        	}
    	}
	}
   
	for(i=startNum; i<=endNum; i++){
    	if(check[i]==0) {   //소수일 때  
        	cnt++;
        	printf("%d ",i);
    	}
	}
   
	printf("\n소수 갯수 : %d", cnt);
	free(check);
}




