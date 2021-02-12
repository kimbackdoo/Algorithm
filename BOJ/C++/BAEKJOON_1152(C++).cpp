#include <iostream>
#include <cstring>
using namespace std;

int main(){
	int cnt=0;
	string s;
	getline(cin, s);
	for(int i=0; s[i]; i++)
		if(s[i]==' '&&s[i+1]!='\0') cnt++;
	if(s[0]=='\0'||s[0]==' ') cnt--;
	cout << cnt+1 << endl;
	return 0;
}