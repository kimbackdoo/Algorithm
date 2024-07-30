#include <stdio.h>

int Ackermann(int m, int n) {
	if(m == 0) return n+1;
	else if(n == 0) return Ackermann(m-1, 1);
	else return Ackermann(m-1, Ackermann(m, n-1));
}

int main() {
	int result = Ackermann(3, 2);
	printf("%d \n", result);
	return 0;
}
