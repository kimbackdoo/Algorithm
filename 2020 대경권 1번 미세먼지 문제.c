#include <stdio.h>
#include <stdlib.h>

// atmos_len은 2차원 배열 atmos의 행(세로) 길이입니다.
int solution(int atmos[][2], size_t atmos_len) {
	int i, day = 0, answer = 0;
	int *a = (int *)calloc(atmos_len, sizeof(int));
	for(i=0; i<atmos_len; i++) {
		if(atmos[i][0] > 80 || atmos[i][1] > 35) {
			if(atmos[i][0] > 150 && atmos[i][1] > 75) {
				a[i]++;
				day=0;
			}
			else if(i==atmos_len-1) a[i]++;
			else day++;
			if(day==3) {
				a[i]++;
				day=0;
			}
		}
		else if(day!=0) day++;
		if(day==3) {
			a[i]++;
			day=0;
		}
	}
	for(i=0; i<atmos_len; i++)
		if(a[i]==1) answer++;
	free(a);
	return answer;
}

int main() {
	int i, atmos[10][2];
	for(i=0; i<10; i++)
		scanf("%d %d", &atmos[i][0], &atmos[i][1]);
	//solution(atmos, 2);
	printf("result : %d\n", solution(atmos, 10));
	return 0;
}
