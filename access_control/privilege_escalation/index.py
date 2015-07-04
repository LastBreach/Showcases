from flask import Flask, render_template, request, make_response
import md5
app = Flask(__name__, static_folder='../../assets', static_url_path='')

# Fake "databases" containing all document IDs and their relations (to keep it simple - it's a showcase!)
docs=["123452","123456","123547","123458","123459","123460","123461","123466","123450","123453"]
userdocs=["123452","123456","123547","123458","123459"]
denydocs=[["123460","123461","123466","123450","123453"]]

@app.route('/', methods=['GET', 'POST'])
def index():
    status=""
    linkname=""
    if request.method == "POST":
        try:
            req_docid = request.form['doc']
            docsum=md5.new(req_docid).hexdigest() #md5
            if req_docid in userdocs:
                status="/download?doc=%s" % docsum
                linkname="Download Link"
            else:
                status="Document not found!"
        except:
            return render_template('index.html', status="", linkname="")
    return render_template('index.html', status=status, linkname=linkname)

@app.route('/download', methods=['GET'])
def download():
    req_docsum = request.args['doc']
    for doc in docs:
        docsum=md5.new(doc).hexdigest()
        if docsum==req_docsum:
            csv="Private userdata for employee nr. %s" % doc
            response = make_response(csv)
            response.headers["Content-Disposition"] = "attachment; filename=report.csv"
            return response
    return "404 - page not found!"

if __name__ == '__main__':
    app.run(port=80, debug=True)
