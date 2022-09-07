#include <iostream>
#include <set>
#include <string>
using namespace std;


set<string> stairs;
int N;

void dfs(string);


int main(){
    cin >> N;
    for (int i = 1; i < 10; i++){
        dfs(to_string(i));
    }

    cout << stairs.size() << "\n";
}

void dfs(string suffix) {

    if (suffix.length() == N){
        stairs.insert(suffix);
        return;
    }

    if (suffix.length() > N){
        cout << suffix << "\n";
        return;
    }

    int last = int(unsigned(suffix.back())) - 48;
    if (last > 0){
        dfs(suffix + to_string(last - 1));
    }
    if (last < 9){
        dfs(suffix + to_string(last + 1));
    }
}