#include <stdio.h>
#include <stdlib.h>

typedef struct _Element {
	int row, col, value;
} Element;

int r, c, v, i;
Element *a, *b;

void ShowRowCol(){
	printf("행의 개수?"); scanf("%d", &r);
	printf("열의 개수?"); scanf("%d", &c);
	printf("0이 아닌 요소의 수?"); scanf("%d", &v);
}

void Init(){
	a=malloc(sizeof(Element)*v);
	b=malloc(sizeof(Element)*v);
	for(i=0; i<v; i++)
		scanf("%d %d %d", &a[i].row, &a[i].col, &a[i].value);
	
}

void Transpose(){
	int j;
	int row_element[c], start_pos[c];
	if(v!=0){
		for(i=0; i<c; i++)
			row_element[i]=0;
		for(i=0; i<v; i++)
			row_element[a[i].col]++;
		start_pos[0]=1;
		for(i=0; i<v; i++)
			start_pos[i] = start_pos[i-1]+row_element[i-1];
		for(i=0; i<v; i++){
			j = start_pos[a[i].col]++;
			b[j].row = a[i].col;
			b[j].col = a[i].row;
			b[j].value = a[i].value;
		}
	}
}

int main(){
	ShowRowCol();
	Init();
	Transpose();
	printf("\n");
	for(i=0; i<v; i++)
		printf("%d %d %d \n", b[i].row, b[i].col, b[i].value);
	free(b);
	free(a);
	return 0;
}