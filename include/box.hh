class Box
{
   public:
      Box();
      std::string name;
      unsigned int length;   // Length of a box
      unsigned int width;    // width of a box
      unsigned int height;   // Height of a box

      void report();
      void setWidth( double inWidth) ;
};
