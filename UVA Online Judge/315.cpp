#include <iostream>
#include <list>
using namespace std;


int* bajo;
int* nbpp;
int N, numbpp, hijosRaiz;
list<int>* G;
bool* esPuntoArticulacion;
int* arcosArbol;



void inicializaEstructuras(void)
{
  esPuntoArticulacion =  new bool[N];
  arcosArbol = new int[N];
  G = new list<int>[N];
  nbpp = new int[N];
  bajo = new int[N];
  for(int i=0; i < N; i++)
  {
    esPuntoArticulacion[i]=false;
    arcosArbol[i]=-1;
    nbpp[i]=-1;
    bajo[i]=-1;
  }
}

void leeGrafo(void)
{
  int nodo, i;
   
 
   inicializaEstructuras();
   cin >> nodo;
   while(nodo!=0)
   {
     do
     { 
       cin >> i;
       G[nodo-1].push_back(i-1);
       G[i-1].push_back(nodo-1);
       
     }while(cin.peek()!='\n');
    cin >> nodo;
   }
}

void liberaEstructuras(void)
{
  delete[] esPuntoArticulacion;
  delete[] arcosArbol;
  delete[] G;
  delete[] nbpp;
  delete[] bajo;
}



int minimo(int a, int b)
{
  if(a < b) return a;
  else return b;
}

void esPuntoArt(int v,int it)
{
      if(nbpp[v]==0)
      {
	hijosRaiz++;
        if(hijosRaiz>1)
          esPuntoArticulacion[v]=true;
      }
      else if(bajo[it] >= nbpp[v])
        esPuntoArticulacion[v]=true;
}

void bpp(int v)
{
  for (std::list<int>::iterator it=G[v].begin(); it != G[v].end(); it++)
  {
    if(nbpp[*it]==-1)
    {
      numbpp++;
      nbpp[*it] = numbpp;
      bajo[*it] = numbpp;
      arcosArbol[*it]=v;
      bpp(*it);
      bajo[v] = minimo(bajo[v], bajo[*it]);
      esPuntoArt(v, *it);
    }

    else if(arcosArbol[v]!=*it)
     {
     bajo[v] = minimo(bajo[v], nbpp[*it]);
     }
  }
}


void bpp(void)
{
  for(int v=0; v < N; v++)
  {
    if(nbpp[v]==-1)
    {
      nbpp[v]=bajo[v]=arcosArbol[v]=hijosRaiz=numbpp=0;
      bpp(v);;
    }
  }
}


int numeroPuntosArticulacion(void)
{
  int numPuntosArticulacion=0;
  for(int v=0; v<N; v++)
   if(esPuntoArticulacion[v])
    numPuntosArticulacion++;
return numPuntosArticulacion;
}


int main()
{
cin >> N;
while(N!=0)
{
  leeGrafo();
  bpp();
  cout << numeroPuntosArticulacion() << endl;
  liberaEstructuras();
  cin>> N;
}
return 0;
}
