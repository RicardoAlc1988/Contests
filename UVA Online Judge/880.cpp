#include <iostream>
#include <math.h>
#include <stdint.h>
using namespace std;

struct QPoint
{
  int64_t  X;
  int64_t  Y;
};

int64_t GetCantorDiagonal(int64_t i)
{
  return (int64_t)ceil((-1 + sqrt(1 + 8 * i)) / 2);
}

QPoint GetCantorNumber(int64_t i)
{
  QPoint qPoint;
  int64_t  cantorDiagonal = GetCantorDiagonal(i);
  int64_t  D = (cantorDiagonal*(cantorDiagonal + 1)) / 2 - i;
  qPoint.X  = D + 1;
  qPoint.Y = cantorDiagonal - D;
  return qPoint;
}

void MuestaQPoint(QPoint qPoint)
{
	cout << qPoint.X
		<< "/"
		<< qPoint.Y
		<< endl;
}


int main()
{
  int64_t i;
  while(cin >> i)
  {
    MuestaQPoint(GetCantorNumber(i));
  }
}
