from flask import Flask
from flask import request
app = Flask(__name__)


@app.route('/')
def index():
    # Grab the visitors User Agent information
    browser_info = request.headers.get('User-Agent')
    return f'<h2>Here is your browser info:</h2> <p>{browser_info}</p>'

if __name__ == '__main__':
    app.run(debug=True)

'''
새 서버 환경 설정 
mkdir MyWebServer
cd MyWebServer
python -m venv venv
.\venv\Scripts\activate 
pip list
pip install flask

deactivate
'''