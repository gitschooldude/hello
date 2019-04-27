.PHONY: all clean build-centos6  run-centos6

GCC=g++
INCLUDE=-I./include

all: hello
hello: src/hello.cpp src/box.o
	$(GCC) -Wall -O0 -g -o hello $(INCLUDE) src/*.o src/hello.cpp
clean:
	rm -f hello src/*.o

src/box.o : src/box.cpp
	$(GCC) -c -o src/box.o src/box.cpp $(CFLAGS) $(LDFLAGS) $(INCLUDE)



build-centos6:
	docker build  -t hello-centos6 -f docker/centos6/Dockerfile .

run-centos6: build-centos6
	docker run -ti --rm hello-centos6

