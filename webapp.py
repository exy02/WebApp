from flask import Flask, render_template, json, request, redirect, session, jsonify
from flaskext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash

mysql = MySQL()
app = Flask(__name__)

# randomly generated encryption & decryption key, ensures security of a communications session
app.secret_key = "captain knuckles?"
# MySQL configurations
app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = "ohgodwhyisthis!"
app.config["MYSQL_DATABASE_DB"] = "milestone"
app.config["MYSQL_DATABASE_HOST"] = "localhost"
mysql.init_app(app)
# ==============================================================================

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/signUp")
def showSignUp():
    return render_template("signUp.html")

# ==============================================================================
# SIGN UP
@app.route("/signUp",methods=["POST","GET"])
def signUp():
    try:
        _name = request.form["inputName"]
        _email = request.form["inputEmail"]
        _password = request.form["inputPassword"]

        # validates input values
        if _name and _email and _password:
            conn = mysql.connect()
            cursor = conn.cursor()
            _hashed_password = generate_password_hash(_password)
            cursor.callproc("sp_createUser",(_name,_email,_hashed_password))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return jsonify({"message":"User created successfully !"})
            else:
                return jsonify({"error":"User already exists !"})
        else:
            return jsonify({"error":"Enter all required fields"})

    except Exception as e:
        return jsonify({"error":str(e)})

    finally:
        cursor.close()
        conn.close()
# ==============================================================================
# ==============================================================================
# ==============================================================================


# =====================================================
# FOR REALTIME DEBUGGING AND UPDATE WITHOUT APP RESTART
if __name__ == "__main__":
    app.run(port=5002, debug=True)
# =====================================================
