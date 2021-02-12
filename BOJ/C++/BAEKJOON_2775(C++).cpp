#include <iostream>
using namespace std;

int count(int k, int n){
	int cnt=0;
	if(k==0){
		cnt=n;
		return cnt;
	}
	else if(k>0){
		k--;
		for(int i=1; i<=n; i++)
			cnt+=count(k,i);
		return  cnt;
	}
}

int main(){
	int t, k, n;
	cin >> t;
	for(int i=0; i<t; i++){
		cin >> k >> n;
		cout << count(k, n) << endl;
	}
	return 0;
}