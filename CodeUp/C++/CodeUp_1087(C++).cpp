#include <iostream>
using namespace std;

int main(){
	int n, sum=0;
	cin >> n;
	for(int i=1;; i++){
		if(sum>=n)
			break;
		sum += i;
	}
	cout << sum << endl;
	return 0;
}