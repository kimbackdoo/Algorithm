#include <iostream>
using namespace std;

int main(){
	int i, a;
	cin >> i;
	reget:
		cin >> a;
		cout << a << endl;
		if(--i != 0)
			goto reget;
	return 0;
}