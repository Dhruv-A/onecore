from flask import Flask, render_template, redirect


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def homepage():
  return render_template('homenew.html')

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
  prev = postID - 1
  next = postID + 1
  return render_template(f'pyT{postID}.html', prev=prev, next=next)

@app.route('/html/<int:postID>')
def htmlTutorial(postID):
  return render_template(f'htmlT{postID}.html')

@app.route('/react/<int:postID>')
def reactTutorial(postID):
  return render_template(f'reactT{postID}.html')

@app.route('/informatics/<int:postID>')
def infoTutorial(postID):
  prev = postID - 1
  next = postID + 1
  return render_template(f'infoT{postID}.html', prev=prev, next=next)

@app.route('/csharp/<int:postID>')
def csharpTutorial(postID):
  prev = postID - 1
  next = postID + 1
  return render_template(f'csharpT{postID}.html', prev=prev, next=next)

@app.route('/invite')
def discordinv():
  return redirect('https://discord.com/invite/2d27eyG')

app.run(host='0.0.0.0', threaded=True, debug=False)