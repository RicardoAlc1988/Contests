#include <iostream>
#include <list>
#include <limits.h>
using namespace std;

int* maxSub;
int* alturaPro;
int n;
int pElemento = 0;

void leeDatos(){
	list<int> objInterceptar;
	n = 0;
	int m;
	cin >> m;
	pElemento = m;
	while(m!=-1){
		objInterceptar.push_back(m);
		n++;
		cin >> m;
	}

	maxSub = new int[n];
	alturaPro = new int[n];
	list<int>::iterator it = objInterceptar.begin();
	int i=0;
	while(it != objInterceptar.end()){
		alturaPro[i] = *it;
		i++;
		it++;
	}
}

int maximo(int a, int b){
	if(a < b)
		return b;
	else
		return a;
}

int maximoInterceptaciones(){
	// Caso base
	int max, maxLongSub;
	maxSub[0] = maxLongSub = 1;

	// Caso general
	for(int i=1; i < n; i++){
		max = 1;
		for(int j=0; j < i; j++){
			if(alturaPro[i] <= alturaPro[j])
				max = maximo(max, 1 + maxSub[j]);
		}
	maxSub[i] =  max;
	if(maxSub[i] > maxLongSub)
		maxLongSub = maxSub[i];
	}
return maxLongSub;
}


void muestraPro(){
	for(int i=0; i < n; i++)
		cout << maxSub[i] << endl;
}

void liberaEstructuras(){
	delete[] maxSub;
	delete[] alturaPro;
}


int main(){
	int numCasos = 1;
	while(pElemento!=-1){

		leeDatos();
		if(pElemento!=-1){
			if(numCasos > 1)
				cout << endl;
			cout << "Test #" << numCasos << ":" << endl;
			cout << "  maximum possible interceptions: " << maximoInterceptaciones() << endl;
		}
		numCasos++;
		liberaEstructuras();
	}
return 0;
}
