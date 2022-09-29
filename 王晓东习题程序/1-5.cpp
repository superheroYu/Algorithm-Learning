#include <iostream>

double maxgap(int n, double *x);

int main()
{
    double s[] = {1, 2, 4, 8, 10, 1000, 2, 1000, 0};
    int n = sizeof(s) / sizeof(s[0]);
    double MAX = maxgap(n, s);
    std::cout << "最大数字间隙为：" << MAX << std::endl;

    return 0;
}

template <typename T>
int *get_min_max(int n, T *x) // 用于寻找数组中最大值和最小值的索引
{
    int min_idx = 0;
    int max_idx = 0;
    T tmp_min = x[0];
    T tmp_max = x[0];
    for (int i = 1; i < n; i++)
    {
        if (x[i] < tmp_min)
        {
            tmp_min = x[i];
            min_idx = i;
        }
        if (x[i] > tmp_max)
        {
            tmp_max = x[i];
            max_idx = i;
        }
    }
    int *minmaxidx = new int[2]{min_idx, max_idx};
    return minmaxidx;
}

double maxgap(int n, double *x) // 寻找数组中的最大间隙
{
    int *minmaxidx = get_min_max(n, x);
    int mini = minmaxidx[0];
    int maxi = minmaxidx[1];
    double max = x[maxi], min = x[mini]; // 记录数组中的最大值和最小值

    // low用于存放每桶中的最小值，high用于存放每桶中的最大值，count用于存储每桶中数字的数量
    double *low = new double[n + 1];
    double *high = new double[n + 1];
    int *count = new int[n + 1];

    // 给low、high、count赋初值
    for (int i = 0; i < n + 1; i++)
    {
        count[i] = 0;
        low[i] = max;
        high[i] = min;
    }

    // 将数组中的数放入桶中
    for (int i = 0; i <= n; i++)
    {
        double num = x[i];
        int idx = int((n - 1) * (num - min) / (max - min)) + 1;
        if (num < low[i])
            low[idx] = num;
        if (num > high[i])
            high[idx] = num;
        count[idx]++;
    }

    // 遍历寻找最大间隙
    double right, left = high[0]; // right记录后一个桶中的最小数，left记录前一个桶中的最大数
    double gap = 0;
    for (int i = 0; i < n + 1; i++)
    {
        if (count[i]) // 判断桶中是否还有数字
        {
            right = low[i];
            if (gap < right - left)
            {
                gap = right - left;
            }
            left = high[i];
        }
    }
    delete minmaxidx;
    return gap;
}