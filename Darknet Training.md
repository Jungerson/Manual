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
