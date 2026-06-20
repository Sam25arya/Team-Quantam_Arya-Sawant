from flask import Flask, render_template, request
import os
from model import detect_image, detect_document

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/predict",method=["POST"])
def predicit():
  if 'file' not in request.file:
    return "No file part"

file = request.files["file"]

if file.filename == '':
    return "No selected file"

filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
file.save(filepath)

#Calling both detection functions
ai_status = detect_image(filepath)
doc_status = detect_document(filepath)

 return render_template("index.html",ai_result=ai_status,doc_result=doc_status)

if_name_ == "_main_":
app.run(debug=True)

 

                        

 
 
