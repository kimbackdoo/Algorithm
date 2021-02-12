#include <iostream>
using namespace std;

int main(){
	int a=1;
	while(a!=0){
		cin >> a;
		if(a==0)
			break;
		cout << a << endl;
	}
	return 0;
}