.PHONY: all clean build-centos6  run-centos6

all:
	g++ -Wall -O0 -g -o hello -I./include src/hello.cpp src/box.cpp
clean:
	rm -f hello

build-centos6:
	docker build  -t hello-centos6 -f docker/centos6/Dockerfile .

run-centos6: build-centos6
	docker run -ti --rm hello-centos6

