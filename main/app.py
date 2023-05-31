from flask import Flask
from service.pdf_service import mergePDF, imposeImgV2

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('pdf/mergePDF')
class MergePDF():
    mergePDF()


@app.route('pdf/imposeSignature')
class SignPDF():
    imposeImgV2()

if __name__ == '__main__':
    app.run()
