from flask import Flask, render_template, redirect, request
from script import model

app = Flask(__name__)

@app.route('/', methods=['GET',"POST"])
def home():
    if request.method == "POST":
        link = request.form.get('link')
        summary = model(link)
        return render_template('result.html', summary=summary)
    return render_template('index.html')


if __name__ == "__main__":
    app.run()

