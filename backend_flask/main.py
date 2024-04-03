from flask import Flask, render_template, request

app = Flask(__name__)

users = []


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form['username'] 
        password = request.form['password'] 
        phone = request.form['phone'] 
        users.append({"username": username, "password": password, "phone": phone})
        return f"Ваш ник: {username}, ваш пароль: {password}, ваш телефон: {phone}"
    

@app.route("/home")
def home():
    return render_template("home.html", users=users)

if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0"
    )