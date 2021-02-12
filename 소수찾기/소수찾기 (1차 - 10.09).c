#include <stdio.h>
void find(int startNum,int endNum); /*
	C언어는 절차지향 언어이기 때문에 find 함수가 main 함수 이후에 정의되는 것을
	컴파일러에게 알리기 위해 find 함수의 원형 선언
*/
void main(){
	int startNum, endNum; //입력 값 변수 
	//printf("범위 입력 해주세요 : ");
	//scanf("%d",&startNum); //범위 값 입력 
	//scanf("%d",&endNum);
	find(1,1000000); //소수 찾기 함수 	
}

void find(int startNum,int endNum){
	int measure[endNum],cnt=0;   //약수 확인 배열 measure, 소수갯수 cnt변수 
	int i,j;      //for문 변 수  
	for(i=startNum;i<=endNum;i++) measure[i]=0;  //약수확인변수 초기화  
	for(i=startNum;i<=endNum;i++){
		
		for(j=2;j<=i;j++){
			if(i%j==0) measure[i]++;  //1을 제외한 약수가 존재할때마다 measure[i]++ 
		}
	}
	for(i=startNum;i<=endNum;i++){
		if(measure[i]==1) {   //약수가 1개일때 소수갯수증가, 그 숫자 출력  
		cnt++;		
		printf("%d ",i);
		}
	}
	printf("소수 갯수 : %d",cnt);
}




