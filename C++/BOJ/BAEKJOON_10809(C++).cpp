#include <iostream>
#include <cstring>
using namespace std;

int main(){
	int arr[123];
	char s[100];
	cin >> s;
	for(int i=97; i<123; i++)
		arr[i]=-1;
	for(int i=0; i<strlen(s); i++){
		if(arr[s[i]]==-1)
			arr[s[i]]=i;
	}	
	for(int i=97; i<123; i++)
		cout << arr[i] << " ";
	cout << endl;
	return 0;
}