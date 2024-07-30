#include <iostream>
using namespace std;

int main(){
	int n,a=1;
	cin >> n;
	while(1){
		int i=a, result=a;
		while(i){
			result+=i%10;
			i/=10;
		}
		if(a==n){
			cout << 0 << endl;
			break;
		}
		else if(result==n){
			cout << a << endl;
			break;
		}
		a++;
	}
	return 0;
}