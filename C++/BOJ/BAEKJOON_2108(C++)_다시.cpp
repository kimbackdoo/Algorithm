#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int n, r, cnt=0, a[4001]={}, b[4001]={};
	double sum=0;
	vector<int> vec;
	scanf("%d", &n);
	int arr[n];
	for(int i=0; i<n; i++){
		scanf("%d", &arr[i]);
		sum+=arr[i];
	}
	sort(arr, arr+n);
	sum/=n; sum=floor(sum+0.5);
	cout<<sum<<"\n"<<arr[n/2]<<"\n";
	for(int i=0; i<n; i++){
		if(arr[i]>=0) a[arr[i]]++;
		else b[abs(arr[i])]++;
	}
	for(int i=0; i<4001; i++){
		if(cnt<a[i]){
			cnt=a[i];
			r=i;
			vec.clear();
			vec.push_back(r);
		}
		if(cnt==a[i]) vec.push_back(i);
		if(cnt<b[i]){
			cnt=b[i];
			r=-i;
			vec.clear();
			vec.push_back(r);
		}
		if(cnt==b[i]) vec.push_back(-i);
	}
	sort(vec.begin(), vec.end());
	if(vec.size()==1) cout<<vec[0]<<"\n";
	else cout<<vec[1]<<"\n";
	cout<<arr[n-1]-arr[0]<<"\n";
	return 0;
}