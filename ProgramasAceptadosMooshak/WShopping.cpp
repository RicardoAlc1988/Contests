#include <iostream>
#include <sys/time.h>
#include <stdlib.h>
#include <stdio.h>
# include <limits.h>
using namespace std;

typedef struct Celda{

	int elem;
	Celda* sig;	
}CeldaRep;

typedef CeldaRep * CeldaAp;

typedef struct Lista{

	CeldaAp primera;	
}ListaRep;

typedef ListaRep * ListaAp;

Lista* ListaCrea(){
	ListaAp l = new ListaRep;
	l->primera = new CeldaRep;
	l->primera->sig=NULL;
	return l;
}

void InsertaLista(ListaAp l,int e){

	CeldaAp aux = new CeldaRep;
	aux-> elem =e;
	aux->sig = l->primera-> sig;
	l->primera->sig = aux;
	
	
}

void MuestraLista(ListaAp l)
{
	CeldaAp aux = l->primera;
	while(aux->sig!=NULL){ 
	cout<<aux->sig->elem<<" ";
	aux= aux->sig;
	}
cout<<"\n";
}

void LiberaLista(ListaAp l)
{
	
	while(l->primera!=NULL){ 
		CeldaAp aux = l-> primera;
		l->primera = l->primera->sig;
		delete aux;
	}
	delete l;
}

// Hasta aquí la implementación de la estructura auxiliar celda
int** MaxGasto;
ListaAp* Precio_objetos;

int Aux(int a, int b)
{
	if(a==INT_MIN) return INT_MIN;
	else return a+b;
}
int Maximo(int a,int b)
{
	if(a>=b) return a;
	else return b;
}

int Wedding_Shopping(int C, int D) // Cantidad de tipos de objetos a comprar y de dinero disponible respectivamente
{
int sol_act=INT_MIN;
	//Casos base: No tenemos objetos o dinero con que comprarlos.
for(int i=1;i<=C;i++) MaxGasto[i][0]=INT_MIN;

for(int j=0;j<=D;j++) MaxGasto[0][j]=0;


	// Caso General
	for(int i=1;i<=C;i++){
		for(int j=1;j<=D;j++){
			for(CeldaAp aux=Precio_objetos[i-1]->primera->sig; aux!=NULL;  aux=aux->sig){
				if(j-aux-> elem>=0){
					sol_act = Maximo(sol_act,Aux(MaxGasto[i-1][j-aux-> elem], aux-> elem));
				}
			}
		MaxGasto[i][j] = sol_act;
		sol_act = INT_MIN;	
		}

	}
return MaxGasto[C][D];
}


int main(){
int N; // numero de casos
int M; // Dinero disponible
int C; // Tipos de prendas
int K;
int aux;
cin>> N;
for(int i=0;i<N;i++){
	cin>>M;
	cin>>C;
	Precio_objetos = new ListaAp[C];
	for(int i=0;i<C;i++) Precio_objetos[i] = ListaCrea();
	MaxGasto = new int*[C+1];
	for(int i=0;i<=C;i++) MaxGasto[i] =new int[M+1];
	for(int i=0;i<C;i++){
		cin>> K;
		for(int j=0;j<K;j++){
			cin>> aux;
			InsertaLista(Precio_objetos[i],aux);
		}
	}
	aux=Wedding_Shopping(C,M);
	if(aux==INT_MIN) cout<<"no solution"<<"\n";
	else cout<<aux<<"\n";
	for(int i=0;i<=C;i++) delete[] MaxGasto[i];
	for(int i=0;i<C;i++) LiberaLista(Precio_objetos[i]);
}

return 0;
}
