from flask import Flask,jsonify


app = Flask(__name__) #intance of our flask application 

#Route '/' to facilitate get request from our flutter app
@app.route('/', methods = ['GET'])
def index():
    return jsonify({'greetings' : 'Hi! this is python'}) 


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=47678)