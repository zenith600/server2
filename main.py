from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
from werkzeug.utils import secure_filename
from datetime import datetime

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
MAX_UPLOADS = 10000

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024 * 1024  # 1 GB limit

# Counter for uploaded files
uploaded_files_count = 0


def allowed_file(filename):
    return True  # Allow any file or folder


def create_upload_folder():
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    upload_folder_name = f"upload_{timestamp}"
    upload_folder_path = os.path.join(app.config['UPLOAD_FOLDER'], upload_folder_name)
    os.makedirs(upload_folder_path, exist_ok=True)
    return upload_folder_path


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    global uploaded_files_count

    if 'file' not in request.files:
        return redirect(request.url)

    files = request.files.getlist('file')

    if not files:
        return redirect(request.url)

    upload_folder_path = create_upload_folder()

    for file in files:
        if file:
            if uploaded_files_count < MAX_UPLOADS:
                filename = secure_filename(file.filename)
                file_path = os.path.join(upload_folder_path, filename)
                file.save(file_path)
                uploaded_files_count += 1
            else:
                return "Maximum number of files reached (10,000)."

    full_link = url_for('serve_folder_index', folder=os.path.basename(upload_folder_path), _external=True)
    return f"Files uploaded successfully. Full link: {full_link}"


@app.route('/uploads/<path:folder>/<path:filename>')
def serve_file(folder, filename):
    return send_from_directory(os.path.join(app.config['UPLOAD_FOLDER'], folder), filename)


@app.route('/uploads/<path:folder>/')
def serve_folder_index(folder):
    return send_from_directory(os.path.join(app.config['UPLOAD_FOLDER'], folder), 'index.html')


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
