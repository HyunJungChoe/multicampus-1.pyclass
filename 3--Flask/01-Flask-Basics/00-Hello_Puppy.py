from flask import Flask

# 인스턴스를 생성한다.
app = Flask(__name__)

# 데코레이터 : 이벤트 처리한다.
@app.route('/')
def index():
    return '<h1>Hello Puppy!</h1>'

@app.route('/cat')
def index2():
    return '<h1>Hello Cat~~</h1>'


if __name__ == '__main__':
    app.run()
