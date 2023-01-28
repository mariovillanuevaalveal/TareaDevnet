from flask import Flask,request
app = Flask(__name__)

@app.route("/")
def index():
    ip_add = request.remote_addr
    return("Su ip es " + ip_add)


##Principal
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000,debug=True)