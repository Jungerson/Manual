# Manual

## 0. Prerequisites
- Installation of Pylon SDK 5.1.0
- Installation of CUDA Version 10.0 (Due to the tensorflow compatibility)
  - https://developer.nvidia.com/cuda-10.0-download-archive?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=1804&target_type=deblocal
  ```sh
  sudo dpkg -i cuda-repo-ubuntu1804-10-0-local-10.0.130-410.48_1.0-1_amd64.deb
  sudo apt-key add /var/cuda-repo-<version>/7fa2af80.pub
  sudo apt-get update
  sudo apt-get install cuda
  ```
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
- Download pre-trained weights for convolutional layers
```sh
cd cfg
wget http://pjreddie.com/media/files/darknet53.conv.74
```

## 2. YOLO/Darknet Training for Object Detection
- Annotate objects using `LabelImg` (https://github.com/tzutalin/labelImg)
  - Once you finish annotating, it generates <filename>.txt files for each image files and `*.data` and `*.names` as well
  - `classes.txt` file contains the object names and each <line number - 1> will be the object ids.
- Generate training / test dataset for darknet training using `generate_filenames.py` (https://github.com/NeuronAware/Manual/blob/master/generate_filenames.py)
    ```sh
    $ python3 generate_filenames.py
    ```
  - It generates `train.txt` and `test.txt` files that contain image file names for darknet training
- Place generated `train.txt`, `test.txt`, `model1.data` and `model1.names` files under one step upper directory of `darknet`
- Copy & modify darknet configuration file from `~darknet/cfg/yolov3.cfg`
    ```sh
    cp yolov3.cfg model1.cfg
    ```
  - Modfify `model1.cfg` file as following instruction (https://github.com/AlexeyAB/darknet#how-to-train-to-detect-your-custom-objects)
    - A sample file has been uploaded to this repo (https://github.com/NeuronAware/Manual/blob/master/model1.cfg)
- Start training 
  ```sh
  darknet$ ./darknet detector train ../model1.data cfg/model1.cfg data/darknet53.conv.74
  ```
  - It takes 70 minutes for each 1000 epochs(batches)
  - Once the training done, it generates `backup/model1_final.weights` file. It should be moved under `~VisionAware/data`
  
