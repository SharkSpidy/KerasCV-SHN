from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return render_template('index.html', error='No file part')
    file = request.files['file']
    if file.filename == '':
        return render_template('index.html', error='No selected file')
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        # Process the uploaded image (e.g., apply your model)
        # Replace the following line with your image processing code
        # processed_image = process_image(filepath)
        processed_image = filepath  # For demonstration, just return the uploaded image
        return render_template('index.html', image_file=processed_image)
    else:
        return render_template('index.html', error='Invalid file format')

if __name__ == '__main__':
    app.run(debug=True)