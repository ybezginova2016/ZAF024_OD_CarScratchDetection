# ZAF024_OD_CarScratchDetection

## Overview
Car scratch detection using computer vision is a project that aims to automatically identify and localize scratches on car surfaces using image processing techniques. This project has significant applications in the automotive industry, where car manufacturers and car owners require a reliable and efficient method for detecting and repairing scratches. By automating the process of scratch detection, this project has the potential to save time and reduce costs for car manufacturers and owners while improving the quality of car repair services.

## Methodology
This use case follows the methodology mentioned below:
- Data Preparation:
The first step is to collect and prepare the car scratch detection dataset. The dataset should include images of car surfaces with and without scratches, and annotations that indicate the location of the scratches. The annotations could be in the form of bounding boxes, masks, or keypoints. The dataset should be split into training, validation, and test sets.

- Model Selection:
The next step is to select the YOLOv5 model architecture for fine-tuning. You can choose from various pre-trained models available on the official YOLOv5 GitHub repository.

- Preprocessing:
Before training the YOLOv5 model, you need to preprocess the car scratch detection data. This could involve resizing the images, normalizing the pixel values, and augmenting the data to increase its variability. Common data augmentation techniques for object detection include random cropping, flipping, rotation, and color jittering.

- Fine-tuning:
The YOLOv5 model can be fine-tuned on the car scratch detection dataset using transfer learning. Transfer learning involves using a pre-trained model as a starting point and fine-tuning it on a new dataset. In this case, you will fine-tune the pre-trained YOLOv5 model on the car scratch detection dataset to learn the specific features and patterns of car scratches.

- Training:
The fine-tuned YOLOv5 model can be trained using the training set and validated using the validation set. During training, the model learns to predict the location and size of scratches in the input images. You can monitor the training progress using metrics such as mean average precision (mAP) and loss.

- Evaluation:
Once the YOLOv5 model is trained, you can evaluate its performance on the test set. This involves measuring its accuracy, precision, recall, and F1-score on the test images. You can also visualize the predicted bounding boxes on the test images to see how well the model is detecting scratches.

- Deployment:
The final step is to deploy the YOLOv5 model for car scratch detection. This could involve integrating it into a mobile or web application, or using it as a backend for an automated car repair system. You can also fine-tune the model on new car scratch detection data to improve its performance over time.

## Business Segments
- Automotive Industry

## Data
- Car Scratch Detection Data - [Link](https://www.kaggle.com/datasets/aniketmalviya/car-scratch-detection)

## Papers
- YOLOv5 - [Link](https://zenodo.org/record/7347926#.ZBzP8XZBy3A)

 ## Instructions
 In order to use this model, follow the below steps:
1. Clone the repository into your local system.
```
git clone https://github.com/ybezginova2016/ZAF024_OD_CarScratchDetection
```
2. Install the required dependencies using pip.
```
pip install -r requirements.txt
```

3. Run the 'load_predict.py' to launch car scratch detection model and make prediction on given test image. 