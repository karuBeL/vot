import datetime
from io import BytesIO
import bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user
import sqlite3
from flask import Flask, request, json, send_file
from flask import render_template
from flask_wtf import FlaskForm
from werkzeug.utils import secure_filename
from wtforms import FileField, SubmitField, StringField
import os
from wtforms.validators import InputRequired

app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)
curr_user = None

basedir = os.path.abspath(os.path.dirname(__file__))

DB_FILENAME = "myDatabase.db"

app.config['SECRET_KEY'] = "secretkey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, DB_FILENAME)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp4'}



conn = sqlite3.connect(DB_FILENAME)
cursor = conn.cursor()

db = SQLAlchemy(app)


class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")
    receiver = StringField("Receiver", validators=[InputRequired()])


class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    filecontent = db.Column(db.LargeBinary, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f'<File {self.filename}>'


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)


class MyFileClass:
    filename = ""
    time = ""
    sender = ""

    def __init__(self, filename, time, sender):
        self.filename = filename
        self.time = time
        self.sender = sender


def CurrentUserFiles():
    files = File.query.filter_by(receiver_id=current_user.id).all()
    filelist = []
    for file in files:
        name = User.query.filter_by(id=file.owner_id).first().username
        filelist.append(MyFileClass(file.filename, str(file.timestamp), name))
    return filelist


def SentFiles():
    files = File.query.filter_by(owner_id=current_user.id).all()
    filelist = []
    for file in files:
        name = User.query.filter_by(id=file.receiver_id).first().username
        filelist.append(MyFileClass(file.filename, str(file.timestamp), name))
    return filelist


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/homepage', methods=["GET", "POST"])
@login_required
def homepage():
    form = UploadFileForm()
    if form.validate_on_submit():
        if User.query.filter_by(username=form.receiver.data).first() is None:
            return "Receiver does not exist"
        file = form.file.data
        print(form.receiver.data)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            receiver_id = User.query.filter_by(username=form.receiver.data).first().id
            new_file = File(filename=filename, owner_id=current_user.id,
                            filecontent=file.read(), receiver_id=receiver_id)
            db.session.add(new_file)
            db.session.commit()
        else:
            return "file extension not allowed"
    return render_template('homepage.html', form=form)


@app.route('/downloads', methods=['GET', 'POST'])
def downloads():
    received_files = CurrentUserFiles()
    sent_files = SentFiles()
    return render_template('downloads.html', received_files=received_files, sent_files=sent_files)


@app.route('/download_file', methods=['GET', 'POST'])
def download_file():
    file = File.query.filter_by(filename=request.args.get('file')).first()
    return send_file(BytesIO(file.filecontent), download_name=file.filename, as_attachment=True)


@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username and password:
        if validateUserSignUp(username, password):
            return homepage()
        return json.dumps({'validation': False})
    return json.dumps({'validation': False})


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


def validateUserLogIn(username, password):
    user = User.query.filter_by(username=username).first()
    hashed_password = user.password
    if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
        login_user(user)
        return True
    else:
        return False


def validateUserSignUp(username, password):
    user = User.query.filter_by(username=username).first()
    if user is None:
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        new_user = User(username=username, password=hashed_password)
        login_user(new_user)
        db.session.add(new_user)
        db.session.commit()
        return True
    else:
        return validateUserLogIn(username, password)


def create_db():
    with app.app_context():
        db.create_all()


if __name__ == '__main__':
    create_db()
    app.run(debug=True)
