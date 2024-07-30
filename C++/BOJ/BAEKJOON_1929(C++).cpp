#include <iostream>
using namespace std;

int main(){
	int m, n;
	scanf("%d %d", &m, &n);
	bool arr[n+1]={0,};
	arr[0]=arr[1]=1;
	for(int i=2; i*i<=n; i++)
		if(arr[i]==0){
			for(int j=i*i; j<=n; j+=i)
				arr[j]=1;
		}
	for(int i=m; i<=n; i++)
		if(!arr[i])
			printf("%d\n", i);
	return 0;
}