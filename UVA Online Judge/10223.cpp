// 10223.cpp : Defines the entry point for the console application.
//

#include <iostream>
using namespace std;

const int MAX_LONG = 22;
long long int L[]  = 
	{1,1,2,5,14,42,132,429,1430,4862,16796,58786,208012,742900,2674440,9694845,35357670,129644790,477638700,1767263190,6564120420,24466267020};
long long int* MaxNumTrees;

void InicializaEstructuras()
{
	MaxNumTrees = new long long int[MAX_LONG];
}


void MaxNumberOfTrees(int n)
{
  if (n == 0 || n == 1)
  {
    MaxNumTrees[n] = 1;
  }
  else
  {
    long long int resul = 0;
    for (int j = 1; j <= n; j++)
    {
      resul += MaxNumTrees[n - j] * MaxNumTrees[j - 1];
    }
   MaxNumTrees[n] = resul;
   }
}

void CalculaMaximoNumeroArbolesBinarios()
{
	for (int i = 0; i < MAX_LONG; i++)
	{
		MaxNumberOfTrees(i);
	}
}

void MuestraArray()
{
	for (int i = 0; i < MAX_LONG; i++)
	{
		cout << MaxNumTrees[i] << endl;
	}
}

long long int GetMaxLenghtOfBinTree(int idx)
{
	return MaxNumTrees[idx];
}

void LiberaEstructuras()
{
	delete[] MaxNumTrees;
}

int FromMaxNumberOfTreesToNumberOfNodes(int numberOfTrees)
{
	// Binary search
	int i, j, m;
	i = 0;
	j = MAX_LONG - 1;
	m = (i + j) / 2;
	while (j - i > 1)
	{
		if (MaxNumTrees[m] == numberOfTrees)
		{
			return m;
		}
		else
		{
			if (MaxNumTrees[m] > numberOfTrees)
			{
				j = m;
			}
			else
			{
				i = m;
			}
			m = (i + j) / 2;
		}
	}
	return m + 1;
}

int main()
{
        InicializaEstructuras();
	CalculaMaximoNumeroArbolesBinarios();
	// MuestraArray();
	int n;
	while(cin>> n)
        {
		cout << FromMaxNumberOfTreesToNumberOfNodes(n) << endl;
	}
	LiberaEstructuras(); 
	return 0;
}

