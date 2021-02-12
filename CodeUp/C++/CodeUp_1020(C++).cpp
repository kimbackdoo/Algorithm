#include<iostream>
#include<cstring>
using namespace std;

int main(){
	char a[30];
	cin >> a;
	for(int i=0; i<strlen(a); i++)
		if(a[i]!='-')
			cout << a[i];
	cout << endl;
	return 0;
}