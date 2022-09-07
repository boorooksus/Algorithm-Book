#include <iostream>
#define MAX 1000000000
using namespace std;

int N;
long long dp[101][10];


int main(){
    cin >> N;

    for (int i = 1; i < 10; i++){
        dp[1][i] = 1;
    }

    for (int i = 2; i <= N; i++) {
        dp[i][0] = dp[i - 1][1];
        for (int j = 1; j < 9; j++){
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % MAX;
        }
        dp[i][9] = dp[i - 1][8];
    }

    long long ans = 0;
    for (int i = 0; i < 10; i++) {
        ans = (ans + dp[N][i]) % MAX;
    }

    cout << ans << "\n";
}
