#include <iostream>
#include <vector>
using namespace std;

int main(){
	vector<string> calpha={
		"c=","c-","dz=","d-","lj","nj","s=","z="
	};
	string s;
	cin >> s;
	for(int i=0; i<calpha.size(); i++){
	    int idx=s.find(calpha[i]);
	    for(; idx!=string::npos; idx=s.find(calpha[i]))
		    s.replace(idx, calpha[i].length(), "@");
	}
	cout << s.length() << endl;
	return 0;
}