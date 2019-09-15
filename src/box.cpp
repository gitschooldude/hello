#include <iostream>
#include "box.hh"

using namespace std;

Box::Box() {
    length = 1;
    width  = 2;
    height = 8;
    color = "green";
}

void Box::report() {
    cout << " Length: " << length << endl;
    cout << " Width:  " << width << endl;
    cout << " Height: " << height << endl;
    cout << " Color: " << color << endl;

}

void Box::setWidth( double inWidth) {
    width = inWidth;
}
