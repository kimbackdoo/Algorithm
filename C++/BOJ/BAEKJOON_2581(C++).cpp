#include <iostream>
using namespace std;

int main(){
	int m, n, j, sum=0, min=10001;
	cin >> m >> n;
	for(; m<=n; m++){
		for(j=2; j<m; j++)
			if(m%j==0) break;
		if(m==j) {
			if(min>m) min=m;
			sum+=m;
		}
	}
	if(sum==0) cout << -1 << endl;
	else cout << sum << endl << min << endl;
	return 0;
}