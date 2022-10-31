#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MIN 1
#define MAX n

void insertionSort(int arr[], int n)
{
    int i, key, j;
    for (i = 1; i < n; i++)
    {
        key = arr[i];
        j = i - 1;
 
        while (j >= 0 && arr[j] > key)
        {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}

int binarySearch(int arr[], int l, int r, int x) {
  if (r >= l) {
    int mid = l + (r - l)/2;
    if (arr[mid] == x) 
      return mid;
    if (arr[mid] > x) 
      return binarySearch(arr, l, mid-1, x);
    return 
      binarySearch(arr, mid+1, r, x);
    }
    return -1;
}



int main() {
  time_t start = time(NULL);
  
  int n;
  printf("\nEnter size: ");
  scanf("%d", &n);
  int *arr = (int *) malloc (n * sizeof(int));
  for(int i=0; i<n; i++) {
    arr[i] = (rand() % (MAX - MIN + 1)) + MIN;
  }
  insertionSort(arr, n);
  int val = (rand() % (MAX - MIN + 1)) + MIN;
  printf("\nArray: \n");
  for(int i=0; i<n; i++) {
  	printf("%d ", arr[i]);
  }
  printf("\nElement to search: %d", val);
  int index = binarySearch(arr, 0, n, val);
  if(index == -1) {
    printf("\nElement %d not found in the array.", val);
  }
  else {
    printf("\nElement %d is present at index %d.", val, index);
  }
  time_t stop = time(NULL);
  printf("\nTime taken: %0.2f", difftime(stop,start));
}