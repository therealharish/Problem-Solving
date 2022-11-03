#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MIN 1
#define MAX n

int getMax(int arr[], int n) {
  int max = arr[0];
  for (int i = 1; i < n; i++)
    if (arr[i] > max)
      max = arr[i];
  return max;
}

void countingSort(int arr[], int size, int place) {
  int out[size + 1];
  int max = (arr[0] / place) % 10;
  for (int i = 1; i < size; i++) {
    if (((arr[i] / place) % 10) > max)
      max = arr[i];
  }
  int count[max + 1];
  for (int i = 0; i < max; ++i)
    count[i] = 0;
  
  for (int i = 0; i < size; i++)
    count[(arr[i] / place) % 10]++;
  
  for (int i = 1; i < 10; i++)
    count[i] += count[i - 1];
  
  for (int i = size - 1; i >= 0; i--) {
    out[count[(arr[i] / place) % 10] - 1] = arr[i];
    count[(arr[i] / place) % 10]--;
  }

  for (int i = 0; i < size; i++)
    arr[i] = out[i];
}

void radixSort(int arr[], int size) {
  int max = getMax(arr, size);
  for (int place = 1; max / place > 0; place *= 10)
    countingSort(arr, size, place);
}
 

int main() {
  srand(time(0));
  time_t start = time(NULL);
  
  int n;
  printf("\nEnter size: ");
  scanf("%d", &n);
  int *arr = (int*) malloc (n * sizeof(int));
  for(int i=0; i<n; i++) {
    arr[i] = (rand() % (MAX - MIN + 1)) + MIN;
  }
  printf("\narr: \n");
  for(int i=0; i<n; i++) {
  	printf("%d ", arr[i]);
  }
  radixSort(arr,n);
  printf("\nSorted arr: \n");
  for(int i=0; i<n; i++) {
  	printf("%d ", arr[i]);
  }
  time_t stop = time(NULL);
  printf("\nTime taken: %0.2f", difftime(stop,start));
}

