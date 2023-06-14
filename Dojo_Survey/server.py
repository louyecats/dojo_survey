from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = "Do not share"

@app.route('/') #http://localhost:5001
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    # print(f"The form is {request.form}")
    session['name']= request.form['user_name']
    session['dojo_location']= request.form['user_dojo_location']
    session['favorite_language']= request.form['user_favorite_language']
    session['comment']= request.form['user_comment']
    return redirect ('/result')

@app.route('/result') #http://localhost:5001/result
def result():
    return render_template('result.html')


if __name__ == "__main__":
    app.run(debug=True, port=5001)