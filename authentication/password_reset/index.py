from flask import Flask, render_template, request, make_response
import md5
app = Flask(__name__, static_folder='../../assets', static_url_path='')

user_db=["admin:admin:admin@lastbreach.com","user:password:user@example.com","bob:s3cr3tb0b:bob@mailinator.com"]

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# send cleartext password
@app.route('/forgot1', methods=['POST'])
def forgot1():
    email = request.form['email']
    for entry in user_db:
        db_email=entry.split(":")[2]
        if db_email==email:
            return render_template('index.html', status1="Sent, check your mail!", status2="", status3="")
    return render_template('index.html', status1="", status2="", status3="")

@app.route('/reset1', methods=['GET'])
def reset1():
    token = request.args['token']
    user = request.args['user']
    for entry in user_db:
        db_email=entry.split(":")[2]
        if db_email==email:
            return render_template('index.html', status1="Sent, check your mail!", status2="", status3="")
    return render_template('index.html', status1="", status2="", status3="")

# send guessable link
@app.route('/forgot2', methods=['POST'])
def forgot2():
    email = request.form['email']
    for entry in user_db:
        db_email=entry.split(":")[2]
        if db_email==email:
            return render_template('index.html', status1="Sent, check your mail!", status2="", status3="")
    return render_template('index.html', status1="", status2="", status3="")


@app.route('/reset2', methods=['POST'])
def reset2():
    email = request.form['email']
    for entry in user_db:
        db_email=entry.split(":")[2]
        if db_email==email:
            return render_template('index.html', status1="Sent, check your mail!", status2="", status3="")
    return render_template('index.html', status1="", status2="", status3="")

# send link with user reset time based activation
@app.route('/forgot3', methods=['POST'])
def forgot3():
    email = request.form['email']
    for entry in user_db:
        db_email=entry.split(":")[2]
        if db_email==email:
            return render_template('index.html', status1="Sent, check your mail!", status2="", status3="")
    return render_template('index.html', status1="", status2="", status3="")

@app.route('/reset3', methods=['POST'])
def reset3():
    email = request.form['email']
    for entry in user_db:
        db_email=entry.split(":")[2]
        if db_email==email:
            return render_template('index.html', status1="Sent, check your mail!", status2="", status3="")
    return render_template('index.html', status1="", status2="", status3="")


if __name__ == '__main__':
    app.run(port=80, debug=True)
