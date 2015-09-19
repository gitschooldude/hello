#include <iostream>
#include "box.hh"

using namespace std;
int main(int argc, char** argv)
{  
  Box box1;
  Box box2;
  Box boxF;

  box1.setWidth(15.0);
  cout<<"Hello World!" << endl;
  cout<<"Box1:" << endl;
  box1.report();
  cout<<"Box2:" << endl;
  box2.report();
  cout<<"BoxF:" << endl;
  boxF.report();

  return 0;
}
