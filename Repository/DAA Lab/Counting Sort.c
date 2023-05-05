#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MIN 1
#define MAX n


void countingSort(int arr[], int size) {
  int out[100000];
  int max = arr[0];
  for (int i = 1; i < size; i++) {
    if (arr[i] > max)
      max = arr[i];
  }
  int count[100000];
  for (int i = 0; i <= max; ++i) {
    count[i] = 0;
  }
  for (int i = 0; i < size; i++) {
    count[arr[i]]++;
  }
  for (int i = 1; i <= max; i++) {
    count[i] += count[i - 1];
  }
  for (int i = size - 1; i >= 0; i--) {
    out[count[arr[i]] - 1] = arr[i];
    count[arr[i]]--;
  }
  for (int i = 0; i < size; i++) {
    arr[i] = out[i];
  }
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
  printf("\nArray: \n");
  for(int i=0; i<n; i++) {
  	printf("%d ", arr[i]);
  }
  countingSort(arr,n);
  printf("\nSorted Array: \n");
  for(int i=0; i<n; i++) {
  	printf("%d ", arr[i]);
  }
  time_t stop = time(NULL);
  printf("\nTime taken: %0.2f", difftime(stop,start));
}

