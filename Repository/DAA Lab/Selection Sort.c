#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MIN 1
#define MAX n

void swap(int *xp, int *yp)
{
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}
 
void selectionSort(int arr[], int n){
    int i, j, min_idx;
    for (i = 0; i < n-1; i++){
        min_idx = i;
        for (j = i+1; j < n; j++)
          if (arr[j] < arr[min_idx])
            min_idx = j;
            if(min_idx != i)
            swap(&arr[min_idx], &arr[i]);
    }
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
  selectionSort(arr, n);
  printf("\nSorted Array: \n");
  for(int i=0; i<n; i++) {
  	printf("%d ", arr[i]);
  }
  time_t stop = time(NULL);
  printf("\nTime taken: %0.2f", difftime(stop,start));
}

