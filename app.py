
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    message = "欢迎来到我的动态网站!"
    return render_template('index.html', message=message)

@app.route('/diary')
def diary():
    return render_template('pages/diary.html')

@app.route('/social')
def social():
    return render_template('pages/social.html')

@app.route('/study')
def study():
    return render_template('pages/study.html')

@app.route('/debugStudy')
def debugStudy():
    return render_template('pages/debugStudy.html')

@app.route('/cssStudy')
def cssStudy():
    return render_template('pages/cssStudy.html')

@app.route('/jsStudy')
def jsStudy():
    return render_template('pages/jsStudy.html')

@app.route('/ML')
def ML():
    return render_template('pages/ML.html')

@app.route('/WeightRecorder')
def WeightRecorder():
    return render_template('pages/WeightRecorder.html')

if __name__ == '__main__':
    app.run(debug=True)