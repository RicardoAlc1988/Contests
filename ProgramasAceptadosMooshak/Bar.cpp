#include <stdlib.h>
#include <stdio.h>
#include <iostream>

int* LongVarillas;

int Longitud_Varillas(int d)
{
	int longitud = 0;
	for(int i=0;i<d;i++){
		longitud+=LongVarillas[i];
	}
return longitud;
}

void Generar(int* s,int nivel, int& sum_acumulada, int& cant_maxima)
{
	s[nivel-1]++;
	if(s[nivel-1]==0){
	cant_maxima= cant_maxima - LongVarillas[nivel-1];
	}
	if(s[nivel-1]==1){
	sum_acumulada= sum_acumulada + LongVarillas[nivel-1];
	}
}

void Retroceder(int* s,int& nivel,int& cant_maxima,int& sum_acumulada)
{
	sum_acumulada= sum_acumulada - LongVarillas[nivel-1];
	cant_maxima= cant_maxima + LongVarillas[nivel-1];
	s[nivel-1]=-1;
	nivel--;

}

void Inicializa(int* s, int r)
{
	for(int i=0;i<r;i++) s[i]=-1;
	
}

void Muestra(int* s, int d)
{
	for(int i=0;i<d;i++) std::cout<<s[i]<<" ";
	std::cout<<"\n";
}
int Bars(int n, int d) // Implementación mediante un árbol binario
{
int sol_act = 0;
int cant_maxima = Longitud_Varillas(d);
int* s = new int[d];
Inicializa(s,d);
int sum_acumulada = 0;
int nivel=1;
int fin = 0;
	while(nivel!=0 && fin!=1){
		Generar(s,nivel,sum_acumulada,cant_maxima);
		if(nivel==d && sum_acumulada==n) return  1;
		else{
			if(nivel<d && sum_acumulada<=n && cant_maxima>=n-sum_acumulada){
				nivel++;
			}
			else{
				while(s[nivel-1]==1){
					Retroceder(s,nivel,cant_maxima,sum_acumulada);	
				}
			}
		}
	}
return fin;
}



int main(){

int t;
int n;
int d;
std::cin>> t;
for(int i=0;i<t;i++){
	std::cin>>n;
	std::cin>>d;
	LongVarillas = new int[d];
	for(int j=0;j<d;j++) std::cin>> LongVarillas[j];
	int aux=Bars(n, d);
	if(aux==0) std::cout<<"NO"<<"\n";
	else std::cout<<"YES"<<"\n";
delete[] LongVarillas;
}


return 0;
}
