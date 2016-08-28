#include <iostream>
#include "box.hh"

using namespace std;
int main(int argc, char** argv)
{  
  Box box2;
  Box boxA;
  Box boxB;
  Box boxD;
  Box boxE;
  Box boxF;

  cout<<"Hello World!" << endl;
  cout<<"Box2:" << endl;
  box2.report();
  cout<<"BoxA:" << endl;
  boxA.report();
  cout<<"BoxB:" << endl;
  boxB.report();
  cout<<"BoxD:" << endl;
  boxD.report();
  cout<<"BoxE:" << endl;
  boxE.report();

  return 0;
}
