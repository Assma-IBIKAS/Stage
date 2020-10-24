from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class Employe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom_prenom = db.Column(db.String(30), nullable=False)
    tel = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    photo = db.Column(db.String(50), unique=True, nullable=False)
    dateN = db.Column(db.String(30), nullable=False)
    adresse = db.Column(db.String(100), nullable=False)
    


@app.route('/')
def test():
    return "hiiii"

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/admin')
def admin():
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)