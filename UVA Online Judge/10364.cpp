#include <iostream>
#include<stdio.h>
using namespace std;
// Sección de datos

long long int sum;
int N, M, l, it;
const int r = 3;  // Número de 'cortes' a pegar
bool*** SQ;
int* sticksLength;


// Sección de código
void InicializaEstructuras(int a)
{
  sum = 0;
  cin>> M;
  sticksLength = new int[M];
  SQ = new bool**[r];
  
  for(int i=0; i < M; i++)
  {
    cin>> l;
    sticksLength[i] = l;
    sum += sticksLength[i];
  }

  for(int i=0; i < r; i++)
  {
    SQ[i] = new bool*[M+1];
    for(int j=0; j <= M; j++)
    {
      SQ[i][j] = new bool[a];
    }
  }
  it = (sum / (r+1));
}

void MuestraArray(int a)
{
  for(int i=0; i < r; i++)
  {
   for(int j=0; j <= M ; j++)
   {
     for(int k=0; k < a; k++)
     {
       cout << SQ[i][j][k] << " ";
     }
   cout << endl;
   }
  cout << "---"  << endl;
  }
}

bool FormSquare(int a)
{
  // Casos Base
  cout << "----"  << " ";
  SQ[0][0][0] = true;
  for(int i=1; i <= a; i++)
  {
    SQ[0][0][i] = false;
  }

  for(int s=1; s < r; s++)
  {
    for(int j=0; j < a; j++)
    {
      SQ[s][0][j] = false;
    }
  }
  
  // Caso General
  for(int s=0; s < r; s++)
  {
    for(int i=1; i <= M; i++)
    {
      for(int j=0; j < a; j++)
      {
        
 	SQ[s][i][j] = SQ[s][i-1][j];
        
        if(sticksLength[i-1] == j && s > 0 && SQ[s-1][i-1][j] < SQ[s][i][j])
        {
          SQ[s][i][j] = SQ[s-1][i-1][j];
        }
        else
        {
	  if(sticksLength[i-1] < j && SQ[s-1][i][j - sticksLength[i-1]] < SQ[s][i][j])
          {
            SQ[s][i][j] = SQ[s-1][i][j - sticksLength[i-1]];
          }
        }
      }
    }
  }
  
return  0; //SQ[r-1][M][a];
}

void LiberarEstructuras()
{
  for(int s=0; s < r; s++)
  {
    for(int i=0; i <= M; i++)
    {
        delete[] SQ[s][i];
    }
    delete[] SQ[s];
  }
  delete[] SQ;
  delete[] sticksLength;
}


void CanFormSquare()
{
  bool resul;
  for(int a=1; a <= it; a++)
  {
   InicializaEstructuras(a);
   resul = FormSquare(a);
   MuestraArray(a);
   LiberarEstructuras();
   if(resul == true)
     cout << "yes" << endl;
  }
cout << "no" << endl;
}


int main()
{
InicializaEstructuras(1);
FormSquare(1);
MuestraArray(1);
LiberarEstructuras();
return 0;
}
