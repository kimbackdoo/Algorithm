#include <stdio.h>
#include <string.h>

int C(int n, int k){
	int i, j;
	int c[n+1][k+1];
	for(i=0; i<=n; i++)
		memset(c, 0, sizeof(c));
	for(i=0; i<=n; i++){
		c[i][0]=c[i][i]=1;
		for(j=1; j<i && j<=k; j++)
			c[i][j]=c[i-1][j-1]+c[i-1][j];
	}
	return c[n][k];
}

int main(){
	int n, k;
	scanf("%d %d", &n, &k);
	printf("C : %d \n", C(n,k));
	return 0;
}
