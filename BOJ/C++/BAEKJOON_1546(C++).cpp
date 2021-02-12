#include <iostream>
using namespace std;

int main(){
	int n;
	double m=0, result=0, a[1000];
	cin >> n;
	for(int i=0; i<n; i++){
		scanf("%lf", &a[i]);
		if(m<a[i])
			m=a[i];
		result += a[i];
	}
	printf("%.2lf\n", result/m*100/n);
	return 0;
}