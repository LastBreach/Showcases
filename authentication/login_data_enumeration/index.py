from flask import Flask, render_template, request, make_response
import md5
app = Flask(__name__, static_folder='../../assets', static_url_path='')

user_db=["admin:admin:admin@lastbreach.com","user:password:user@example.com","bob:s3cr3tb0b:bob@mailinator.com"]

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def download():
    usr = request.form['usr']
    pwd = request.form['pwd']
    for entry in user_db:
        db_usr=entry.split(":")[0]
        db_pwd=entry.split(":")[1]
        if db_usr==usr:
            if db_pwd==pwd:
                status="Login successful"
                return render_template('intern.html', status=status)
            else:
                status="Wrong password!"
                return render_template('index.html', status=status)
        else:
            status="Wrong username!"
    return render_template('index.html', status=status)

@app.route('/forgot', methods=['GET','POST'])
def forgot():
    if request.method == "POST":
        email = request.form['email']
        for entry in user_db:
            db_email=entry.split(":")[2]
            if db_email==email:
                return render_template('forgot.html', status="Password reset link was sent")
        return render_template('forgot.html', status="Email not found!")
    return render_template('forgot.html', status="")

@app.route('/register', methods=['GET','POST'])
def register():
    status=""
    pwd_status=""
    user_status=""
    mail_status=""

    if request.method == "POST":
        user = request.form['user']
        mail = request.form['mail']
        pwd1 = request.form['pwd1']
        pwd2 = request.form['pwd2']

        if user=="" or user==None:
            return render_template('register.html', status="No user specified!")
        if mail=="" or mail==None:
            return render_template('register.html', status="No email specified!")
        if "@" not in mail or "." not in mail:
            return render_template('register.html', status="Please specify a valid email address!")
        if not (pwd1==pwd2 and pwd1!="" and pwd1!=None):
            return render_template('register.html', status="Password missmatch!")
        for entry in user_db:
            db_user=entry.split(":")[0]
            db_mail=entry.split(":")[2]
            if db_user==user:
                return render_template('register.html', status="user not available!")
            if db_mail==mail:
                return render_template('register.html', status="email is already registered!")
        db_entry="%s:%s:%s" % (user, pwd1, mail)
        user_db.append(db_entry)
        return render_template('register.html', status="Thanks for registering!")
    return render_template('register.html', status=status)


if __name__ == '__main__':
    app.run(port=80, debug=True)
