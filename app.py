from flask import Flask

app = Flask(__name__) 


@api.route('/')  
def get(): 
    return {"hello": "world!"}

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
