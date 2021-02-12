#include <iostream>
using namespace std;

int main(){
	long long n, range=1, tmp=1;
	cin >> n;
	int cnt=1;
	while(1){
		if(range>=n) break;
		tmp=6*(cnt++);
		range+=tmp;
	}
	cout << cnt << endl;
	return 0;
}