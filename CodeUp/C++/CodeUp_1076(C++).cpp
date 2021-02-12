#include <iostream>
using namespace std;

int main(){
	char a, b='a';
	cin >> a;
	do {
		printf("%c ", b);
		b+=1;
	} while(b < a+1);
	cout << endl;
	return 0;
}