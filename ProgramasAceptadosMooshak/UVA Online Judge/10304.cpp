#include <algorithm>
#include <limits.h>
#include <iostream>
using namespace std;


 struct costeMinStr
    {
        int costeMinimo;
	int costeNodosArbol;
        costeMinStr() { costeMinimo = 0; costeNodosArbol = 0; }
    };

costeMinStr** ArbolMinimo;
int* arrayCostes;

int minimo(int a, int b)
{
  if(a < b) return a;
  else return b;
}

void InicializaEstructuras(int n)
{
  int r;
  arrayCostes = new int[n+1];
  for(int j=0; j < n; j++)
  { 
    cin >> r;
    arrayCostes[j] = r;
  }
  ArbolMinimo = new costeMinStr*[n+1];
  for(int i = 0; i <= n; i++)
  {
    ArbolMinimo[i] = new costeMinStr[n+1];
  } 
}

int ArbolCosteMinimo(int n)
{
  int a, b, c, d;
  int min;
  int costeActual;
  // Caso Base
  for(int i=1; i <= n; i++)
  {
    ArbolMinimo[1][i].costeNodosArbol = arrayCostes[i-1];
  }

  for(int i=2; i <= n; i++)
  {
    for(int j=1; j <= n-(i-1); j++)
    {
      ArbolMinimo[i][j].costeNodosArbol += ArbolMinimo[i-1][j].costeNodosArbol + arrayCostes[j+i-2];
      min = INT_MAX;
      for(int k=0; k <i; k ++)
      {
 	  a = ArbolMinimo[k][j].costeMinimo;
	  b = (k+j+1 <= n) ? ArbolMinimo[i-k-1][k+j+1].costeMinimo : 0;
          c = ArbolMinimo[k][j].costeNodosArbol;
          d = (k+j+1 <= n) ? ArbolMinimo[i-k-1][k+j+1].costeNodosArbol : 0;
          costeActual = a + b + c +d;

          min =  minimo(min, costeActual);
      }
      ArbolMinimo[i][j].costeMinimo = min;
    }
  }
  return ArbolMinimo[n][1].costeMinimo;
}

void liberaEstructuras(int n)
{
  delete[] arrayCostes;
  for(int i=0; i <= n; i++) delete[] ArbolMinimo[i];
}

void MuestraTabla(int n)
{
  for(int i=0; i <= n; i++)
  {
   for(int j=0; j <= n; j++)
   {
     cout << ArbolMinimo[i][j].costeMinimo  << " - " << ArbolMinimo[i][j].costeNodosArbol << " ";
   }
   cout << endl;
  }
}

int main()
{
  int n;
  while(cin >> n)
  {
   InicializaEstructuras(n);
   cout << ArbolCosteMinimo(n) << endl;
   liberaEstructuras(n);
  }
}
