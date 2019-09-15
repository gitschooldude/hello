#include <iostream>
#include "box.hh"

using namespace std;

Box::Box() {
    length = 1;
    width  = 2;
    height = 8;
    color = "green";
}

void Box::report(bool also_to_file) {
    cout << " Name: " << name << endl;
    cout << " Length: " << length << endl;
    cout << " Width:  " << width << endl;
    cout << " Height: " << height << endl;
    cout << " Color: " << color << endl;

    if (also_to_file) {
        // Print info to file of same name as Box
        std::string filename = std::string("./output/") + name + std::string(".txt");
        f.open (filename.c_str());
        f << " Name: " << name << endl;
        f << " Length: " << length << endl;
        f << " Width:  " << width << endl;
        f << " Height: " << height << endl;
        f << " Color: " << color << endl;
        f.close();
    }
}

void Box::setWidth( double inWidth) {
    width = inWidth;
}
