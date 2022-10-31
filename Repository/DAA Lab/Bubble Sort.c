#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MIN 1
#define MAX n

void swap(int* xp, int* yp)
{
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}
 
void bubbleSort(int arr[], int n)
{
    int i, j;
    for (i = 0; i < n - 1; i++)
 
        // Last i elements are already in place
        for (j = 0; j < n - i - 1; j++)
            if (arr[j] > arr[j + 1])
                swap(&arr[j], &arr[j + 1]);
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
  printf("\nArray: \n");
  for(int i=0; i<n; i++) {
  	printf("%d ", arr[i]);
  }
  bubbleSort(arr, n);
  printf("\nSorted Array: \n");
  for(int i=0; i<n; i++) {
  	printf("%d ", arr[i]);
  }
  time_t stop = time(NULL);
  printf("\nTime taken: %0.2f", difftime(stop,start));
}

