#include <iostream>
# include <limits.h>
using namespace std;

int* ArrayPosiciones;
int* ArrayCapacidadesMaximas;
void Inicializa_Array(int* A, int dim, int Valorini){
	for(int i=0; i<dim;i++){
		A[i] = Valorini;
	}
}

void Pon_Valor(int* A, int r, int s, int Valorini, int& SOA){
	if(r!=s){
		for(int i=r; i<=s; i++){
			if(A[i]==0){
				A[i] = Valorini;
				SOA++;
				}
			}
		}

}


int Quita_Valor(int* A, int r, int s, int Valorini, int& SOA){
int resultado = 0;
	if(r!=s){
		for(int i=r; i<=s; i++){
			if(A[i]==Valorini){
				A[i] = 0;
				SOA--;
				}
			}
	}
return resultado;

}




int RiegaJardin(int L, int N, int S){

int nivel = 1;
int VOA = 0;
int SOA = 0;
int capActual = S;
int* s = new int[N];
int* J = new int[L];

//Inicialización del array de soluciones
Inicializa_Array(s,N,-1);
Inicializa_Array(J,L,0);
//Bucle principal del programa

while(nivel!=0){
	
	s[nivel-1] ++;
	if(s[nivel-1]>=0){
		Pon_Valor(J, ArrayPosiciones[nivel -1] -1 - s[nivel-1],ArrayPosiciones[nivel -1] -1 + s[nivel-1], nivel, SOA);
		if(s[nivel-1]>0) capActual--;
		
	}
	
		if(nivel == N){
			if(SOA>VOA && capActual>=0) VOA = SOA;
	}
	

// Comprobamos si se puede seguir avanzanado
	if(capActual>=0 && 2*capActual + SOA + N - nivel > VOA && nivel!=N) nivel ++;
		
	else{
		
		while(nivel!=0 && s[nivel-1]==ArrayCapacidadesMaximas[nivel-1]){
			Quita_Valor(J, ArrayPosiciones[nivel -1] - 1 - s[nivel-1], ArrayPosiciones[nivel -1] - 1 + s[nivel-1], nivel, SOA);
				capActual = capActual + s[nivel-1];
				s[nivel-1] = -1;
				nivel--;
				
			
			
			}

		}

		

	}
 return VOA;
}

int main(){



int n;
int L;
int N;
int S;
cin>>n;
for(int i =0; i<n; i++){


cin>>L;
cin>>N;
ArrayPosiciones = new int[N];
ArrayCapacidadesMaximas = new int[N];
for(int i = 0; i<N; i++) {
	cin>>ArrayPosiciones[i];
	
}
cin>>S;

for(int i = 0; i<N; i++) {
	cin>>ArrayCapacidadesMaximas[i];
	
}
	
	std::cout<<RiegaJardin(L,N, S)<<"\n";
}


return 0;
}
