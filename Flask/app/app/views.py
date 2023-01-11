from main import pipe
from app import app
from flask import render_template, request
from PIL import Image
import os


UPLOAD_FOLDER = 'C:/Users/lenovo/PycharmProjects/Flask/app/app/static/uploads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

def getwidth(path):
    img = Image.open(path)
    size= img.size # width and height
    aspect = size[0]/size [1]# width / height
    w = 300 * aspect
    return int(w)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method=='POST':
        if request.files:
            image = request.files['image']
            filename = image.filename
            print(filename)
            path = UPLOAD_FOLDER+'/'+filename
            print(path)
            image.save(path)
            print('Image Saved')
            w = getwidth(path)
            # predictions 
            pipe(path,filename)

            
            return render_template('predict.html', fileupload=True, img_name=filename,w=w)
            
        
    return render_template('predict.html', fileupload=False,  img_name="", w=300)