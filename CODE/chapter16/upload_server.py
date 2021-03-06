import os
from flask import Flask, request


UPLOAD_FOLDER = 'uploads'
app = Flask(__name__)


@app.route('/', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
        return "文件上传成功"

if __name__ == '__main__':
    app.run()
