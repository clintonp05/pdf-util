import os
from flask import Flask,send_file,render_template,request
from .config import API_CONF
from .service.pdf_service import mergePDF, imposeImgV2

app = Flask(__name__)
dirname = os.path.dirname(__file__)

print("name",__name__)
print(app)

if __name__ == '__main__':
    app.run()

def echo():
    print('Hello')

echo()    

@app.route("/")
def hello_world():
    print('request received')
    return "<p>Hello, World!</p>"

@app.route('/pdf/mergePDF')
def merge_pdf():
    file = mergePDF()
    return send_file(file,download_name='merged.pdf')

@app.route('/pdf/imposeSignature')
def sign_pdf():
    file = imposeImgV2()
    return send_file(file, download_name='signed.pdf')

@app.route('/pdf/showFileUpload')
def show_file_upload():
    return render_template("index.html")

@app.route('/upload',methods=['POST'])
def upload():
    if request.method == 'POST':
  
        # Get the list of files from webpage
        files = request.files.getlist("file")

        # delete existing files if exists
        print(os.listdir(os.path.join(dirname,"../assets/output/")))
        for file in os.listdir(os.path.join(dirname,"../assets/output/")):
            try:
                os.remove(os.path.join(dirname,"../assets/output/"+file))
            except Exception as e:
                print(e)

        # Iterate for each file in the files List, and Save them
        for file in files:
            file.save(os.path.join(dirname,"../assets/output/",file.filename))
        return "<h1>Files Uploaded Successfully.!</h1>"

if __name__ == '__main__':
    app.run(host=API_CONF['HOST'],port=API_CONF['PORT'],threaded=API_CONF['THREADED'],debug=True)