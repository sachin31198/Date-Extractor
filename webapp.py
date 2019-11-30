from flask import Flask, render_template, request
from werkzeug import secure_filename
from PIL import Image
import pytesseract
import re


app = Flask(__name__)

@app.route('/upload')
def upload_file1():
   return render_template('upload.html')
	
@app.route('/results', methods = ['GET', 'POST'])
def upload_file2():
   if request.method == 'POST':
      f = request.files['file']
      nom_image = secure_filename(f.filename)
      image = Image.open(f)
      mystr=pytesseract.image_to_string(image)
      match = re.findall(r'(\d+/\d+/\d+)',mystr)
      if len(match)==0:
             return "<h1>No Dates Found</h1>"
      return render_template('results.html',matches=match)
		
if __name__ == '__main__':
   app.run(debug = True)
