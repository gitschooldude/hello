#include <iostream>
#include "box.hh"

using namespace std;

Box::Box() {
    length = 3;
    width  = 4;
    height = 8;
    char * foo = NULL;
    cout << *foo;
}

void Box::report() {
    cout << "  Length: " << length << endl;
    cout << "  Width:  " << width << endl;
    cout << "  Height: " << height << endl;

}

void Box::setWidth( double inWidth) {
    width = inWidth;
}
