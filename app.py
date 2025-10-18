from flask import Flask, render_template
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    debug = os.getenv("DEBUG", "True")
    app.run(debug=debug == "True" or debug == "1")
