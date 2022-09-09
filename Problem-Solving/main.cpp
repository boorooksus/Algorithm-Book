#include <iostream>
using namespace std;

int m, n;
string dna[50];

int main(){
    std::ios::sync_with_stdio(false);
    int T;
    cin >> T;
    while (T--){
        cin >> m >> n;
        for (int i = 0; i< m; i++ ){
            cin >> dna[i];
        }

        int hamming = 0;
        string repre = "";
        for (int i = 0; i < n; i++){
            int base[26];
            char repre_base = 0;
            int max_cnt = 0;
            fill_n(base, 26, 0);
            for (int j = 0; j < m; j++){
                base[dna[j][i] - 65]++;

            }
        }
    }
}