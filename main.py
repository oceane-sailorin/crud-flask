from flask import Flask

#display  app
app = Flask(__name__)

@app.route("/")
def home():
    return "My flask app"
  
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

