from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def index():
    ip_add = request.remote_addr
    browser = request.headers.get("User-Agent")
    return(render_template("index.html",ip = ip_add, browserCliente = browser))

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8081,debug=True)
