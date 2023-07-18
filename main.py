from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import json
# from datetime import datetime

with open('config.json','r') as c:
    params=json.load(c)["params"]
local_server=True

app=Flask(__name__)
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT='465',
    MAIL_USE_SSL=True,
    MAIL_USERNAME=params['gmail-user'],
    MAIL_PASSWORD=params['gmail-password']
)
mail=Mail(app)

if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

class Contacts(db.Model):
    '''
    S_Num,Name,Email,P_Num,Message,Date
    '''
    s_num = db.Column(db.Integer, primary_key=True)
    name = db.Column("name",db.String(80), nullable=False)
    email = db.Column("email",db.String(20), nullable=False)
    phn_num = db.Column("phone",db.String(12), nullable=False)
    msg = db.Column("message",db.String(120), nullable=False)
    # Date = db.Column(db.String(12), nullable=True)

class Post(db.Model):
    '''
    s_num,title,slug,content,date
    '''
    s_num = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    slug = db.Column(db.String(21), nullable=False)
    content = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)


@app.route("/")
def home():
    return render_template('index.html',params=params)

@app.route("/about")
def about():
    return render_template('about.html',params=params)

@app.route("/post",methods=['GET'])
def post_route():
    # post=Post.query.filter_by(slug=post_slug).first()
    return render_template('post.html',params=params)

@app.route("/contact",methods=['POST','GET'])
def contact():
    if(request.method=='POST'):
        '''Add entry to the database'''
        name=request.form.get('name')
        email=request.form.get('email')
        phone=request.form.get('phone')
        message=request.form.get('message')

        entry=Contacts(name=name,phn_num=phone,msg=message,email=email)

        db.session.add(entry)
        db.session.commit()

        mail.send_message('New message from'+name,
                          sender=email,
                          recipients=[params['gmail-user']],
                          body=message +"\n"+phone)#to recieve email from app

    return render_template('contact.html',params=params)

app.run(debug=True)