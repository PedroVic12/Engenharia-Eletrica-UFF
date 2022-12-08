template <class T>

class myPair
{
    T values[2];

public:
    myPair(T first, T second)
    {
        values[0] = first;
        values[1] = second;
    }

    T max()
    {
        if (values[0] > values[1])
        {
            return (values[0]);
        }
        else
            return (values[1]);
    }
};

int main()
{
    cout << myPair<int>(3, 7) << endl;
    cout << myPair<float>(1.0, 2.0) << endl;

    return 0;
}