from flask import Flask, render_template, request, session, url_for, redirect
import os
from markupsafe import escape
app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# homepage
@app.route('/', methods=['GET', 'POST'])
def index():
    # if user logged in
    if 'username' in session:
        user = session['username']
        print(user)
        return '''<!DOCTYPE html>
        <html>
        <body>
        <h1> Hello {}</h1>
        </body>
        </html>
        '''.format(escape(user))
    else:
        # if not then if the request is post for username and password
        if request.method =='POST':
            session['username'] = request.form['username']
            session['password'] = request.form['password']
            return redirect(url_for('index'))
    return '''{}'''.format(escape(user))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

# to upload profile picture or new QR code
@app.route('/upload', methods=['GET', 'POST'])
def upload_pic():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('templates/images/uploaded_file.jpg')
    return  '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
# for error page
@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404

if __name__ == '__main__':
    # for reload other files purposes
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, host='0.0.0.0')