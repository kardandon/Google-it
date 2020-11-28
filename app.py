from flask import Flask, render_template


app = Flask(__name__)
app.config['SECRET_KEY'] = 'GetRektMur4tReyiz#'
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(threaded=True)
    
