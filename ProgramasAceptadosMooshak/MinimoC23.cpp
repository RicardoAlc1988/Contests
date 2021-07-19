#include <stdlib.h>
#include <iostream>
#include <stdio.h>
#include <math.h>
#include <limits.h>


double log(int x, int b)
{
	return log10(x)/log10(b);
}

int Minimo_C23(int m)
{
	int min=INT_MAX;
for(int i=0;i<=(int)(floor(log(m,2))+1);i++){
	for(int j=0;j<=(int)(floor(log(m,2))+1-i);j++){
		if((int)(pow(3,i)*pow(2,j))>=m && (int)(pow(3,i)*pow(2,j)<=min)) min=(int)(pow(3,i)*pow(2,j));
		}
	}

return min;

}

int main(){
int m;
std::cin >>m;
while(m!=0){
	std::cout<<Minimo_C23(m)<<"\n";
	std::cin>>m;
	}
return 0;
}
