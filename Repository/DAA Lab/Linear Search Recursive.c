#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MIN 1
#define MAX n

int linearSearch(int arr[], int size, int x) {
    int rec;
    size--;
    if (size >= 0) {
        if (arr[size] == x)
            return size;
        else
            rec = linearSearch(arr, size, x);
    }
    else
        return -1;
    return rec;
}

int main() {
  time_t start;
  start = time(NULL);
  int n;
  printf("\nEnter size: ");
  scanf("%d", &n);
  int *arr = (int *) malloc (n * sizeof(int));
  for(int i=0; i<n; i++) {
    arr[i] = (rand() % (MAX - MIN + 1)) + MIN;
  }
  int val = (rand() % (MAX - MIN + 1)) + MIN;
  int index = linearSearch(arr, n, val);
  printf("\nArray: \n");
  for(int i=0; i<n; i++) {
  	printf("%d ", arr[i]);
  }
  printf("\nElement to search: %d", val);
  if(index == -1) {
    printf("\nElement %d not found in the array.", val);
  }
  else {
    printf("\nElement %d is present at index %d.", val, index);
  }
  time_t stop = time(NULL);
  printf("\nTime taken: %d", stop-start);
}