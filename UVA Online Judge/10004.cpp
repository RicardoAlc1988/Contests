#include<iostream>
#include <list>
#include <queue>
using namespace std;

int n;
int l;
list<int>* G;
int* padre;
bool* color;
queue<int> C;


void InicializaEstructuras()
{
  G = new list<int>[n];
  padre = new int[n];
  color = new bool[n];
  for(int i=0; i < n; i++)
  {
    padre[i] = -1;
    color[i] = false;
  }
}

bool ColorHijo(int ptrPadre)
{
  if(!color[ptrPadre])
  {
    return true;
  }
  else
  {
    return false;
  }
}

bool LeeGrafo()
{
  int r,s;
  cin>> n;
  if(n == 0)
  {
    return false;
  }
  cin>> l;
  InicializaEstructuras();
  for(int i=0; i < l; i++)
  {
    cin>> r;
    cin>> s;
    G[r].push_back(s);
    G[s].push_back(r);
  }
return true;
}

bool EsBicororeable(int v)
{
  int x;
  padre[v] = v;
  C.push(v);
  while(!C.empty())
  {
    x = C.front();
    C.pop();
    for (list<int>::iterator it=G[x].begin(); it != G[x].end(); it++)
    {
      if(padre[*it] == -1)
      {
        padre[*it] = x;
        color[*it] = ColorHijo(x);
        C.push(*it);
      }
      
      else
      {
        if(color[*it] == color[x])
         {
           return false;
         }
      }
    }
  }
return true;
}

void LiberaEstructuras()
{
  delete[] G;
  delete[] padre;
  delete[] color;
  while(!C.empty())
  {
    C.pop();
  }
}

int main()
{
  while(LeeGrafo())
  {
    if(EsBicororeable(0))
    {
      cout<< "BICOLORABLE." << endl;
    }
    else
    {
      cout<< "NOT BICOLORABLE." << endl;
    }
    LiberaEstructuras();
  }
return 0;
}
