#include <iostream>
using namespace std;

int main(){
	int day=1, a, b, c;
	cin >> a >> b >> c;
	while(day%a!=0||day%b!=0||day%c!=0) day++;
	cout << day << endl;
	return 0;
}