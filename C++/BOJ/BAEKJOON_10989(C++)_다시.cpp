#include <iostream>
using namespace std;

int main(){
	int n, arr[10001]={};
	scanf("%d", &n);
	for(int i=0; i<n; i++){
		int tmp;
		scanf("%d", &tmp);
		arr[tmp]++;
	}
	for(int i=1; i<=10000; i++)
		for(int j=0; j<arr[i]; j++)
			cout << i << "\n";
	return 0;
}