#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Declaration
void print(vector<int> elements);
void printWithIndex(vector<int> elements);

int main()
{
    vector<int> numbers = {1, 2, 3};
    numbers.push_back(4);
    numbers.push_back(5);

    printWithIndex(numbers);

    numbers.erase(numbers.begin() + 1);

    printWithIndex(numbers);

    numbers.insert(numbers.end(), 4); 

    printWithIndex(numbers);
    
    
}

void print(vector<int> elements)
{
    for(int element: elements)
        cout << element << " ";
}

void printWithIndex(vector<int> elements)
{
    for(int index=0; index < elements.size() ; index++)
        cout << elements[index] << " ";
    
    cout << endl;
}