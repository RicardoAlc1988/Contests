#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <gmp.h>
#include <gmpxx.h>
using namespace std;

const int MAX_LENGTH = 1001;
unsigned long long int* longitudBST;
int index;
bool ini = false;

unsigned long long int* getArray()
{
  if(ini == false)
  {
    longitudBST = new unsigned long long int [MAX_LENGTH];
    longitudBST[0] = longitudBST[1] = 1;
    index = 1;
    ini = true;
  }
  return longitudBST;
}

void calculaLongitud(int i)
{
  for(int j=index + 1; j <= i;j++)
  {
    longitudBST[j] = 0;
    for(int k=1; k <= j/2; k++)
    {
      longitudBST[j] += longitudBST[k - 1] * longitudBST[j - k];
    }
    longitudBST[j] = 2 * longitudBST[j];
    if(j % 2 == 1)
    {
      longitudBST[j] += longitudBST[j/2] * longitudBST[j/2];
    }
  }
  index = i;
}

unsigned long long int getNumberOfBST(int i)
{
  unsigned long long int  numberOfBST;
  unsigned long long int* array = getArray();
  if(index >= i) numberOfBST = array[i];
  else
  { 
    calculaLongitud(i);
    numberOfBST = array[i];
  }
  return numberOfBST;
}

void showArray()
{
 for(int i = 0; i < MAX_LENGTH; i++)
 {
   cout << longitudBST[i] << endl; 
 }
}



int main()
{
 int n;
 while(cin >> n)
 {
    cout << getNumberOfBST(n) << endl;
    // showArray();
 }
 delete[] longitudBST;
}

