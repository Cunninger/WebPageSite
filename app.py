from flask import Flask, render_template

app = Flask(__name__)

websites = [
    {
        'img_src': 'static/images/example_logo.png',
        'alt_text': 'Example',
        'title': 'Example',
        'description': '这是一个示例平台的描述'
    },
    # 添加更多网站信息...
]

@app.route('/')
def index():
    return render_template('index.html', websites=websites)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)