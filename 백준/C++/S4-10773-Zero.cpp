#include <iostream>
#include <stack>
using namespace std;

int main(){
    int K;
    cin >> K;
    
    stack<int> s;
    for (int i = 0; i < K; i++ ){
        int temp;
        cin >> temp;
        if (temp > 0) {
            s.push(temp);
        } else {
            s.pop();
        }
    }

    int ans = 0;
    while (!s.empty()){
        ans += s.top();
        s.pop();
    }
    cout << ans << "\n";
}