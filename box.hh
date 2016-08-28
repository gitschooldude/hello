class Box
{
   public:
      Box();
      std::string name;
      double length;   // Length of a box
      double width;    // width of a box
      double height;   // Height of a box

      void report();
      void setWidth( double inWidth) ;
};
