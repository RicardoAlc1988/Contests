#include <iostream>
#include <limits.h>
using namespace std;

int* alto;
int* ancho;
int* Tabla;
int* Tabla2;

int Maximo(int a, int b){
	if(a>b) return a;
	else return b;
}

void TomaDatos(int N){
	alto = new int[N];
	ancho = new int[N];
	Tabla = new int[N];
	Tabla2 = new int[N];
	for(int i=0;i<N;i++) cin>> alto[i];
	for(int i=0;i<N;i++) cin>> ancho[i];
}


void LiberaEstructuras(int N){
	delete alto;
	delete ancho;
	delete Tabla;
	delete Tabla2;
}



void MaximaSubcadena(int N){
	int maximo = ancho[0];
	int maximo2 = ancho[0];
	int max = INT_MIN;
	int max2 = INT_MAX;
	Tabla[0] = Tabla2[0] = ancho[0];
	for(int i=1;i<N;i++){
		max = ancho[i];
		max2 = ancho[i];
		for(int j=0;j<i;j++){
			if(alto[i]>alto[j])max = Maximo(max,Tabla[j] + ancho[i]);
			if(alto[i]<alto[j])max2 = Maximo(max2,Tabla2[j] + ancho[i]);
		}
	Tabla[i] = max;
	Tabla2[i] = max2;
	if(Tabla[i]>maximo) maximo = Tabla[i];
	if(Tabla2[i]>maximo2) maximo2 = Tabla2[i];
	max = INT_MIN;
	max2 = INT_MIN;
	}
if(maximo>=maximo2) cout<<". Increasing ("<<maximo<<"). "<<"Decreasing ("<<maximo2<<")."<<"\n";
else cout<<". Decreasing ("<<maximo2<<"). "<<"Increasing ("<<maximo<<")."<<"\n";
}

int main(){
int t,N;
cin>> t;
for(int i=0;i<t;i++){
	cin>> N;
	TomaDatos(N);
	cout<<"Case "<<i+1;
	MaximaSubcadena(N);
	LiberaEstructuras(N);
}
return 0;
}
