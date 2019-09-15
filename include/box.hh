#include <iostream>
#include <fstream>
class Box
{
   private:
      std::ofstream f;
   public:
      Box();
      std::string name;
      unsigned int length;   // Length of a box
      unsigned int width;    // width of a box
      unsigned int height;   // Height of a box

      void report(bool also_to_file=false);
      void setWidth( double inWidth) ;
      std::string color;   // Color of the box
};
