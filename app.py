from flask import Flask, render_template
import os

template_dir = os.path.abspath('templates')
app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def index():
    return render_template('combined.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)