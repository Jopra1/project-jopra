from flask import Flask

app=Flask(__name__)
@app.route('/')
def mainindex():
    return "This is running on a flask server"
if __name__ == "__main__":
    app.run(debug=True,port=5000)
