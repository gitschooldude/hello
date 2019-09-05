#include <iostream> 
#include "box.hh"
#include <vector>
#include <unistd.h>

using namespace std;
int main(int argc, char** argv)
{  
  Box box2;box2.name = "box2";
  Box boxA;boxA.name = "boxA";
  Box boxB;boxB.name = "boxB";
  Box boxD;boxD.name = "boxD";
  Box boxE;boxE.name = "boxE";
  Box boxF;boxF.name = "boxF";

  vector <Box*> user_boxes;
  for (int i = 1; i < argc; ++i) {
      cout << "Creating user-defined box: " <<  argv[i] << endl; 
      cout << "  Simulating a 10 second \"creation time\"... " <<  endl; 
      usleep(10e6);
      Box * mybox = new Box();
      mybox->name = std::string(argv[i]);
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
      (*it)->report(true);
  }
  cout<<"We're done!" << endl;

  // always return zero
  // comment here
  return 0;
}
