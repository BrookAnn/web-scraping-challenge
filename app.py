from flask import Flask, render_template, redirect
from pymongo import MongoClient
import MarsMission


app = Flask(__name__)


mongo = MongoClient("mongodb://localhost:27017/scraped")



@app.route("/")
def home():

    
    scraped_data = mongo.db.scraped_data.find_one()

   
    return render_template("index.html", scraped=scraped_data)



@app.route("/scrape")
def scrape():

    
    data_scraped = MarsMission.data_scrape()

   
    mongo.db.scraped_data.update({}, data_scraped, upsert=True)

   
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
