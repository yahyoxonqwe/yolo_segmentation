# Window segmantation with [Yolov8 segmentation](https://docs.ultralytics.com/tasks/segment/)
YOLOv8 is a state-of-the-art object detection algorithm known for its high accuracy and real-time performance. It's particularly effective when it comes to instance segmentation, which involves identifying and delineating individual objects within an image. 
YOLOv8 provides precise bounding boxes and accurate masks, making it an excellent choice for tasks that require pixel-level analysis.

[Dataset download](https://universe.roboflow.com/roboflow-universe-projects/windows-instance-segmentation/dataset/5)

# Installation
Clone the repository:
``` bash
git clone https://github.com/yahyoxonqwe/yolo_segmentation.git
```
Change into the project directory:
``` bash
cd yolo_segmentation
```
Install the required dependencies:
``` bash
pip install -r requirements.txt
```
## Predict

``` bash
python predict.py
```

## Demo
![video](output.gif)
