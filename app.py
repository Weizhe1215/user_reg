from flask import Flask, render_template, request

# 启动flask项目
app = Flask(__name__)


# 注册界面
@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == "GET":
        return render_template('register.html')
    else:
        user = request.form.get("user")
        pwd = request.form.get("pwd")
        gender = request.form.get("gender")
        hobby_list = request.form.getlist("hobby")  # 多个input
        city = request.form.get("city")
        skill_list = request.form.getlist('skill')
        more = request.form.get('more')
        print(user, pwd, gender, hobby_list, city, skill_list, more)
        return "注册成功"

@app.route()



if __name__ == '__main__':
    app.run()
