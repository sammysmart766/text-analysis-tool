from flask import Flask

app = Flask(__name__)

@app.route("/health")
def home():
    return "Flask server is up and running."

if __name__ == "__main__":
    app.run()