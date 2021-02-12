1차
#include <stdio.h>

/*
	C언어는 절차지향 언어이기 때문에 find 함수가 main 함수 이후에 정의되는 것을
	컴파일러에게 알리기 위해 find 함수의 원형 선언
*/
void find(int, int);

void main(){
	int startNum, endNum; // 입력 값 변수
	printf("범위 입력 해주세요 : ");
	scanf("%d %d", &startNum, &endNum); // 범위 값 입력
	find(startNum,endNum); // 소수 찾기 함수
}

void find(int startNum,int endNum){
	int measure[endNum], cnt=0; // 약수 확인 변수measure, 소수갯수 cnt변수
	int i,j; // for문 변수

	for(i=startNum;i<=endNum;i++) measure[i]=0; // 약수확인변수 초기화
	
	for(i=startNum;i<=endNum;i++){
		for(j=2;j<=i;j++){
			if(i%j==0) measure[i]++; // 1을 제외한 약수가 존재할때마다 measure[i]++
		}
   	}
   
	for(i=startNum;i<=endNum;i++){
		if(measure[i]==1) { // 약수가 1개일때 소수갯수증가, 그 숫자 출력  
			cnt++;      
			printf("%d\n",i);
    		}
	}
	
	printf("소수 갯수 : %d",cnt);
}

2차
#include <stdio.h>

/*
	C언어는 절차지향 언어이기 때문에 find 함수가 main 함수 이후에 정의되는 것을
	컴파일러에게 알리기 위해 find 함수의 원형 선언
*/
void find(int, int);

void main(){
	int startNum, endNum; // 입력 값 변수 
	printf("범위 입력 해주세요 : ");
	scanf("%d %d", &startNum, &endNum); // 범위 값 입력 
	find(startNum,endNum); // 소수 찾기 함수 
}

void find(int startNum, int endNum){
	int measure[endNum], cnt=0; // 약수 확인 배열 measure, 소수갯수 cnt변수 
	int i, j; // for문 변수  
   
	for(i=startNum; i<=endNum; i++) measure[i]=0;
	
	for(i=startNum; i<=endNum; i++){
		for(j=2; j<=i/2; j++){
        		if(i%j==0) {
            			measure[i]++;
            			break; // 1을 제외한 약수가 존재할때마다 measure[i]++
         		}
       		}
   	}
   	
	for(i=startNum; i<=endNum; i++){
		if(measure[i]==0) { // 약수가 1개일때 소수갯수증가, 그 숫자 출력
    			cnt++;
    			printf("%d ",i);
    		}
	}

	printf("\n소수 갯수 : %d", cnt);
}

3차
#include <stdio.h>
#include <stdlib.h>

/*
	C언어는 절차지향 언어이기 때문에 find 함수가 main 함수 이후에 정의되는 것을
	컴파일러에게 알리기 위해 find 함수의 원형 선언
*/
void find(int, int);

void main(){
	int startNum, endNum; // 입력 값 변수 
	printf("범위 입력 해주세요 : ");
	scanf("%d %d", &startNum, &endNum); // 범위 값 입력 
	find(startNum,endNum); // 소수 찾기 함수 
}

void find(int startNum, int endNum){
	int cnt=0; // 카운트 변수  
	int i, j; // for문 변수  
	int *check = (int*)malloc(sizeof(int) * endNum); //동적할당 check는 약수확인변수  
	
	for(i=startNum; i<=endNum; i++) check[i]=0;  //약수확인변수 초기화
   
	for(i=startNum; i<=endNum; i++){
		for(j=2; j<=i/2; j++){
			if(i%j==0) {
            			check[i]++;
            			break; // 1을 제외한 약수가 존재할때마다 check[i]++ 이후 루프 탈출 
			}
		}
   	}
   
   	for(i=startNum; i<=endNum; i++){
      		if(check[i]==0) { // 약수가 1개일때 소수갯수증가, 그 숫자 출력  
         		cnt++;
			printf("%d ",i);
		}
	}
   
   	printf("\n소수 갯수 : %d", cnt);
   	free(check);
}

4차
#include <stdio.h>
#include <stdlib.h> 
#include <math.h>

/*
	C언어는 절차지향 언어이기 때문에 find 함수가 main 함수 이후에 정의되는 것을
	컴파일러에게 알리기 위해 find 함수의 원형 선언
*/
void find(int, int);

void main(){
	int startNum, endNum; // 입력 값 변수 
	printf("범위 입력 해주세요 : ");
	scanf("%d %d", &startNum, &endNum); // 범위 값 입력 
	find(startNum,endNum); // 소수 찾기 함수 
}

void find(int startNum, int endNum){
	int cnt=0; // 소수갯수 cnt변수 
	int i, j; // for문 변수  
	int *check = (int*)malloc(sizeof(int) * endNum); //동적할당  
	
	for(i=startNum; i<=endNum; i++) check[i]=0; // 약수확인변수 초기화
	check[1] = 1; // 1은 소수가 아니므로 1 입력
   
	for(i=startNum; i<=endNum; i++){
    		for(j=2; j<=sqrt(i); j++){ // 제곱근 이후의 수는 확인할 필요가 없기 때문에 제곱근 까지 탐색  
        		if(i%j==0) {
            			check[i]++;  
            			break; // 1을 제외한 약수가 존재할때마다 check[i]++ 
         		}
       		}
   	}
   
	for(i=startNum; i<=endNum; i++){
		if(check[i]==0) { // 약수가 1개일때 소수갯수증가, 그 숫자 출력  
        		cnt++;
        		printf("%d ",i);
       		}
   	}
   	
	printf("\n소수 갯수 : %d", cnt);
	free(check);
}

5차
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/*
	C언어는 절차지향 언어이기 때문에 find 함수가 main 함수 이후에 정의되는 것을
	컴파일러에게 알리기 위해 find 함수의 원형 선언
*/
void find(int, int);

void main(){
	int startNum, endNum; // 입력 값 변수 
	printf("범위 입력 해주세요 : ");
	scanf("%d %d", &startNum, &endNum); // 범위 값 입력
	find(startNum, endNum);
}

void find(int startNum, int endNum){
	int cnt=0; // 소수갯수 cnt변수 
	int i,j; // for문 변수  
	int *check = (int*)calloc(endNum, sizeof(int)); // calloc을 이용하여 배열 동적할당 및 0으로 초기화 
	
	for(i=2; i<=endNum; i++) check[i] = 1; // 0, 1이 아닌 모든 수를 소수라 가정  
    
    	for(i=2; i<=sqrt(endNum); i++){ // 제곱근 이후의 수는 탐색할필요 없기 때문에 제곱근 까지 탐색   
		if(!check[i]) continue; // 소수가 아닐경우 continue
		
		// 소수인 i의 배수는 소수가 아니므로 0 입력  
		for(j=2; i*j<=endNum; j++)
			check[i*j] = 0;
   	}

	for(i=startNum; i<=endNum; i++){
		if(check[i]==1) { // 소수일 때
        		cnt++; // 카운트 증가
        		printf("%d ", i); // 출력
    		}
	}
	
	printf("\n소수 갯수 : %d", cnt);
	free(check);
}