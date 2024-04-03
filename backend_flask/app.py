from flask import Flask, request 

app = Flask(__name__) 


@app.route("/") 
def hw(): 
    return "Hello World" 

@app.route("/hello/<name>") 
def hello(name): 
    return f"Hello {name}" 

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == 'GET':
        username = request.args.get('username')
        password = request.args.get('password')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
    else:
        return 'Метод не поддерживается'
    
    return f'Username: {username}, Password: {password}'

if __name__ == "__main__": 
    app.run(
        debug=True, 
        host="0.0.0.0", 
    )   