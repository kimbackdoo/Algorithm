#include <iostream>
#include <cstdlib>
using namespace std;

int main(){
	int a[2];
	char s[4];
	for(int i=0; i<2; i++){
		cin >> s;
		char rev=s[0];
		s[0]=s[2];
		s[2]=rev;
		a[i]=atoi(s);
	}
	if(a[0]<a[1]) cout << a[1] << endl;
	else cout << a[0] << endl;
	return 0;
}