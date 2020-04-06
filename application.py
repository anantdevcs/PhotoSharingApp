from flask import Flask, render_template, request, session, flash, redirect

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
from flask import Flask, render_template, request

class users_db(db.Model):
    __tablename__ = "users_databse"
    user_id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable = True)
    profile_picture_name = db.Column(db.String, nullable = True)
    shared_file_name = db.Column(db.String, nullable = True)
    num_downloads = db.Column(db.Integer, nullable = True)
    num_uploads = db.Column(db.Integer, nullable = True)
    password = db.Column(db.String, nullable = True)

    


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://nnvydxolfxvmeu:16a5836b229ffba2dae8e201fa8766f4e8b930a4e5cfeb20cce2ca35ed3e24cc@ec2-52-6-143-153.compute-1.amazonaws.com:5432/dbbjpu2jer1pkr"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
app.secret_key = "abc"  


@app.route('/')
def index():
    if 'user_id' in session :

        return render_template('index.html',user_dict = session )
    else:
        return render_template('index.html')

@app.route('/login', methods = ['POST', 'GET'])

def login():
    if request.method == 'GET':
        return render_template('login.html', user_db = session)
    else :
        user_id = request.form['user_id']
        password = request.form['password']
        if users_db.query.filter_by(user_id = user_id ).first() is not None:
            session['user'] = user_id
            return redirect('/')
        else:
            flash('Username or password are invalid')
            return render_template('index.html', user_dict = session)

        


def create():
    db.create_all()

if __name__ == '__main__':
    with app.app_context():
        create()
        app.run(debug = True)