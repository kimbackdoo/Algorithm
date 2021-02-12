#include <stdio.h>
#include <stdlib.h>
#include <math.h>
void find(int startNum,int endNum); /*
	C언어는 절차지향 언어이기 때문에 find 함수가 main 함수 이후에 정의되는 것을
	컴파일러에게 알리기 위해 find 함수의 원형 선언
*/

void find(int, int);

int main(){
    int startNum, endNum; //입력 값 변수 
    printf("범위 입력 해주세요 : ");
    scanf("%d",&startNum); //범위 값 입력
    scanf("%d",&endNum); //범위 값 입력
    find(startNum, endNum);
}

void find(int startNum, int endNum){
	int cnt=0;   //소수갯수 cnt변수 
	int i,j;   // for문 변수  
	int *check = (int*)calloc(endNum, sizeof(int)); // calloc을 이용하여 배열 동적할당 및 0으로 초기화 
	check[1] = 1;
      
      
    for(i=2; i<=sqrt(endNum); i++){  //제곱근 이후의 수는 탐색할필요 없기 때문에 제곱근 까지 탐색  
    	
        if(check[i]) continue;  //소수가 아닐경우 continue 
             
    	for(j=2; i*j<=endNum; j++) //소수인 i의 배수는 소수가 아니므로 1 입력  
        	check[i*j] = 1;
    	}
   
    	for(i=startNum; i<=endNum; i++){
    	if(check[i]==0) {   //소수일 때  
        	cnt++;   //카운트 증가  
        //	printf("%d ", i); //출력   
    	}
	}
   
   printf("\n소수 갯수 : %d", cnt);
   free(check);
}




