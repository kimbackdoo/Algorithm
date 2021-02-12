#include <stdio.h>
#include <stdlib.h>
void find(int startNum,int endNum); /*
	C언어는 절차지향 언어이기 때문에 find 함수가 main 함수 이후에 정의되는 것을
	컴파일러에게 알리기 위해 find 함수의 원형 선언
*/
void main(){
	int startNum, endNum; //입력 값 변수 
	//printf("범위 입력 해주세요 : ");
	//scanf("%d",&startNum); //범위 값 입력 
	//scanf("%d",&endNum);
	//find(startNum,endNum); //소수 찾기 함수 
	find(2,1000000);
	
	
}
void find(int startNum, int endNum){
	int cnt=0;   //카운트 변 수  
	int i,j;   //for문 변수  
	int *check = malloc(sizeof(int) * endNum); //동적할당  check는  약수확인변 수  
   
	for(i=startNum; i<=endNum; i++) check[i]=0;  //0으로 초기 화  
	check[1] = 1;
	for(i=startNum; i<=endNum; i++){
    	for(j=2; j<=i/2; j++){
        	if(i%j==0) {
            	check[i]++;
        	break; //1을 제외한 약수가 존재할때마다 check[i]++ 이후 루프 탈출 
        	}
    	}
	}
   
	for(i=startNum; i<=endNum; i++){
    	if(check[i]==0) {   //소수일 때  
        	cnt++;
        //	printf("%d ",i);
    	}
	}
   
	printf("\n소수 갯수 : %d", cnt);
	free(check);
}




