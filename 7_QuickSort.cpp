#include <iostream>
#include <cstdlib>  // For rand()

using namespace std;

int partition(int* arr, int p, int r) {
    int x = arr[r]; // pivot
    int i = p - 1;  // index of smaller element
    for (int j = p; j < r; j++) {
        if (arr[j] <= x) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[r]);
    return i + 1;
}

void quickSort(int* arr, int p, int r) {
    if (p < r) {
        int q = partition(arr, p, r);
        quickSort(arr, p, q - 1);
        quickSort(arr, q + 1, r);
    }
}

// Randomized Partition
int randomPartition(int* arr, int p, int r) {
    int randomIndex = rand() % (r - p + 1) + p;
    swap(arr[randomIndex], arr[r]);  // Move the random pivot to the end
    return partition(arr, p, r);     // Use the normal partition function
}

void randomizedQuickSort(int* arr, int p, int r) {
    if (p < r) {
        int q = randomPartition(arr, p, r);
        randomizedQuickSort(arr, p, q - 1);
        randomizedQuickSort(arr, q + 1, r);
    }
}

int main() {
    cout<<"Name : Amol Subhash Dangat\nRoll No : 09\n"<<endl;
    int A[] = {23, 34, 54, 123, 34, 56, 67676, 112};
    int n = sizeof(A) / sizeof(A[0]);
    randomizedQuickSort(A, 0, n - 1);
    cout<<"Sorted array is: ";
    for (int i = 0; i < n; i++) {
        cout << A[i] << " ";
    }
    cout << '\n';
    return 0;
}
