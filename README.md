# Manual

## 0. Prerequisites
- Installation of Pylon SDK 5.1.0
- Installation of CUDA Version 10.0 (Due to the tensorflow compatibility)
- Make sure the `LD_LIBRARY_PATH` and `PATH` environment variables
```sh
LD_LIBRARY_PATH=.:/usr/local/lib:/opt/pylon5/lib64:/usr/local/cuda/lib64:/usr/local/cuda/lib64/stubs
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin/snap/bin:/usr/local/cuda/bin
```

## 1. YOLO/Darknet Installation
- https://pjreddie.com/darknet/install/
- Refer to the section __***Compiling With CUDA***__

```sh
git clone https://github.com/pjreddie/darknet.git
cd darknet
# change the value of GPU=1 of Makefile then,,,
make
```
- Download yolov3 data file
```sh
cd cfg
wget https://pjreddie.com/media/files/yolov3.weights
```
