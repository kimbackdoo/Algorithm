#include <iostream>
using namespace std;

int main(){
	int n, sum=0;
	char ch[100];
	cin >> n;
	cin >> ch;
	for(int i=0; i<n; i++)
		sum+=ch[i]-'0';
	cout << sum << endl;
	return 0;
}