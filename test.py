from flask import Flask, redirect, request, render_template, url_for
from flask import session as login_session
import pyrebase



Config = {
  "apiKey": "AIzaSyAGYyO5BLgV3ommDiAvpkdT5lifnK2DX_E",
  "authDomain": "basketball-shop-e1f8e.firebaseapp.com",
  "databaseURL": "https://basketball-shop-e1f8e-default-rtdb.europe-west1.firebasedatabase.app",
  "projectId": "basketball-shop-e1f8e",
  "storageBucket": "basketball-shop-e1f8e.appspot.com",
  "messagingSenderId": "124474074055",
  "appId": "1:124474074055:web:90cb7b98baba3d4c486fe2",
  "measurementId": "G-X1J3W4BV9C",
  "databaseURL" : "https://basketball-shop-e1f8e-default-rtdb.europe-west1.firebasedatabase.app/" 
}


firebase = pyrebase.initialize_app(Config)
auth = firebase.auth()
db = firebase.database()


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'



# Your code should be below
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/gallery')
def gallery():
    return render_template("Gallery.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ""

    if request.method == 'POST':
        username = request.form['Username']
        email = request.form['email']
        password = request.form['password']
        date = request.form['date']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email , password)
            user = {"username": username, "email": email , "password" : password , "date" : date }
            db.child("Users").child(login_session['user']['localId']).set(user)
            return redirect(url_for('home'))
        except :
            error = "Authentication failed"

    return render_template("signup.html")

@app.route('/signin')
def signin():
    return render_template("signin.html")




# Your code should be above

if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)