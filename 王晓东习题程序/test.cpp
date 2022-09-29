#include <iostream>

template <typename T>
void test(T &a, T &b);

template <typename T>
void test(const T &a, const T &b, const T &c);
template <> void test<int>(const int &a, const int &b, const int &c);

int main()
{
    // test<int>(12, 12);
    float a = 12;
    float b = 12;
    float c = 12;
    //test()
    test(a, b, c);
    test<int>(a, b, c);
}

// template <typename T>
// void test(const T &a, const T &b)
// {
//     std::cout << a << " " << b << std::endl;
// }
template <typename T>
void test(const T &a, const T &b, const T &c)
{
    std::cout << a << " " << b << " 1" << std::endl;
}

template <> void test<int>(const int &a, const int &b, const int &c)
{
    std::cout << a << " " << b << " 2 " << std::endl;
}