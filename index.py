from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/')
# def principal():
#     return "Welcome"

@app.route('/')
def principal():
    return render_template("index.html")

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/languages')
def languages():
    myLanguages = ("Javascript", "Java", "C#", "Go", "PHP", "Javascript", "Perl")
    return render_template('languages.html', languages=myLanguages)


if __name__ == '__main__':
    app.run(debug=True)
     