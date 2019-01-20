# Start from a centos6.8 base image
FROM centos:centos6.8

RUN yum install -y vim-enhanced vim-X11 gcc gcc-c++
RUN yum install -y git

# Copy the project into the image
COPY . /apps/ 

# Run a bash shell
CMD ["/bin/bash"]
