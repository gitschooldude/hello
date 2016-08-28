#include <iostream>
#include "box.hh"

using namespace std;
int main(int argc, char** argv)
{  
  Box box1;
  Box box2;
  Box boxA;
  Box boxB;
  Box boxD;
  Box boxE;

  box1.setWidth(15.0);
  cout<<"Hello World!" << endl;
  cout<<"Box1:" << endl;
  box1.Report();
  cout<<"Box2:" << endl;
  box2.Report();
  cout<<"BoxA:" << endl;
  boxA.Report();
  cout<<"BoxB:" << endl;
  boxB.Report();
  cout<<"BoxD:" << endl;
  boxD.Report();
  cout<<"BoxE:" << endl;
  boxE.Report();

  return 0;
}
