#include <iostream>
#include <cstring>
using namespace std;

int main(){
	int max=0, alpha[26]={};
	char c, s[1000001];
	cin >> s;
	for(int i=0; s[i]; i++){
		if('a'<=s[i]&&s[i]<='z') s[i]-=32;
		alpha[s[i]-65]++;
	}
	for(int i=0; i<26; i++){
		if(max<alpha[i]){
			max=alpha[i];
			c=i;
		}
		else if(alpha[i]==max) c='?';
	}
	printf("%c\n", (c=='?')?'?':c+65);		
	return 0;
}