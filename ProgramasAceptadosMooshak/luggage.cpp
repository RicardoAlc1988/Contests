#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <ctype.h>
using namespace std;


typedef struct Celda{

	int elem;
	Celda* sig;
	Celda* ant;
}CeldaRep;

typedef CeldaRep * CeldaAp;

typedef struct Lista{
	CeldaAp primera;
	int cardinal;

}ListaRep;

typedef ListaRep * ListaAp;

Lista* ListaCrea(){
	ListaAp l = new ListaRep;
	l->primera = new CeldaRep;
	l->primera->sig=l-> primera;
	l->primera->ant=l-> primera;
	l-> cardinal = 0;
	return l;
}

void InsertaLista(ListaAp l,int e){

	CeldaAp aux2 = new CeldaRep;
	CeldaAp aux = l-> primera-> ant;
	aux2-> elem = e;
	aux2-> sig = aux-> sig;
	aux2-> ant = aux;
	aux2-> ant-> sig = aux2;
	aux2-> sig-> ant = aux2;
	l-> cardinal++;
}

void MuestraListaCreciente(ListaAp l)
{
	CeldaAp aux = l->primera;
	while(aux->sig!=l->primera){ 
	cout<<aux->sig->elem<<" ";
	aux= aux->sig;
	}
cout<<"\n";
}


void MuestraListaDecreciente(ListaAp l)
{
	CeldaAp aux = l->primera;
	while(aux->ant!=l->primera){ 
	cout<<aux->ant->elem<<" ";
	aux= aux->ant;
	}
cout<<"\n";
}

void LiberaLista(ListaAp l)
{
	CeldaAp ultima = l-> primera-> ant;
	while(l-> primera!=ultima){ 
		CeldaAp aux = l->primera;
		l->primera = l->primera-> sig;
		delete aux;
		
	}


	delete (l-> primera);
	delete(l);
}

// Hasta aquí la implementación de la estructura auxiliar celda con doble enlace.
ListaAp weights;

int TotalSum(ListaAp p){
	int sum=0;
	for(CeldaAp aux=p->primera->sig; aux!=p->primera;  aux=aux->sig) sum = sum + aux-> elem;
	return sum;
}

void Inicializate(int* a,int m, int c){
	for(int i=0;i<m;i++) a[i] = c;
}

void Generar(int* s,int& nivel, int& actualweight, int& totalweight,CeldaAp& aux){
	s[nivel-1]++;
	if(s[nivel-1]==1){
	actualweight+=aux->sig->elem;
	totalweight-=aux->sig->elem;
	}
}

void Retroceder(int* s,int& nivel, int& actualweight,int& totalweight,CeldaAp& aux){
	s[nivel-1]=-1;
	actualweight-=aux->sig->elem;
	totalweight+=aux->sig->elem;
	nivel--;
	aux = aux->ant;
}

int luggage(){

int actualweight = 0;
int totalweight = TotalSum(weights);
CeldaAp aux = weights->primera;
int* s = new int[weights-> cardinal];
Inicializate(s,weights-> cardinal,-1);
int nivel = 1;
int sameweight=0;
	while(nivel!=0){
		Generar(s,nivel,actualweight,totalweight,aux);
		// for(int i=0;i<weights-> cardinal;i++) cout<<s[i]<<"\n";
		if(actualweight==totalweight) return 1;
		else if(actualweight<=totalweight && nivel<weights->cardinal){
			nivel++;
			aux = aux-> sig;
			}
			else{
				while(nivel!=0 && s[nivel-1]==1){
					Retroceder(s,nivel,actualweight,totalweight,aux);
				}
			}
	}
return sameweight;
}


int main(){
int t; //Number of cases
cin>> t;
for(int i=0;i<t;i++){
	weights = ListaCrea();
	int n;
	cin>> n;
	InsertaLista(weights,n);
	while(getchar()!='\n'){
		cin>> n;
		InsertaLista(weights,n);
	}

	int aux = luggage();
	if(aux==0) cout<<"NO"<<"\n";
	else cout<<"YES"<<"\n";
	LiberaLista(weights);
}
return 0;
}
