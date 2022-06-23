
from flask import Flask, render_template, redirect, request, url_for
import data_handler

app = Flask(__name__)
FILE = './sprinter/data.csv'

@app.route('/')
def index():
    user_stories = data_handler.get_all_user_story(FILE)
    return render_template('index.html', user_stories=user_stories)

@app.route('/story')
def route_add():
   return render_template('story.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
    global FILE
    user_list = []
    if request.method == 'POST':
        result = request.form
        for value in result.values():
            user_list.append(value)
        user_list.append('-')
        data_handler.write_user_story(FILE, user_list)
        return render_template('result.html', result=result)
    else:
        return render_template('result.html')







if __name__ == ('__main__'):
    app.run(debug=True)