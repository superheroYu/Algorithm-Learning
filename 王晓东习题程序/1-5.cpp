#include <iostream>

double maxgap(int n, double *x);

int main()
{
    double s[] = {1, 2, 4, 8, 10, 1000, 2, 1000, 0};
    int n = sizeof(s) / sizeof(s[0]);
    double MAX = maxgap(n, s);
    std::cout << "������ּ�϶Ϊ��" << MAX << std::endl;

    return 0;
}

template <typename T>
int *get_min_max(int n, T *x) // ����Ѱ�����������ֵ����Сֵ������
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

double maxgap(int n, double *x) // Ѱ�������е�����϶
{
    int *minmaxidx = get_min_max(n, x);
    int mini = minmaxidx[0];
    int maxi = minmaxidx[1];
    double max = x[maxi], min = x[mini]; // ��¼�����е����ֵ����Сֵ

    // low���ڴ��ÿͰ�е���Сֵ��high���ڴ��ÿͰ�е����ֵ��count���ڴ洢ÿͰ�����ֵ�����
    double *low = new double[n + 1];
    double *high = new double[n + 1];
    int *count = new int[n + 1];

    // ��low��high��count����ֵ
    for (int i = 0; i < n + 1; i++)
    {
        count[i] = 0;
        low[i] = max;
        high[i] = min;
    }

    // �������е�������Ͱ��
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

    // ����Ѱ������϶
    double right, left = high[0]; // right��¼��һ��Ͱ�е���С����left��¼ǰһ��Ͱ�е������
    double gap = 0;
    for (int i = 0; i < n + 1; i++)
    {
        if (count[i]) // �ж�Ͱ���Ƿ�������
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