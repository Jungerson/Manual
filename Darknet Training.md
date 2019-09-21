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
