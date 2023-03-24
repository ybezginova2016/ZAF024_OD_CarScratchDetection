import os
import torch
import numpy as np
import matplotlib.pyplot as plt

os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

# Initializing Global Variables
MODEL_PATH = "model.pt"
IMAGE_PATH = "test_image.png"


# Function to make prediction
def predict(img_path, model_path):
    model = torch.hub.load('ultralytics/yolov5', 'custom', path = model_path)      
    result = model(img_path)
    print(result.pandas().xyxy[0])

    render_image = np.squeeze(result.render())
    
    plt.imsave("test_image_prediction.png", render_image)

    return result.pandas().xyxy[0]



predict(IMAGE_PATH, MODEL_PATH)
