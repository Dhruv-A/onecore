from flask import Flask, render_template


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def homepage():
  return render_template('home.html')

@app.route('/courses')
def coursepage():
  return render_template('courses.html')

@app.route('/contact')
def contactpage():
  return render_template('contact.html')

@app.route('/puzzles')
def getMainPuzzle():
    return render_template('puzzlesMain.html')

@app.route('/puzzles/<int:postID>')
def getPuzzle(postID):
  return render_template(f'puzzleT{postID}.html')

@app.route('/puzzles/solution/<int:postID>')
def getPuzzleSolution(postID):
  return render_template(f'puzzleST{postID}.html')

@app.route('/dev')
def devpage():
  return render_template('dev.html')

@app.route('/python/<int:postID>')
def pyTutorial(postID):
  return render_template(f'pyT{postID}.html')

@app.route('/html/<int:postID>')
def htmlTutorial(postID):
  return render_template(f'htmlT{postID}.html')

@app.route('/react/<int:postID>')
def reactTutorial(postID):
  return render_template(f'reactT{postID}.html')

@app.route('/informatics/<int:postID>')
def infoTutorial(postID):
  return render_template(f'infoT{postID}.html')

@app.route('/hsc')
def getHsc():
  return render_template(f'hsccourses.html')

@app.route('/maths/<int:postID>')
def mathsTutorial(postID):
  return render_template(f'mathsT{postID}.html')

@app.route('/e1maths/<int:postID>')
def e1mathsTutorial(postID):
  return render_template(f'e1mathsT{postID}.html')

@app.route('/e2maths/<int:postID>')
def e2mathsTutorial(postID):
  return render_template(f'e2mathsT{postID}.html')

@app.route('/chem/<int:postID>')
def chemTutorial(postID):
  return render_template(f'chemT{postID}.html')

@app.route('/phys/<int:postID>')
def physTutorial(postID):
  return render_template(f'physT{postID}.html')

@app.route('/english/<int:postID>')
def englishTutorial(postID):
  return render_template(f'englishT{postID}.html')

@app.route('/bio/<int:postID>')
def bioTutorial(postID):
  return render_template(f'bioT{postID}.html')

@app.route('/eco/<int:postID>')
def ecoTutorial(postID):
  return render_template(f'ecoT{postID}.html')

@app.route('/e1english/<int:postID>')
def e1englishTutorial(postID):
  return render_template(f'e1englishT{postID}.html')

app.run(host='0.0.0.0', threaded=True)