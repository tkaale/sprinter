
from flask import Flask, render_template, redirect, request, url_for
import data_handler

app = Flask(__name__)
FILE = './sprinter/data.csv'

@app.route('/')
def index():
    user_stories = data_handler.get_all_user_story(FILE)
    return render_template('index.html', user_stories=user_stories)

@app.route('/story')
@app.route('/story/<id>', methods = ['POST', 'GET'])
def story(id):
    
    return render_template('story.html')




if __name__ == ('__main__'):
    app.run(debug=True)