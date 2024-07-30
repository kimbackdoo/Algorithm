#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

bool compare(string a, string b){
	if(a.size()!=b.size())
		return a.size()<b.size();
	return a<b;
}

int main(){
	string s[20001], tmp;
	int n;
	cin >> n;
	for(int i=0; i<n; i++)
		cin >> s[i];
	sort(s, s+n, compare);
	for(int i=0; i<n; i++){
		if(tmp!=s[i]) cout << s[i] << "\n";
		tmp=s[i];
	}
	return 0;
}