#include <iostream>
using namespace std;

int main(){
	int a;
	cin >> a;
	while(a!=0){
		if(a==0)
			break;
		cout << a << endl;
		a--;
	}
	return 0;
}