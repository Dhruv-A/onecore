from flask import Flask, render_template


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def homepage():
  return render_template('home.html')

@app.route('/courses')
def coursepage():
  return render_template('courses.html')

@app.route('/python/<int:postID>')
def pyTutorial(postID):
  return render_template(f'pyT{postID}.html')

@app.route('/contact')
def contactpage():
  return render_template('contact.html')

@app.route('/puzzles')
def puzzlehome():
  return render_template('puzzlesMain.html')

@app.route('/dev')
def devpage():
  return render_template('dev.html')

app.run(host='0.0.0.0', threaded=True)