#include <iostream>
#include <cstring>
#include <fstream>

using namespace std;

int C(int, int);
int N(char [], int);

int main() 
{
    ifstream input("data\\input1_2.txt");
    ofstream outfile("data/output1_2.txt");
    if (!input) cout << "文件打开错误!" << endl;
    else
    {
        int k=10;
        // input >> k;
        for (int m=0; m<=k; m++)
        {
            char s[7];
            input.getline(s, 7);
            if (!s[0]) continue;
            int n = strlen(s);
            int sum = 0;
            for(int j=1;j<n;j++)
            {
                sum += C(26, j);
            }
            int result = sum + N(s, 0) + 1;
            cout << result << endl;
            outfile << result << endl;
        }
    }
    
    input.close();
    outfile.close();
    return 0;
}

int C(int n, int m)
{
    int a = 1;
    int b = 1;
    for(int j=1;j<=m;j++)
    {
        a *= n-j+1;
        b *= j;
    }
    return a/b;
}

int N(char *s, int i)
{
    int n = strlen(s);
    if(n<1) return 0;
    char high = s[0];
    int sum = 0;
    for(int k=1;k<=high-'a'-i;k++)
    {
        sum += C(26-i-k, n-1);
    }
    if(n>1) sum += N(&s[1], high-'a'+1);
    return sum;
}