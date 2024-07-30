#include <iostream>
using namespace std;

int Fac(int n){
	if(n<=1) return 1;
	else return n*Fac(n-1);
}

int main(){
	int n;
	scanf("%d", &n);
	printf("%d\n", Fac(n));
	return 0;
}