from flask import Flask, render_template, request
app = Flask(__name__, static_folder='../../assets', static_url_path='')


@app.route('/', methods=['GET', 'POST'])
def index():
    status=""
    if request.method == "POST":
        try:
            document = request.form['doc']
            if document in ["123452","123456","123547","123458","123459"]:
                status="Document sent for approval!"
            elif document in ["123460","123461","123466","123450","123453"]:
                status="Access denied!"
            else:
                status="Document not found!"
        except:
            return render_template('index.html', status="")
    return render_template('index.html', status=status)



if __name__ == '__main__':
    app.run(port=80, debug=True)
