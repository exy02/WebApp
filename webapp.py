from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/signUp")
def showSignUp():
    return render_template("signUp.html")


if __name__ == "__main__":
    app.run(port=5002, debug=True)
