#include <iostream>
using namespace std;

int main(){
	int t, n;
	cin >> t;
	bool prime[10001]={0,1,0,};
	for(int i=2; i<=10000; i++)
		if(prime[i]==0)
			for(int j=2; i*j<=10000; j++)
				prime[i*j]=1;
	for(int i=0; i<t; i++){
		cin >> n;
		for(int i=n/2; i>0; i--)
			if(prime[i]==0&&prime[n-i]==0){
				cout << i << " " << n-i << endl;
				break;
			}
	}
	return 0;
}