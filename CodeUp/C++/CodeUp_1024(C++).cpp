#include<iostream>
#include<cstring>
using namespace std;

int main(){
	char a[20];
	cin >> a;
	for(int i=0; i<strlen(a); i++)
		cout << "'" << a[i] << "'" << endl;
	return 0;
}