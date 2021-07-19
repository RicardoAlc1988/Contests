#include <iostream>
#include <sys/time.h>
#include <stdlib.h>
#include <stdio.h>
using namespace std;

void burbuja(int *d,int n)
{
  int i,j,t;

  for(i=0;i<n;i++)
  {
    for(j=i+1;j<n;j++)
    {
      if(d[i]>d[j])
      {
        t=d[i];
        d[i]=d[j];
        d[j]=t;
      }
    }
  }
}

void Muestra_array(int* a, int n){
	for(int i=0;i<n;i++) cout<<a[i]<<" ";
	cout<<"\n";
}	

int altura_maxima(int* a, int n)
{	
	int i,j;
	// Prepocesamiento de los datos
	burbuja(a,n);
	i=0;
	j = n-1;

	
}
int main()
{
// Testeo el algoritmo de la burbuja
int a[] = {7,-2,6,9,-3};
altura_maxima(a,5);

return 0;
}
