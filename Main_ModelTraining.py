from ultralytics import YOLO
import ultralytics.engine.model


model = YOLO("yolov8.pt")
hyp = {}
hyp['hsv_h']= 0.0 # image HSV-Hue augmentation (fraction)
hyp['hsv_s']= 0.5 # image HSV-Saturation augmentation (fraction)
hyp['hsv_v']= 0.4 # image HSV-Value augmentation (fraction)
hyp['degrees']= 0.0 # image rotation (+/- deg)
hyp['translate']= 0.1 # image translation (+/- fraction)
hyp['scale']= 0.0 # image scale (+/- gain)
hyp['shear']= 0.0 # image shear (+/- deg)
hyp['perspective']= 0.0 # image perspective (+/- fraction), range 0-0.001
hyp['flipud']= 0.5 # image flip up-down (probability)
hyp['fliplr']= 0.5 # image flip left-right (probability)
hyp['mosaic']= 0.5 # image mosaic (probability)
hyp['mixup']= 0.0 # image mixup (probability)
hyp['copy_paste']= 0.1 # segment copy-paste (probability)
#hyp['erasing'] = 0.3 #  erases a portion of the image
hyp['device']=[0,1,2,3]
# Use the model
if __name__ == '__main__': 
    metrics = model.train(**hyp, data="./config_2.yaml", 
                epochs=50, imgsz=640, batch=8, plots=True)
    print('====================end=================')
    print(metrics)