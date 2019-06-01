#include <iostream> 
#include "box.hh"
#include <vector>

using namespace std;
int main(int argc, char** argv)
{  
  Box box2;
  Box boxA;
  Box boxB;
  Box boxD;
  Box boxE;
  Box boxF;

  vector <Box*> user_boxes;
  for (int i = 1; i < argc; ++i) {
      cout << "Creating user-defined box: " <<  argv[i] << endl; 
      Box * mybox = new Box();
      mybox->name = argv[i];
      user_boxes.push_back(mybox);
  }


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

  vector<Box*>::iterator it;
  for(it = user_boxes.begin(); it != user_boxes.end(); it++ ) {
      cout << "User-defined box: " <<  (*it)->name << endl; 
      (*it)->report();
  }
  cout<<"We're done!" << endl;

  // always return zero
  // comment here
  return 0;
}
