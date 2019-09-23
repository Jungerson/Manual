# Darknet(YOLO) Training Procedure
## 0. Install `labelImg`
- https://github.com/tzutalin/labelImg
- For windows - https://github.com/tzutalin/labelImg#windows

## 1. Subpart classification
- Open a sample model image
- Start annotating and classify subparts
- Switch the format of saving file from Pascal/VOC to YOLO
- Save the result in order to get the `classes.txt`
- Replace the contents of `data/predefined_classes.txt` to `classes.txt`
- Distribute the `predefined_classes.txt` file to the team
- Start annotating 

## 2. Meta Model Info Manipulation
- Make an excel sheet for subpart information - https://docs.google.com/spreadsheets/d/1-zj_If2AKV3c7wlbcEBxU5eSV4RvYh0A364nZ1_Ko20/edit?usp=sharing
- Run the script insert_items.py with exported csv file to insert into DynamoDB

## 3. Darknet Training
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
  darknet$ ./darknet detector train training_100/LX2.data training_100/LX2.cfg darknet53.conv.74 -dont_show -mjpeg_port 8090 -map
  ```
  - It takes 70 minutes for each 1000 epochs(batches)
  - Once the training done, it generates `backup/model1_final.weights` file. It should be moved under `~VisionAware/data`
  
