#include <stdio.h>

int GCD(int a, int b){
	if(a<b){
		if(a==0) return b;
		return GCD(a, b%a);
	}
	else{
		if(b==0) return a;
		return GCD(b, a%b);
	}
}

int LCM(int a, int b){
	return a*b/GCD(a,b);
}

int main(){
	int a, b;
	printf("두 수 입력 : ");
	scanf("%d %d", &a, &b);
	printf("최대공약수 : %d\n최소공배수 : %d\n", GCD(a,b), LCM(a,b)); 
	return 0;
}
