#include <stdio.h>
#include <stdlib.h>

typedef struct _Element { // 희소행렬의 행, 열, 0이 아닌 값에 대한 구조체 
	int row, col, value;
} Element;

int r, c, v, i; // r: 행의 개수, c: 열의 개수, v: 0이 아닌 요소의 개수 
Element *a, *b; // a: 희소행렬의 정보를 담고 있는 구조체 Element형 배열
				// b: 배열 a의 각 요소를 전치시켜 전치행렬의 정보를 담고 있는 구조체 Element형 배열 

// 행, 열, 0이 아닌 요소의 개수를 입력 받기 위한 함수 
void ShowRowCol(){ 
	printf("행의 개수?"); scanf("%d", &r);
	printf("열의 개수?"); scanf("%d", &c);
	printf("0이 아닌 요소의 수?"); scanf("%d", &v);
}

// 0이 아닌 요소의 개수만큼 Element형 배열 a, b를 동적으로 메모리를 할당받고 0이 아닌 요소의 개수만큼
// 행, 열, 값을 입력받아 희소행렬의 정보를 담고 있는 Element형 배열 a를 초기화시키기 위한 함수 
void Init(){
	a=malloc(sizeof(Element)*v);
	b=malloc(sizeof(Element)*v);
	for(i=0; i<v; i++)
		scanf("%d %d %d", &a[i].row, &a[i].col, &a[i].value);
}

// 배열 a의 각 요소를 전치시켜서 배열 b에 저장하기 위한 함수 
void Transpose() {
	int j, pos;
	if(v>0){ // 0이 아닌 원소들(행, 열, 값)에 대해서만 전치를 진행한다 
		pos = 0; // 배열 b에 낮은 행부터 저장하기 위해 변수 pos를 0으로 초기화 
		for(i=0; i<c; i++) // 배열 a를 열별로 전치시킨다
			for(j=0; j<v; j++)  // 0이 아닌 원소 수에 대해서만 전치시킨다 
				if(a[j].col==i){ // 현재의 열에 속하는 원소가 있으면 배열 b에 삽입한다 
					b[pos].row=a[j].col; // 배열 b의 구조체 멤버 row에 배열 a의 구조체 멤버 col을 저장 
					b[pos].col=a[j].row; // 배열 b의 구조체 멤버 col에 배열 a의 구조체 멤버 row을 저장 
					b[pos].value=a[j].value; // 배열 b의 구조체 멤버 value에 배열 a의 구조체 멤버 value을 저장 
					pos++;
				}
	}
}

int main(){
	ShowRowCol(); // 행, 열, 0이 아닌 요수의 개수를 입력받는다 
	Init(); // a, b를 동적으로 할당받고 0이 아닌 요소의 개수만큼 행, 열, 값을 a에 저장시킨다
	Transpose(); // a를 전치시켜 b에 저장한다
	printf("\n");
	for(i=0; i<v; i++) // 전치시킨 배열 b를 출력한다
		printf("%d %d %d \n", b[i].row, b[i].col, b[i].value);
	free(b); // b를 동적으로 할당받았기 때문에 free(b);를 통해 b의 메모리를 해제한다
	free(a); // a를 동적으로 할당받았기 때문에 free(a);를 통해 a의 메모리를 해제한다
	return 0;
}