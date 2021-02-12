#include <iostream>
using namespace std;

int main(){
	int a, sum=0;
	cin >> a;
	for(int i=1; ; i++){
		sum+=i;
		if(sum>=a){
			cout << i << endl;
			break;	
		}
	}
	return 0;
}