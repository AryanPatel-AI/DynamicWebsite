from flask import Flask, render_template
from pymongo import MongoClient

client = MongoClient("mongodb+srv://aryanpatel66871_db_user:IOEocBjcsqUkqYcP@cluster0.letklkj.mongodb.net/?appName=Cluster0")
mydb = client["portfolio"]
mycol = mydb["profiles"]
data = mycol.find_one()

app = Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html", name=data['name'])

if __name__ == "__main__":
    app.run(debug=True)