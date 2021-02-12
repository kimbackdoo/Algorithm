#include <iostream>
using namespace std;

int main(){
	int g;
	cin >> g;
	switch(g/10){
		case 10:
		case 9:
			cout << "A" << endl;
			break;
		case 8:
		case 7:
			cout << "B" << endl;
			break;
		case 6:
		case 5:
		case 4:
			cout << "C" << endl;
			break;
		default:
			cout << "D" << endl;
	}
	return 0;
}