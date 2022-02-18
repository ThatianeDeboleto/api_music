from flask import Flask, render_template, redirect, url_for,flash
import os

app = Flask(__name__)
app.debug = True


@app.route('/', methods=['POST', 'GET'])
def hello():
    return render_template('index.html')


@app.route('/stream', methods=['POST', 'GET'])
def stream():
    songs = os.listdir('static/music')
    return render_template('music.html', songs=songs)


if __name__ == '__main__':
    app.run()
