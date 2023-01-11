import torch
import numpy as np
import cv2
import matplotlib.pyplot as plt

model = torch.hub.load('ultralytics/yolov5', 'custom', path = 'yolov5/runs/train/exp27/weights/best.pt')

def pipe(path, filename):        
    result = model(path)
    print(result.pandas().xyxy[0])

    result = np.squeeze(result.render())
    plt.imsave(f'C:/Users/lenovo/PycharmProjects/Flask/app/app/static/results/{filename}', result)