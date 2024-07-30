#include <iostream>
using namespace std;

int main(){
	int sum=0, alpha[26]={3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10,10};
	char s[16];
	cin >> s;
	for(int i=0; s[i]; i++){
		int idx=s[i]-65;
		sum+=alpha[idx];
	}
	cout << sum << endl;
	return 0;
}