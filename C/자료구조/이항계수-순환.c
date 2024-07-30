#include <stdio.h>

int C(int n, int k){
	if(k==0 || k==n) return 1;
	if(0<k && k<n)
		return C(n-1, k-1)+C(n-1, k);
}

int main(){
	int n, k;
	scanf("%d %d", &n, &k);
	printf("C : %d \n", C(n,k));
	return 0;
}
