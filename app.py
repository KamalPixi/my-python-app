from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return {
        "status": "online",
        "message": "Hello from Flask inside Incus!"
    }

if __name__ == "__main__":
    app.run()
