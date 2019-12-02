#encoding: utf-8
from flask import Flask, render_template,request,redirect,url_for,session
from models import User
from exts import db


import config
app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/',methods=['GET','POST'])
def login():
    if(request.method=='GET'):
        return render_template('login.html')
    else:
        telephone = request.form.get('telephone')
        password = request.form.get('password')
        user = User.query.filter(User.telephone==telephone,User.password==password).first()
        if user:
            session['user_id'] = user.id
            session.pernament = True
            return redirect(url_for('index'))
        else:
            return u'手机号或者密码错误'


@app.route('/register/',methods=['GET','POST'])
def register():
    if(request.method=='GET'):
        return render_template('register.html')
    else:
        telephone = request.form.get('telephone')
        username = request.form.get('username')
        password = request.form.get('password')
        password1 = request.form.get('password1')

        #手机号码如果被注册了，就不能再被注册
        user = User.query.filter(User.telephone==telephone).first()
        if user:
            return u'该手机号已经被注册，请换个手机号再试一次'
        else:
            if password != password1:
                return u'两次返回数据不一致'
            else:
                user=User(telephone=telephone,username=username,password=password1)
                db.session.add(user)
                db.session.commit()
                #如果注册成功，就跳转到登录页面
                return redirect(url_for('login'))
if __name__ == '__main__':
    app.run()
