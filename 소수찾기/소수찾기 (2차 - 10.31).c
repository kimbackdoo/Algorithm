#include <stdio.h>
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
	int measure[endNum], cnt=0;   //약수 확인 배열 measure, 소수갯수 cnt변수 
	int i,j;   //for문 변수  
   
	for(i=startNum; i<=endNum; i++) measure[i]=0;
	measure[1] = 1; 
	for(i=startNum; i<=endNum; i++){
    	for(j=2; j<=i/2; j++){
        	if(i%j==0) {
            	measure[i]++;  //1을 제외한 약수가 존재할때마다 measure[i]++ , i/2까지만 탐색했을 때 약수가 존재하면 measure[i]=1 없으면 0 즉  소수  
        	break;
        	}
    	}
	}
   
	for(i=startNum; i<=endNum; i++){
    	if(measure[i]==0) {   //소수일 때 
        	cnt++;
        	printf("%d ",i);
    	}
	}
   
	printf("\n소수 갯수 : %d", cnt);
}




