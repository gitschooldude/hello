all:
	g++ -Wall -O0 -g -o hello hello.cpp box.cpp
clean:
	rm -f hello
