from flask import Flask, render_template, request, make_response
import md5
app = Flask(__name__, static_folder='../../assets', static_url_path='')

user_db=["admin:password:admin@lastbreach.com","user:s3cr3t:user@example.com","bob:b0b:bob@mailinator.com"]

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
                status="Wrong username or password!"
                return render_template('index.html', status=status)
        else:
            status="Wrong username or password!"
    return render_template('index.html', status=status)

if __name__ == '__main__':
    app.run(port=80, debug=True)
