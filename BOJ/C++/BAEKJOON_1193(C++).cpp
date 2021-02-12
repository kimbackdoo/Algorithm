#include <iostream>
using namespace std;

int main(){
	int n, len=0, b=1;
	cin >> n;
	while(1){
		if(n-b<=0) break;
		n-=b;
		len++, b++;
	}
	if(len%2==0) cout<<len+2-n<<"/"<<n<<endl;
	else cout<<n<<"/"<<len+2-n<<endl;
	return 0;
}