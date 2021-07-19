#include <iostream>
#include <stdio.h>
#include <stdlib.h>
# include <limits.h>
using namespace std;

int* Dietas;
int** Calorias;

int Minimo(int a, int b)
{
	if(a>=b) return b;
	else return a;
}

int Parte_Positiva(int a)
{
	if(a>=0) return a;
	else return 0;

}

int Aux(int a, int b){
	if(a==INT_MAX) return INT_MAX;
	else return  a+b;

}
int Dieta_Optima(int d, int n)
{

	//Casos base
for(int i=0; i<=d; i++) Calorias[i][0] = 0;
for(int j=1; j<=n/10; j++) Calorias[0][j] = INT_MAX;

	for(int i=1;i<=d;i++){
		for(int j=1;j<=n/10;j++){
			Calorias[i][j] = Minimo(Calorias[i-1][j],Aux(Calorias[i-1][Parte_Positiva(j-(Dietas[i-1]/10))], Dietas[i-1]));
		}
	}


return Calorias[d][n/10];

}


int main(){
// Verificación el algoritmo 

int num_cas; // Número de casos
int n; // número de calorías
int d; //número de cursos
cin>>num_cas;
for(int i=0;i<num_cas; i++){
	cin>> n;
	cin>> d;
	Dietas = new int[d];
	for(int h=0;h<d;h++)  cin>> Dietas[h];
	Calorias = new int*[d+1];
for(int i=0;i<=d;i++) Calorias[i] = new int[n/10+1];
int aux = Dieta_Optima(d,n);
if(aux!=INT_MAX) cout<<aux<<"\n";
else cout<<"NO SOLUTION"<<"\n";
delete[] Dietas;
for(int k=0; k<=d;k++) delete[] Calorias[k];
}
}
