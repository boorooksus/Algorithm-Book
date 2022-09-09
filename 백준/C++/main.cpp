#include <iostream>
#include <cstring>
#include <queue>
#include <cmath>
using namespace std;


int N;
int after[1000];
int first[1000];

void shuffle(int[], int);
bool check(const int[], const int[]);


int main(){
    std::ios::sync_with_stdio(false);

    cin >> N;
    for (int i = 0; i < N; i++){
        cin >> after[i];
    }

    for (int i = 1;  pow(2, i) < N; i++){
        for (int j = 0; j < N; j++){
            first[j] = j + 1;
        }
        shuffle(first, i);
        for (int j = 1; pow(2, j) < N; j++){
            int second[1000];
            memcpy(second, first, sizeof(second));
            shuffle(second, j);
            if(check(after, second)){
                cout << i << " " << j << "\n";
                return 0;
            }
        }
    }
}

void shuffle(int cards[], int k){
    queue<int> res;
    // first step
    int cnt =  (int)pow(2, k);
    for (int i = N - cnt; i < N; i++){
        res.push(cards[i]);
    }
    for (int i = 0; i < N - cnt; i++){
        res.push(cards[i]);
    }

    // second ~ K + 1 steps
    for (int i = 2; i <= k + 1; i++){
        queue<int> temp;
        for(int j = 0; j < cnt; j++){
            temp.push(res.front());
            res.pop();
        }
        cnt = (int)pow(2, k - i + 1);
        int len = (int)temp.size();
        for (int j = 0; j < len - cnt; j++){
            temp.push(temp.front());
            temp.pop();
        }
        while(!res.empty()){
            temp.push(res.front());
            res.pop();
        }
        while (!temp.empty()){
            res.push(temp.front());
            temp.pop();
        }
    }

    for(int i = 0; i < N; i++){
        cards[i] = res.front();
        res.pop();
    }
}

bool check(const int x[], const int y[]){
    for (int i = 0; i < N; i++){
        if (x[i] != y[i]){
            return false;
        }
    }
    return true;
}