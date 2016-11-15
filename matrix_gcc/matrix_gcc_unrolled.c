#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define N 10
#define M 10


void init_matrix(int (*a)[N])
{
int i,j;
  for (i=0;i<N;i++)
    for (j=0;j<N;j++)
      a[i][j] = 5;
}

void init_vector(int (*b))
{
int i;
  for (i=0;i<M;i++)
  	b[i] = 3;
}

void matrix_vector_multiply(int (*a)[N], int (*b), int (*c))
{
   int i,j;
   for (i=0;i<N;i++)
   	c[i]=0;
   	for (j=0;j<M;j+=5)
      c[i] += a[i][j] * b[j];
      c[i] += a[i][j+1] * b[j+1];
      c[i] += a[i][j+2] * b[j+2];
      c[i] += a[i][j+3] * b[j+3];
      c[i] += a[i][j+4] * b[j+4];
}

int main()
{
    int i,j;
    int res = 0;
    int (*a)[N] = (int (*)[N]) calloc(N*N, sizeof(int));
    int (*b) = (int (*)) calloc(M, sizeof(int));
    int (*c) = (int (*)) calloc(N, sizeof(int));
    
    init_matrix(a) ; init_vector(b);
    
    for(j=0;j<10000000;j++)
      matrix_vector_multiply(a,b,c);
    
    for(i=0;i<N;i++)
        res+=c[i] % 2;
    return res;
}
