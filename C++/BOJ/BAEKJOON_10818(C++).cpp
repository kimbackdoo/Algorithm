#include <iostream>
using namespace std;

int main(){
	int n, max=-1000000, min=1000000, t;
	scanf("%d", &n);
	for(int i=0; i<n; i++){
		scanf("%d", &t);
		if(min>t) min=t;
		if(max<t) max=t;
	}		
	printf("%d %d\n", min, max);
	return 0;
}