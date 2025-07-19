from flask import Flask, request

app = Flask(__name__)

@app.route("/add")
def add():
    a = request.args.get("a", type=int, default=0)
    b = request.args.get("b", type=int, default=0)
    return f"{a} + {b} = {a + b}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)