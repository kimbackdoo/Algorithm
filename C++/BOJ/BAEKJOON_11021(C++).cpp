#include <iostream>
using namespace std;

int main(){
	int n, a, b, arr[100];
	scanf("%d", &n);
	for(int i=1; i<=n; i++){
		scanf("%d %d", &a, &b);
		arr[i] = a+b;
	}
	for(int i=1; i<=n; i++)
		printf("Case #%d: %d \n", i, arr[i]);
	return 0;
}