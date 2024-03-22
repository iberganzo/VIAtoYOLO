# VIAtoYOLO

## YOLO labeling tool for instance segmentation models 

VIAtoYOLO is a tool to convert labeled data from VGG Image Annotator (VIA) tool to YOLO format to train instance segmentation algorithms on YOLO series like YOLOv9. This is an implementation on Python 3.

<img width="1680" alt="via_tool" src="https://github.com/iberganzo/VIAtoYOLO/assets/75735764/721c65ad-7934-43b1-b917-258bea598bea">

### Workflow

1. First of all, you need to annotate all the images you will use as training, validation and testing data. To label the features to be detected in them use VIA tool from the University of Oxford (Dutta and Zisserman, 2019).

VIA: https://www.robots.ox.ac.uk/~vgg/software/via/via_demo.html

YOLO segmentation format for one class: `0 x1 y1 x2 y2 x3 y3 x4 y4 ... xn yn`

2. Save all the labeled JSON files you want to convert to YOLO format in the `/VIA/` folder. Now run the python code `viatoyolo`. Ensure you indicate the size of the images in pixels both horizontally and vertically `--img 512 512`.

```ini
python3 viatoyolo.py --img 1280 768
```

3. The resulting labeled data converted to yolo format (for one class) is saved in `/yolo/` folder. You will find a TXT file for each image inside the JSON files.

YOLOv9: https://github.com/WongKinYiu/yolov9/

### Citation

To cite this repository:

```ini
Berganzo-Besga, I. VIAtoYOLO: YOLO labeling tool for instance segmentation models. GitHub repository 2024. Available online: https://github.com/iberganzo/VIAtoYOLO
```
