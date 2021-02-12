#include <iostream>
using namespace std;

int main(){
	long long a, m, d, n;
	cin >> a >> m >> d >> n;
	for(int i=1; i<n; i++){
		a = a*m+d;
	}
	printf("%lli\n", a);
	return 0;
}