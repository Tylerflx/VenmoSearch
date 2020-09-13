from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/login')
def log_in():
    return 'Log In Page'

@app.route('/upload', methods=['GET', 'POST'])
def upload_pic():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('templates/images/uploaded_file.jpg')
    return 'Upload'
if __name__ == '__main__':
    app.run()