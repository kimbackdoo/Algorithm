#include <iostream>
using namespace std;

int main(){
	int a;
	for(int i=0; i<3; i++){
		cin >> a;
		if(a%2==0)
			cout << "even" << endl;
		else
			cout << "odd" << endl;
	}
	return 0;
}