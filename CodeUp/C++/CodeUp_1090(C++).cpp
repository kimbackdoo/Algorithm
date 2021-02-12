#include <iostream>
#include <cmath>
using namespace std;

int main(){
	int a, r, n;
	long long s;
	cin >> a >> r >> n;
	s=a*pow(r, n-1);
	cout << s << endl;
	return 0;
}