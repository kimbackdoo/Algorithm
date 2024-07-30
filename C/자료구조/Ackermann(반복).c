#include <stdio.h>

#define MAX_LAN 100000
int Ackermann(int m, int n) {
	int arr[MAX_LAN];
	int top=0;
	
	arr[top++] = m;
	arr[top] = n;
	
	while(1) {
		if(top == 0) return arr[top];
		else if(arr[top-1] == 0) {
			arr[top-1] = arr[top] + 1;
			top -= 1;
		}
		else if(arr[top] == 0) {
			arr[top-1] = arr[top-1] - 1;
			arr[top] = 1;
		}
		else {
			arr[top+1] = arr[top] - 1;
			arr[top] = arr[top-1];
			arr[top-1] = arr[top-1] - 1;
			top += 1;
		}
	}
}

int main() {
	int result = Ackermann(3, 2);
	printf("%d \n", result);
	return 0;
}
