from flask import Flask,render_template,request
from config import config
from app.model.DBSubmitter import DBinfo
app = Flask(__name__)
app.config.from_object(config['development'])
#需要再config中设置db路径和密码
DBinfo.setDatabase(app.config["DATABASE_URI"],app.config["DATABASE_PASSWORD"])
#主页面
@app.route('/')
def home():
    pass
#发送登录请求
@app.route('/login')
def post_login():
    pass

#发送注册请求
@app.route('/register')
def post_register():

    pass
#发送申请请求
@app.route('/post_submit')
def post_submit():
    pass
#修改个人信息
@app.route('/post_revise')
def post_revise():
    pass

if __name__ == '__main__':
    app.run()