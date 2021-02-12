#include <iostream>
using namespace std;

int main(){
	int n=1;
	while(cin>>n){
		if(n==0) break;
		bool prime[n*2+1]={0,};
		for(int i=2; i*i<=n*2; i++){
		if(prime[i]==0)
			for(int j=i*i; j<=n*2; j+=i)
				prime[j]=1;
		}
		int cnt=0;
		for(int i=n+1; i<=n*2; i++)
			if(prime[i]==0) cnt++;
		cout << cnt << endl;
	}
	return 0;
}