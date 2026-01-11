from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def hello_world():
    name = request.args.get('username', None) 
    if name:
        return f"Hi {name} , Good to Have you on our website."
    return 'Hello Anonymous User! 🌟 Please log in to enjoy a personalized experience. We have exciting features waiting for you!'

if __name__ == '__main__':
    app.run(debug=True)