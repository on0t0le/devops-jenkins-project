from flask import Flask

app = Flask(__name__)
@app.route("/")
def home():
    html = "<h3>Hello!</h3>" \
           "<p>And, again</p>" \
           "<h2>Welcome to <h2>" \
           "<h1>The Aperture Sciense computer-aided Enrichment Center</h1><br/>" \
           "<b>Hostname:</b> {hostname}"
                      
    return html.format(hostname=socket.gethostname())
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',port=80)