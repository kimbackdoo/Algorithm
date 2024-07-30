#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

bool compare(pair<int, int>x, pair<int, int>y){
	if(x.second < y.second) return  true;
	else if(x.second==y.second)
		if(x.first < y.first) return true;
	return false;
}

int main(){
	int n;
	cin >> n;
	vector<pair<int, int>>v(n);
	for(int i=0; i<n; i++)
		cin >> v[i].first >> v[i].second;
	sort(v.begin(), v.end(), compare);
	for(int i=0; i<n; i++)
		cout<<v[i].first<<" "<<v[i].second<<"\n";
		return 0;
}