from flask import Flask

from src.EntityTypeGenerator import EntityTypeGenerator

app = Flask(__name__)

generator = EntityTypeGenerator()


@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/generate')
def generateEntities():
    return generator.generateArray(10)

@app.route('/youare/<string:value>')
def youare(value):
    return generator.sayYouAre(value)

if __name__ == '__main__':
    app.run(port=8082, debug=True)