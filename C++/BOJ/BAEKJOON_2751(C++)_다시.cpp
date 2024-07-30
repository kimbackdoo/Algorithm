#include <iostream>
using namespace std;

int arr[1000000], tmp[1000000];

void Merge(int left, int mid, int right){
	int i=left, j=mid+1, k=left;
	while(i<=mid && j<=right){
		if(arr[i]<arr[j]) tmp[k++]=arr[i++];
		else tmp[k++]=arr[j++];
	}
	if(i>mid)
		for(int idx=j; idx<=right; idx++)
			tmp[k++]=arr[idx];
	else
		for(int idx=i; idx<=mid; idx++)
			tmp[k++]=arr[idx];
	for(int idx=left; idx<=right; idx++)
		arr[idx]=tmp[idx];
}

void mergeSort(int left, int right){
	if(left<right){
		int mid=(left+right)/2;
		mergeSort(left, mid);
		mergeSort(mid+1, right);
		Merge(left, mid, right);
	}
}

int main(){
	int n;
	cin >> n;
	for(int i=0; i<n; i++)
		cin >> arr[i];
	mergeSort(0, n-1);
	for(int i=0; i<n; i++)
		cout << arr[i] << "\n";
	return 0;
}