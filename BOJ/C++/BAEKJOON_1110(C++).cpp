#include <iostream>
using namespace std;

int main(){
	int n, t, count=0;
	int a, b, c;
	scanf("%d", &n);
	if(n<10)
		n*=10;
	t = n;
	while(1){
		a = t/10;
		b = t%10;
		c = a+b;
		t = b*10 + c%10;
		count++;
		if(n==t){
			printf("%d \n", count);
			break;
		}
	}
	return 0;
}