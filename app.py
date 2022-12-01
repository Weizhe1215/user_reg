from flask import Flask, render_template, request

# 启动flask项目
app = Flask(__name__)


# 定义网址后缀
@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/do/reg')
def do_register():
    print(request.args)
    return "注册成功"


if __name__ == '__main__':
    app.run()
