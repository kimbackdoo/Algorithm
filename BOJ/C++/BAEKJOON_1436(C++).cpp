#include <iostream>
using namespace std;

int main(){
	int n, value=66, cnt=0;
	cin >> n;
	while(value++){
		int tmp=value, flag=0;
		while(tmp){
			if(tmp%1000==666) flag=1;
			tmp/=10;
		}
		if(flag){
			cnt++;
			if(cnt==n) break;
		}
	}
	cout << value << endl;
	return 0;
}