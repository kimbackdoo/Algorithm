#include <iostream>
using namespace std;

int main(){
	int t, r;
	char s[21];
	cin >> t;
	for(int k=0; k<t; k++){
		cin >> r >> s;
		for(int i=0; s[i]!='\0'; i++)
			for(int j=0; j<r; j++)
				printf("%c", s[i]);
		cout << endl;
	}
	return 0;
}